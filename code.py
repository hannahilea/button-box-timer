# Timer - Cycles through Green -> Yellow -> Red LEDs
# Resets when button is pushed

import time
import board
from digitalio import DigitalInOut, Direction, Pull

THRESHOLD_YELLOW_SEC = 30 * 60 
RED_THRESHOLD_SEC = 60 * 60
LOOP_DELAY_SEC = 0.1

# Set up button
button = DigitalInOut(board.D3)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Set up leds
led_green = DigitalInOut(board.D0)
led_green.direction = Direction.OUTPUT
led_green.value = True

led_yellow = DigitalInOut(board.D1)
led_yellow.direction = Direction.OUTPUT
led_yellow.value = True

led_red = DigitalInOut(board.D2)
led_red.direction = Direction.OUTPUT
led_red.value = True

print("HELLO!")


# Cycle colors while button is pushed
def button_is_pushed():
    global button
    global led_red, led_yellow, led_green
    i = True
    while not button.value:  # Button value is False when pushed, due to wiring
        for led in [led_red, led_yellow, led_green]:
            led.value = i
            led_yellow.value = i
        i = not i
        time.sleep(LOOP_DELAY_SEC)


def update_leds_for_timer(i):
    global led_red, led_yellow, led_green
    if i > RED_THRESHOLD_SEC / LOOP_DELAY_SEC:
        # print("Red!")
        led_green.value = False
        led_yellow.value = False
        led_red.value = True
    elif i > THRESHOLD_YELLOW_SEC / LOOP_DELAY_SEC:
        # print("Yellow!")
        led_green.value = False
        led_yellow.value = True
        led_red.value = False
    else:
        # print("Green!")
        led_green.value = True
        led_yellow.value = False
        led_red.value = False


def main():
    global button
    button_prev = button.value
    timer_value = 0
    while True:
        if button_prev != button.value:
            # Time to reset things!
            if not button.value:
                # print("Pushed!")
                button_is_pushed()
                timer_value = 0
            else:
                # print("Released!")
                pass
            button_prev = not button_prev
        timer_value += 1
        update_leds_for_timer(timer_value)
        time.sleep(LOOP_DELAY_SEC)


main()
