# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    x_strength, y_strength, z_strength = accelerometer.get_values()
    for x in range(5):
        for y in range(5):
            col = 4
            if x > 2:
                if x_strength > 0:
                    col += 2
                else:
                    col -= 2
            elif x < 2:
                if x_strength > 0:
                    col -= 2
                else:
                    col += 2
            if y > 2:
                if y_strength > 0:
                    col += 2
                else:
                    col -= 2
            elif y < 2:
                if y_strength > 0:
                    col -= 2
                else:
                    col += 2
            display.set_pixel(x,y,col)
    