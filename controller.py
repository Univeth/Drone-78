import socket
import network
from time import sleep
import utime
import _thread
import reader
import commands


# Laver network connection til dronens netværk.
def setup_network():
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
    return sock, tello_address


# Laver "threading" som gøre man kan modtage og sende UDP packets samtidigt.
def receive_thread(sock):
    def recv():
        while True:
            try:
                data, addr = sock.recvfrom(1518)
                print(data.decode("utf-8"))
            except KeyboardInterrupt:
                print("\nExit . . .\n")
                break

    _thread.start_new_thread(recv, ())


# Sender UDP packets til dronen.
def send_tello_command(sock, tello_address, command):
    command = command.encode("utf-8")
    sent = sock.sendto(command, tello_address)


# Orchestrere og kalder alle funktionerne.
def execute_commands():
    sock, tello_address = setup_network()
    receive_thread(sock)

    send_tello_command(sock, tello_address, commands.command())
    utime.sleep(1)

    print("\nREADY ->")

    while True:
        try:

            js1_x = reader.joystick1_x()
            js1_y = reader.joystick1_y()
            js2_x = reader.joystick2_x()
            js2_y = reader.joystick2_y()

            print("JS1 <X>: > ", reader.joystick1_x())
            print("JS1 <Y>: ", reader.joystick1_y())
            if js1_x >= 63000:
                print("Joy1 Button Pressed")
                send_tello_command(sock, tello_address, commands.takeoff())

            elif 40000 <= js1_x < 63000:
                print("Right")
                send_tello_command(sock, tello_address, commands.move_right(30))

            elif 18000 <= js1_x < 40000:
                print("Deadzone")
                # utime.sleep(0.5)
                pass

            elif js1_x <= 18000:
                print("Left")
                send_tello_command(sock, tello_address, commands.move_left(30))

            # Y AKSE - JOY1
            if js1_y <= 18000:
                print("Op")
                send_tello_command(sock, tello_address, commands.move_forward(30))

            elif 18000 <= js1_y < 40000:
                print("Deadzone")
                pass

            elif js1_y >= 40000:
                print("Ned")
                send_tello_command(sock, tello_address, commands.move_back(30))

            #
            #
            #
            #

            # X AKSE - JOY2
            if js2_x >= 63000:
                print("Joy2 Button Pressed")
                send_tello_command(sock, tello_address, commands.land())

            elif 40000 <= js2_x < 63000:
                print("Right")
                send_tello_command(sock, tello_address, commands.clockwise(40))

            elif js2_x <= 18000:
                print("Left")
                send_tello_command(sock, tello_address, commands.counterclockwise(40))

            # Y AKSE - JOY2
            if js2_y <= 18000:
                print("Op")
                send_tello_command(sock, tello_address, commands.takeoff())

            elif js2_y >= 40000:
                print("Ned")
                send_tello_command(sock, tello_address, commands.land())

            utime.sleep(0.3)

        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break


execute_commands()
