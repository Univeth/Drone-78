import utime


class LcdApi:
    # LCD commands
    LCD_CLR = 0x01  # DB0: clear display
    LCD_HOME = 0x02  # DB1: return to home position
    LCD_ENTRY_MODE = 0x04  # DB2: set entry mode
    LCD_ENTRY_INC = 0x02  # DB1: increment
    LCD_ENTRY_SHIFT = 0x01  # DB0: shift
    LCD_ON_CTRL = 0x08  # DB3: turn lcd/cursor on
    LCD_ON_DISPLAY = 0x04  # DB2: turn display on
    LCD_ON_CURSOR = 0x02  # DB1: turn cursor on
    LCD_ON_BLINK = 0x01  # DB0: blinking cursor
    LCD_MOVE = 0x10  # DB4: move cursor/display
    LCD_MOVE_DISP = 0x08  # DB3: move display (0-> move cursor)
    LCD_MOVE_RIGHT = 0x04  # DB2: move right (0-> left)
    LCD_FUNCTION = 0x20  # DB5: function set
    LCD_FUNCTION_8BIT = 0x10  # DB4: set 8BIT mode (0->4BIT mode)
    LCD_FUNCTION_2LINES = 0x08  # DB3: two lines (0->one line)
    LCD_FUNCTION_10DOTS = 0x04  # DB2: 5x10 font (0->5x7 font)
    LCD_FUNCTION_RESET = 0x30  # See "Initializing by Instruction" section
    LCD_CGRAM = 0x40  # DB6: set CG RAM address
    LCD_DDRAM = 0x80  # DB7: set DD RAM address

    LCD_RS_CMD = 0
    LCD_RS_DATA = 1

    LCD_RW_WRITE = 0
    LCD_RW_READ = 1

    def put_cursor(self, line, pos):
        if line == 0:
            # Line 1 starts at address 0x00
            address = pos
        elif line == 1:
            # Try different addresses for the start of the second line
            for start_address in [0x08, 0x10, 0x20, 0x40, 0x60, 0x80, 0xA0, 0xC0, 0xE0]:
                address = start_address + pos
                self.hal_write_command(self.LCD_DDRAM | address)
                self.write(" ")
                self.hal_write_command(self.LCD_DDRAM | address)
        else:
            raise ValueError("Line number must be 0 or 1")

    def set_cursor_to_second_line(self):
        self.hal_write_command(
            0xC0
        )  # Change this to 0x40 if your display starts the second line at 0x40

    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.cur_line = 0

    def clear(self):
        """Clears the LCD display and moves the cursor to the top left corner."""
        self.hal_write_command(self.LCD_CLR)
        self.hal_sleep_us(2000)  # Spec says > 1.52ms

    def write(self, string):
        for char in string:
            self.hal_write_data(ord(char))

    def hal_sleep_us(self, usecs):
        utime.sleep_us(usecs)

    def hal_write_command(self, cmd):
        raise NotImplementedError

    def hal_write_data(self, data):
        raise NotImplementedError
