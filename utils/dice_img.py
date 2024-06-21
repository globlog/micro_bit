from microbit import *
from random import choice

one     = '00000:00000:00900:00000:00000'
two_1   = '00000:00000:90009:00000:00000'
two_2   = '00900:00000:00000:00000:00900'
three_1 = '00009:00000:00900:00000:90000'
three_2 = '90000:00000:00900:00000:00009'
four    = '90009:00000:00000:00000:90009'
five    = '90009:00000:00900:00000:90009'
six_1   = '90909:00000:00000:00000:90909'
six_2   = '90009:00000:90009:00000:90009'

sides = [one,one,two_1,two_2,three_1,three_2,four,four,five,five,six_1,six_2]
while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image(choice(sides)))
