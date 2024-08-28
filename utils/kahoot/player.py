from microbit import *
from random import randint
import radio

radio.config(group=137)
radio.on()

'''
    The protocol of a message is simply:
    sender:receiver:text
'''

id = str(randint(1000000,9999999))

choice = 0
new_question = True

while True:
    message = radio.receive()
    if message:
        sender, receiver, text = message.split(':')
        if sender == 'HOST':
            if text in ['1','2','3','4']:
                if text == str(choice):
                    display.show(Image.HAPPY)
                else:
                    display.show(Image.SAD)
            elif text != '0':
                display.scroll(text)
            new_question = True
                
    if button_a.is_pressed():
        if new_question:
            choice = 0
            new_question = False
        choice = choice % 4 + 1
        display.show(choice)
        sleep(300)

    if button_b.is_pressed():
        radio.send(id + ':' + 'HOST' + ':' + str(choice))
        