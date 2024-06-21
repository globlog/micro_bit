# Imports go at the top
from microbit import *
from random import randint

pause = False
current_x = 2
current_y = 2
positions = [(current_x,current_y),(current_x,current_y),(current_x,current_y)]
display.set_pixel(current_x,current_y,9)
manual = True
# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        pause = not pause
    if button_b.was_pressed():
        manual = not manual
    if not pause:
        old_x,old_y = positions[0]
        if manual:
            direction = accelerometer.current_gesture()
        else:
            direction = ['left','right','up','down'][randint(0,3)]
        if direction == 'left':
            current_x = max(old_x-1,0)
        elif direction == 'right':
            current_x = min(old_x+1,4)
        elif direction == 'up':
            current_y = min(old_y+1,4)
        elif direction == 'down':
            current_y = max(old_y-1,0)
        if (old_x,old_y) != (current_x,current_y):
            x,y = positions.pop()
            display.set_pixel(x,y,0)
            positions = [(current_x,current_y)]+positions
            for i,position in enumerate(positions[::-1]):
                x,y = position
                display.set_pixel(x,y,3*(i+1))
            sleep(150)