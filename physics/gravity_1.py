# Imports go at the top
from microbit import *

current_x = 2
current_y = 2
display.set_pixel(current_x,current_y,9)
# Code in a 'while True:' loop repeats forever
while True:
    old_x,old_y = current_x,current_y
    direction = accelerometer.current_gesture()
    if direction == 'left':
        current_x = max(current_x-1,0)
    elif direction == 'right':
        current_x = min(current_x+1,4)
    elif direction == 'up':
        current_y = max(current_y-1,0)
    elif direction == 'down':
        current_y = min(current_y+1,4)
    if (old_x,old_y) != (current_x,current_y):
        display.set_pixel(old_x,old_y,0)
        display.set_pixel(current_x,current_y,9)
        sleep(200)