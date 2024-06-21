from microbit import *

countdown = 5
stop = True

display.show(countdown)
while True:
    if not stop:
        for i in range(countdown):
            display.show(countdown-i)
            sleep(1000)
        while True:
            display.show(Image.CHESSBOARD)
            sleep(150)
            display.show(Image.CHESSBOARD.invert())
            sleep(150)
            if button_a.was_pressed() or button_b.was_pressed():
                stop = True
                display.show(countdown)
                break
    if button_a.was_pressed():
        stop = False
    if button_b.was_pressed():
        countdown = (countdown + 1) % 10 + countdown//9
        display.show(countdown)
        
            
        
