import socket
import network
from time import sleep
import _thread
from machine import Pin
from tello import Tello_Commands
import komponenter


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

    Tello = Tello_Commands()

    # SEND COMMANDS
    def send_command(command):
        command = command.encode("utf-8")
        sent = sock.sendto(command, tello_address)


    send_command(Tello.command())
    sleep(1)

    while True:
        try:
            # KNAPPER
            if komponenter.takeoff_land.value() == 1:
                send_command(Tello.takeoff())
                print("takeoff")
                sleep(2)
                # TILFØJ FUNKTIONALITET SÅ KNAPPEN OGSÅ GÆLDER SOM LAND

            
            # X AKSE - JOY1
            if komponenter.joystick1_x() >= 60000:
                print("Joy1 Button Pressed")
            
            elif komponenter.joystick1_x() >= 40000:
                print("Højre")
            
            elif komponenter.joystick1_x() <= 25000:
                print("Venstre")
            
            # X AKSE - JOY2
            if komponenter.joystick2_x() >= 60000:
                print("Joy2 Button Pressed")
            
            elif komponenter.joystick2_x() >= 40000:
                print("Højre")
            
            elif komponenter.joystick2_x() <= 25000:
                print("Venstre")
           
           
            # Y AKSE - JOY1
            if komponenter.joystick1_y() >= 40000:
                print("Op")
                
            elif komponenter.joystick1_y() <= 25000:
                print("Ned")
            
            # Y AKSE - JOY1
            if komponenter.joystick2_y() >= 40000:
                print("Op")
                
            elif komponenter.joystick2_y() <= 25000:
                print("Ned")
            
            
        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break


send_command()
