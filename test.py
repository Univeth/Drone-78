from machine import Pin
from time import sleep


def test():

    n = Pin(16, mode=Pin.IN, pull=Pin.PULL_DOWN)
    d = Pin(17, mode=Pin.IN, pull=Pin.PULL_DOWN)

    while True:
        if n.value() == 1:
            n.on()
            print("Takeoff...")

            sleep(0.2)
        else:
            n.off()

        if d.value() == 1:
            d.on()
            print("Landing...")

            sleep(0.2)
        else:
            d.off()
