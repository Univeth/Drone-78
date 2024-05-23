import cv2
import threading
import pygame
from djitellopy import Tello

# Initialize Pygame and joystick
pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# Initialize Tello
tello = Tello()
tello.connect()
tello.streamon()

# Function to handle video streaming
def video_stream():
    while True:
        frame = tello.get_frame_read().frame
        cv2.imshow('Tello Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    tello.streamoff()
    cv2.destroyAllWindows()

# Function to handle drone control
def drone_control():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(0):  # Example button for takeoff
                    tello.takeoff()
                elif joystick.get_button(1):  # Example button for land
                    tello.land()

        # Get joystick axes
        axis_0 = joystick.get_axis(0)
        axis_1 = joystick.get_axis(1)

        # Convert axis input to drone movement
        if axis_0 < -0.5:
            tello.move_left(20)
        elif axis_0 > 0.5:
            tello.move_right(20)

        if axis_1 < -0.5:
            tello.move_forward(20)
        elif axis_1 > 0.5:
            tello.move_back(20)

if __name__ == '__main__':
    # Create threads for video streaming and drone control
    video_thread = threading.Thread(target=video_stream)
    control_thread = threading.Thread(target=drone_control)

    # Start the threads
    video_thread.start()
    control_thread.start()

    # Wait for threads to complete
    video_thread.join()
    control_thread.join()

    # Quit Pygame
    pygame.quit()