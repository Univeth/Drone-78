import cv2

cap = cv2.VideoCapture("udp://@0.0.0.0:11111")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Tello Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
