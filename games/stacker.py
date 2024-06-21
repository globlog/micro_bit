# Imports go at the top
from microbit import *

rows = []
positions = [0,1,2]
dir = True
level = 0
# Code in a 'while True:' loop repeats forever
play = False
while True:
    if button_b.was_pressed():
        play = True
        rows = []
        positions = [0,1,2]
        dir = True
        level = 0
        display.clear()
        
        
    while play:
        if button_a.was_pressed():
            lost = True
            if len(rows) == 3:
                rows.pop(0)
            newrow = [False]*5          
            for position in positions:
                if 0 <= position < 5 :
                    if rows == []:
                        newrow[position] = True
                        lost = False 
                    elif rows[-1][position]:
                        newrow[position] = True                
                        lost = False
            rows += [newrow]
            display.clear()
            for y, single_row in enumerate(rows):
                for x, col in enumerate(single_row):
                    if col:
                        display.set_pixel(x,4-y,9)
                    else:
                        display.set_pixel(x,4-y,0)
            if lost:
                play = False
                sleep(200)
                display.scroll(level)
                break
            else:
                level += 1
                if level == 4:
                    positions = positions[:2]
                elif level == 7:
                    positions = positions[:1]
        #clear row
        for position in range(5):
            display.set_pixel(position,4-len(rows),0)
        for i in range(len(positions)):
            positions[i] += 1 if dir else -1
        for position in positions:
            if 0 <= position < 5:
                display.set_pixel(position,4-len(rows),9)
        if positions[0] == 4 or positions[-1] == 0:
            dir = not dir
        sleep(150 - 20 * (level // 10))