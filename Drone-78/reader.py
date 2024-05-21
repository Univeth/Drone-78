import machine
from machine import Pin
import utime


# KNAPPER

takeoff_land = Pin(1, mode=Pin.IN, pull=Pin.PULL_DOWN)


# JOYSTICKS

A = machine.Pin(18, machine.Pin.OUT)
B = machine.Pin(17, machine.Pin.OUT)
C = machine.Pin(16, machine.Pin.OUT)

adc = machine.ADC(machine.Pin(27))


def joystick1_x():
    A.value(1)
    B.value(1)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()


def joystick1_y():
    A.value(0)
    B.value(0)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()


def joystick2_y():
    A.value(1)
    B.value(0)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()


def joystick2_x():
    A.value(0)
    B.value(1)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()
