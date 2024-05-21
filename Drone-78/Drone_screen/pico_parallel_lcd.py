from machine import Pin
from lcd_api import LcdApi
import utime

class GpioLcd(LcdApi):

    def __init__(self, rs_pin, enable_pin, d4_pin, d5_pin, d6_pin, d7_pin, num_lines, num_columns):
        self.rs = Pin(rs_pin, Pin.OUT)
        self.enable = Pin(enable_pin, Pin.OUT)
        self.d4 = Pin(d4_pin, Pin.OUT)
        self.d5 = Pin(d5_pin, Pin.OUT)
        self.d6 = Pin(d6_pin, Pin.OUT)
        self.d7 = Pin(d7_pin, Pin.OUT)
        
        self.rs.off()
        self.enable.off()
        
        LcdApi.__init__(self, num_lines, num_columns)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_ms(5)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_us(100)
        utime.sleep_ms(10)  # Wait for the LCD to finish initializing

        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        utime.sleep_ms(1)
        self.hal_write_init_nibble(self.LCD_FUNCTION)
        utime.sleep_ms(1)

        self.hal_write_command(self.LCD_FUNCTION | self.LCD_FUNCTION_2LINES)
        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)
        self.hal_write_command(self.LCD_ENTRY_MODE | self.LCD_ENTRY_INC)
        self.hal_write_command(self.LCD_HOME)
        self.hal_write_command(self.LCD_CLR)
        
    def hal_write_init_nibble(self, nibble):
            self.d4.value((nibble >> 4) & 1)
            self.d5.value((nibble >> 5) & 1)
            self.d6.value((nibble >> 6) & 1)
            self.d7.value((nibble >> 7) & 1)
            self.hal_pulse_enable()

    def hal_pulse_enable(self):
        self.enable.on()
        utime.sleep_us(1)
        self.enable.off()
        utime.sleep_us(1)

    def hal_write_command(self, cmd):
        self.rs.off()
        self.hal_write_byte(cmd)
        if cmd <= 3:
            utime.sleep_ms(5)

    def hal_write_data(self, data):
        self.rs.on()
        self.hal_write_byte(data)

    def hal_write_byte(self, data):
        self.d4.value((data >> 4) & 1)
        self.d5.value((data >> 5) & 1)
        self.d6.value((data >> 6) & 1)
        self.d7.value((data >> 7) & 1)
        self.hal_pulse_enable()
        self.d4.value(data & 1)
        self.d5.value((data >> 1) & 1)
        self.d6.value((data >> 2) & 1)
        self.d7.value((data >> 3) & 1)
        self.hal_pulse_enable()
