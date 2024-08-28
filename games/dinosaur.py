# Imports go at the top
from microbit import *
from random import randint

speed = 150

class player():
    def __init__(self):
        self.base = 4
        self.height = 2
        self.jumping_frames = [1,2,2,2,2,2,2,2,1,0]
        self.ducking_frames = [1,1,1,1,1,1,2]
        self.jumping = len(self.jumping_frames)
        self.ducking = len(self.ducking_frames)
        self.display()

    def move(self):
        if 0 <= self.jumping < len(self.jumping_frames):
            self.jump()
        if 0 <= self.ducking < len(self.ducking_frames):
            self.duck()
    def jump(self):
        self.display(False)
        self.ducking = len(self.ducking_frames)
        j = self.jumping_frames[self.jumping]
        self.base = 4-j
        self.display()
        self.jumping += 1
            
    def duck(self):
        self.display(False)
        self.jumping = len(self.jumping_frames)
        j = self.ducking_frames[self.ducking]
        self.height = j
        self.display()
        self.ducking += 1

    def display(self,show = True):
        for i in range(self.height):
            display.set_pixel(0, self.base - i, 9 if show else 0)
        

    
user = player()
run_every(user.move,ms=speed)

class obstacle():
    def __init__(self):
        self.y = [2,3] if randint(0,1) == 0 else [3,4]
        self.x = 4
        self.display()
        self.t = 0
    def move(self):
        self.display(False)
        self.t += 1
        if self.t % 3 == 0:
            self.x -= 1
        if self.x < 0:
            self.__init__()
        else:
            self.display()
                    
    def display(self,show = True):
        for coord in self.y:
            display.set_pixel(self.x, coord, 9 if show else 0)


obs = obstacle()

run_every(obs.move,ms=speed)

class game():
    def __init__(self, user, object):
        self.user = user
        self.object = object
        self.points = 0
    def check_collision(self):
        if self.object.x == 0:
            if (self.object.y == [2,3] and 0 <= self.user.ducking < len(self.user.ducking_frames)) or (self.object.y == [3,4] and 0 <= self.user.jumping < len(self.user.jumping_frames)):
                self.points += 1
            else:
                display.scroll(self.points)
                sleep(3000)
        elif self.object.x == 4:
            self.user.display()
                
gamer = game(user,obs)

# Code in a 'while True:' loop repeats forever

while True:
    if button_a.is_pressed():
        user.jumping = 0
    if button_b.is_pressed():
        user.ducking = 0
    gamer.check_collision()
        
