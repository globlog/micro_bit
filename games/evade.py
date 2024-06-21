from time import sleep
from microbit import *
from random import randint,choice,random

class player():
    def __init__(self):
        self.x = 2
        self.y = 4
    def move(self, sleft):
        self.clear()
        if left:
            self.x = max(self.x-1,0)
        else:
            self.x = min(self.x+1,4)
        self.add()
    def clear(self):
        display.set_pixel(self.x,self.y,0)
    def add(self):
        display.set_pixel(self.x,self.y,9)
        
class hazard():
    def __init__(self,x):
        self.x = x
        self.y = -1
    def move(self):
        self.clear()
        self.y = (self.y + 1) if self.y < 4 else -1
        self.add()
    def clear(self):
        if 0 <= self.y < 5:
            display.set_pixel(self.x,self.y,0)
    def add(self):
        if 0 <= self.y < 5:
            display.set_pixel(self.x,self.y,6)
        
        
def check_lost(you, hazards):
    for hazard in hazards:
        if hazard.y == you.y and hazard.x == you.x:
            return True
    return False

score = 0

hazards = [hazard(x) for x in range(5)]

you = player()
you.add()

lost = False
points = 0
play = True
while True:
    while play and not lost:
        if button_a.was_pressed():
            you.move(True)
        if button_b.was_pressed():
            you.move(False)
        sleep(40)
        t = random()
        if t > 0.7:
            index = randint(0,4)
            hazards[index].move()
        lost = check_lost(you, hazards)
        points += 1

    if lost:
        display.scroll(points//100)
        play = False
        lost = False
        hazards = [hazard(x) for x in range(5)]
        you = player()
        
    if button_a.was_pressed():
        play = True
        you.add()