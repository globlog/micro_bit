from microbit import *
from random import randint

while True:
    if accelerometer.was_gesture('shake'):        
        display.show(randint(1,6))
