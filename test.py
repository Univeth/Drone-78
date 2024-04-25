#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import socket
import sys
import time


def test():
    host = ""
    port = 9000
    locaddr = (host, port)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    tello_address = ("192.168.10.1", 8889)

    sock.bind(locaddr)

    print("\r\n\r\nTello Python3 Demo.\r\n")

    print(
        "Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n"
    )

    print("end -- quit demo.\r\n")

    # recvThread create

    while True:

        try:
            msg = input("")

            if not msg:
                break

            if "end" in msg:
                print("...")
                sock.close()
                break

            # Send data
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break
