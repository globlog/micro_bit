# Imports go at the top
from microbit import *
from random import randint

cards = {10 : 'T', 11 : 'J', 12 : 'Q', 13 : 'K', 14 : 'A'}

lives = 4
points = 0
        
# Code in a 'while True:' loop repeats forever
currentcard = randint(2,14)
while lives > 0:
    if currentcard not in cards:
        display.show(currentcard)
    else:
        display.show(cards[currentcard])
    nextcard = randint(2,14)
    while True:
        if button_a.is_pressed():
            if nextcard >= currentcard:
                points += 1
                display.show(Image.YES)
            else:
                lives -= 1
                display.show(Image.NO)
            sleep(500)
            currentcard = nextcard 
            break
        if button_b.is_pressed():
            if nextcard <= currentcard:
                points += 1
                display.show(Image.YES)
            else:
                lives -= 1
                display.show(Image.NO)
            sleep(500)
            currentcard = nextcard 
            break

display.scroll(points)