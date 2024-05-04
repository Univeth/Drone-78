import machine
import utime


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


def joystick2_x():
    A.value(1)
    B.value(0)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()


def joystick2_y():
    A.value(0)
    B.value(1)
    C.value(0)

    utime.sleep_ms(10)

    return adc.read_u16()


while True:
    print("\n")
    print("JS1 <X>: > ", joystick1_x())
    print("JS1 <Y>: ", joystick1_y())
    print("\n")
    print("JS2 <Y>: > ", joystick2_x())
    print("JS2 <X>: > ", joystick2_y())

    utime.sleep(0.8)
