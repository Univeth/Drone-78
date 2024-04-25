import time
import socket
from machine import Pin


def udp_send(message):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = ("192.168.10.1", 8889)  # Tello drone address
    sock.sendto(message.encode(), tello_address)
    sock.close()


def remote_control():
    # Setup buttons
    n = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Assuming pin 16 is connected to 'n' button
    d = Pin(17, Pin.IN, Pin.PULL_DOWN)  # Assuming pin 17 is connected to 'd' button

    while True:
        if n.value() == 1:
            print("Takeoff button pressed")
            udp_send("takeoff")
            time.sleep(
                0.5
            )  # Delay to avoid sending multiple commands in quick succession

        if d.value() == 1:
            print("Land button pressed")
            udp_send("land")
            time.sleep(
                0.5
            )  # Delay to avoid sending multiple commands in quick succession

        time.sleep(0.1)  # Adjust as needed to control the button polling rate
