from pico_parallel_lcd import GpioLcd
import utime

# Define GPIO pins for LCD
RS = 0
E = 1
D4 = 2
D5 = 3
D6 = 4
D7 = 5

# Initialize the LCD
lcd = GpioLcd(
    rs_pin=RS,
    enable_pin=E,
    d4_pin=D4,
    d5_pin=D5,
    d6_pin=D6,
    d7_pin=D7,
    num_lines=2,
    num_columns=8,
)

# Clear the LCD
lcd.clear()


def message(battery, mode):
    # Clear Screen
    lcd.clear()
    # Display a message
    lcd.write(battery)
    utime.sleep(0.1)
    lcd.set_cursor_to_second_line()
    utime.sleep(0.1)
    lcd.write(mode)
