import socket
import network
from time import sleep
import utime
import _thread
from machine import Pin
import komponenter
import kommandoer


def send_command():
    # NETWORK WI-FI CONNECT
    host = ""
    port = 9000
    locaddr = (host, port)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("TELLO-E9C6E8", "")
    while not wlan.isconnected():
        sleep(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = ("192.168.10.1", 8889)
    sock.bind(locaddr)

    # THREADING
    def recv():
        while True:
            try:
                data, addr = sock.recvfrom(1518)
                print(data.decode("utf-8"))
            except KeyboardInterrupt:
                print("\nExit . . .\n")
                break

    recv_thread = _thread.start_new_thread(recv, ())

    print("\r\n\r\nPress button ->\r\n")

    DEADZONE_THRESHOLD = 5000

    # SEND COMMANDS
    def send_command(command):
        command = command.encode("utf-8")
        sent = sock.sendto(command, tello_address)

    send_command(kommandoer.command())
    sleep(1)

    while True:
        try:
            # KNAPPER
            # if komponenter.takeoff_land.value() == 1:
            #     send_command(Tello.takeoff())
            #     print("takeoff")
            #     sleep(2)
            # # TILFØJ FUNKTIONALITET SÅ KNAPPEN OGSÅ GÆLDER SOM LAND

            # X AKSE - JOY1
            print("JS1 <X>: > ", komponenter.joystick1_x())
            print("JS1 <Y>: ", komponenter.joystick1_y())
            if komponenter.joystick1_x() >= 63000:
                print("Joy1 Button Pressed")
                utime.sleep(1)

            elif 40000 <= komponenter.joystick1_x() < 63000:
                print("Right")
                utime.sleep(1)

            elif 18000 <= komponenter.joystick1_x() < 40000:
                print("Deadzone")
                utime.sleep(1)
                pass

            elif komponenter.joystick1_x() <= 18000:
                print("Left")
                utime.sleep(1)

            # X AKSE - JOY2
            if komponenter.joystick2_x() >= 63000:
                print("Joy2 Button Pressed")
                utime.sleep(1)

            elif 40000 <= komponenter.joystick2_x() < 63000:
                print("Right")
                utime.sleep(1)

            elif komponenter.joystick2_x() <= 18000:
                print("Left")
                utime.sleep(1)

            # Y AKSE - JOY1
            if komponenter.joystick1_y() >= 40000:
                print("Op")
                utime.sleep(1)

            elif 18000 <= komponenter.joystick1_y() < 40000:
                print("Deadzone")
                utime.sleep(1)
                pass

            elif komponenter.joystick1_y() <= 18000:
                print("Ned")
                utime.sleep(1)

            # Y AKSE - JOY2
            if komponenter.joystick2_y() >= 40000:
                print("Op")
                utime.sleep(1)

            elif komponenter.joystick2_y() <= 18000:
                print("Ned")
                utime.sleep(1)

        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break


send_command()
