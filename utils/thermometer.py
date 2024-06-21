from microbit import *

cels = True
while True:
    celsius = temperature()
    if button_a.is_pressed() or button_b.is_pressed():
        cels = not cels
    if cels:
        display.scroll(celsius)
    else:
        fahrenheit = 9 * celsius // 5 + 32
        display.scroll(fahrenheit)