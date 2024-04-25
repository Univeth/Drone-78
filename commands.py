import socket
import sys
from machine import Pin
from time import sleep

# UDEN THREADING
# UDEN THREADING
# UDEN THREADING


def command2():
    host = ""
    port = 9000
    locaddr = (host, port)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    tello_address = ("192.168.10.1", 8889)

    sock.bind(locaddr)

    print("\r\n\r\nTello\r\n")
    print("end -- quit demo.\r\n")

    n = Pin(16, mode=Pin.IN, pull=Pin.PULL_DOWN)
    d = Pin(17, mode=Pin.IN, pull=Pin.PULL_DOWN)

    while True:
        try:
            msg = "command"

            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)

            if n.value() == 1:
                print("Takeoff...")
                msg = "takeoff".encode(encoding="utf-8")
                sent = sock.sendto(msg, tello_address)
                sleep(0.5)

            if d.value() == 1:
                print("Landing...")
                msg = "land".encode(encoding="utf-8")
                sent = sock.sendto(msg, tello_address)
                sleep(0.5)

            sleep(0.1)

        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break
