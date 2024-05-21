from djitellopy import tello
import cv2

# Initialize Tello drone
me = tello.Tello()
me.connect()

# Print battery level functionnnnn 
def display_battery():
    battery_level = me.get_battery()
    print("Battery Level:", battery_level)

# Turn off stream (just in case)
me.streamoff()

# Turn on stream
me.streamon()

while True:
    # Get frame from Tello drone
    img = me.get_frame_read().frame
    
    # Convert color space from BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display the image
    cv2.imshow("Image", img_rgb)
    
    # "q" Lukker Python-vinduet. "b" printer batteri-niveauet i terminalen. 
    if cv2.waitKey(5) & 0xFF == ord("q"):
        me.streamoff()
        break
    if cv2.waitKey(5) & 0xFF == ord("b"):
            display_battery()

# Close OpenCV windows
cv2.destroyAllWindows()
