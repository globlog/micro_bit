from microbit import *
import time

def get_time(seconds):
    return (seconds // 3600) % 24, (seconds // 60) % 60, seconds % 60

def bin_row(number,strength,rows):
    b_r = ''
    for i in range(5*rows):
        if i == 5:
            b_r = ':' + b_r
        b_r = (str(strength) if number % 2 else '0') + b_r
        number //= 2
        
    return b_r

play = False
seconds = 0
while True:
    if button_a.was_pressed():
        play = not play
    if button_b.was_pressed():
        seconds = 0
    while play:
        h,m,s = get_time(seconds)
        image = bin_row(h,9,1)+':'+bin_row(m,6,2)+':'+bin_row(s,3,2)+':'
        display.show(Image(image))
        time.sleep(1)
        seconds += 1