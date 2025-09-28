# Button that changes onboard LED and any attached neopixels

import time
import board
from rainbowio import colorwheel
import neopixel
from digitalio import DigitalInOut, Direction, Pull

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# onboard dotstar only
import adafruit_dotstar
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.01
led[0] = PURPLE

# Set up button
button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Set up light
num_pix = 48
pixels = neopixel.NeoPixel(board.A0, num_pix, brightness=0.01, auto_write=False)

print("HELLO!")

button_prev = button.value
while True:
    #Only update light if value changes
    if button_prev != button.value:
        if button.value:  
            print("Pushed!")
            led[0] = CYAN
            pixels[0] = CYAN
            pixels[2] = CYAN
            pixels.show()
        else:
            print("Released!")
            led[0] = PURPLE
            pixels[0] = PURPLE
            pixels[2] = PURPLE
            pixels.show()
        button_prev = not button_prev
    time.sleep(.1)
