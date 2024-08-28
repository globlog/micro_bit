from microbit import *

start = False

chessboards = [Image.CHESSBOARD,Image.CHESSBOARD.invert()]

while True:
    if button_a.was_pressed():
        if not start:
            start = not start
            t0 = running_time()
            display.show(chessboards)
            
    if button_b.was_pressed():
        display.clear()
        if start:
            start = not start
            t1 = running_time()
            time = t1 - t0
            display.scroll(str(time//1000)+'.'+str(round((time%1000)/10)))
            #display.scroll(str(time//100)+'.'+str(time%100)+'%')





