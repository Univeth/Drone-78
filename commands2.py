import socket
import network
import time
import _thread
from machine import Pin


def commands2():
    host = ""
    port = 9000
    locaddr = (host, port)

    # Tilkobler til dronens netværk
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("TELLO-E9C6E8", "")
    while not wlan.isconnected():
        time.sleep(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    tello_address = ("192.168.10.1", 8889)

    sock.bind(locaddr)

    # Threading for at få besked tilbage fra Drone
    def recv():
        while True:
            try:
                data, addr = sock.recvfrom(1518)
                print(data.decode("utf-8"))
            except KeyboardInterrupt:
                print("\nExit . . .\n")
                break

    print("\r\n\r\nPress button ->\r\n")

    recv_thread = _thread.start_new_thread(recv, ())

    takeoff_pin = Pin(16, mode=Pin.IN, pull=Pin.PULL_DOWN)
    land_pin = Pin(17, mode=Pin.IN, pull=Pin.PULL_DOWN)

    # Funktion for at sende kommandoer til Tello drone
    def send_command(command):
        command = command.encode("utf-8")
        sent = sock.sendto(command, tello_address)

    send_command("command")
    time.sleep(1)

    while True:
        try:
            
            if takeoff_pin.value() == 1:
                send_command("takeoff")
                print("takeoff")
                time.sleep(2)

            if land_pin.value() == 1:
                send_command("land")
                print("land")
                time.sleep(2)

        except KeyboardInterrupt:
            print("\n . . .\n")
            sock.close()
            break

commands2()
