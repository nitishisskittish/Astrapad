import board
import busio
import digitalio
import time
import adafruit_ssd1306
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

pixels = neopixel.NeoPixel(board.D7, 17, brightness=1, auto_write=False)
colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 0, 255), # Magenta
    (0, 255, 255)  # Cyan
]

def get_current_color(color_idx):
    colors_names = ["Red", "Green", "Blue", "Yellow", "Pink", "Cyan"]
    return colors_names[color_idx % 6]

color_idx = 0

pin_a = digitalio.DigitalInOut(board.D9)
pin_a.pull = digitalio.Pull.UP
pin_b = digitalio.DigitalInOut(board.D3)
pin_b.pull = digitalio.Pull.UP

col1 = digitalio.DigitalInOut(board.D0)
col1.direction = digitalio.Direction.OUTPUT
col1.value = False

row1 = digitalio.DigitalInOut(board.D6) # Button 1
row1.pull = digitalio.Pull.UP

row2 = digitalio.DigitalInOut(board.D8)
row2.pull = digitalio.Pull.UP

kbd = Keyboard(usb_hid.devices)
i2c = busio.I2C(board.D5, board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

count = 0
last_a = pin_a.value

def update_display(msg, val):
    oled.fill(0)
    oled.text("ASTRAPAD", 0, 0, 1)
    oled.text("ACT:" + msg[:28], 0, 10, 1)
    oled.text("VAL:" + str(val), 0, 20, 1)
    oled.show()

pixels.fill(colors[color_idx])
pixels.show()
update_display("SYSTEM READY", count)

while True:
    cur_a = pin_a.value
    if cur_a != last_a:
        if pin_b.value != cur_a:
            count += 1
        else:
            count -= 1

        print(f"Count: {count}")
        update_display("SCROLLING", count)
        update_display("READY", count)
    last_a = cur_a

    if not row1.value:
        kbd.press(Keycode.SPACE)
        update_display("SPACE BAR", 0)
        kbd.release(Keycode.SPACE)
        time.sleep(0.15)
        update_display("READY", 0)

    if not row2.value:
        color_idx = (color_idx + 1) % len(colors)
        pixels.fill(colors[color_idx])
        pixels.show()
        update_display("COLOR CHANGED", get_current_color(color_idx))
        time.sleep(0.15)
        update_display("READY", count)
