# Button changes color of LED 
# Rainbow when pushed
# Otherwise cycles green yellow orange red (not smooth)


import time
import board
from rainbowio import colorwheel
import neopixel
from digitalio import DigitalInOut, Direction, Pull

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
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
led.brightness = 0.03
led[0] = PURPLE

# Set up button
button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Set up light
num_pix = 48
pixels = neopixel.NeoPixel(board.A0, num_pix, brightness=0.01, auto_write=False)

print("HELLO!")


# Cycle colors while button is pushed
def button_is_pushed():
    global button 
    global led 

    i = 1
    COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE, CYAN, PURPLE]
    while button.value:
        led[0] = COLORS[i] 
        i += 1
        i = i % len(COLORS)
        time.sleep(.1)
      

def get_color_for_timer_count(i):
    if i > 30:
        return RED
    if i > 20:
        return ORANGE
    if i > 10:
        return YELLOW
    return GREEN
    

def main():
    global button 
    global led 
    global pixels 

    button_prev = button.value
    timer_value = 0
    while True:
        #Only update light if value changes
        if button_prev != button.value:
            if button.value:  
                print("Pushed!")
                pixels[0] = CYAN
                pixels[2] = CYAN
                pixels.show()
                button_is_pushed()
                timer_value = 0
            else:
                print("Released!")
                pixels[0] = PURPLE
                pixels[2] = PURPLE
                pixels.show()
            button_prev = not button_prev

        timer_value += 1
        led[0] = get_color_for_timer_count(timer_value)

        time.sleep(.1)


main()
