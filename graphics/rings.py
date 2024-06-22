from microbit import *

def ring(size):
    if size == 1:
        return '00000:00000:00900:00000:00000'
    elif size == 2: 
        return '00000:09990:09090:09990:00000'
    elif size == 3:
        return '99999:90009:90009:90009:99999'
    else:
        return '00000:00000:00000:00000:00000:00000'

size = 0
while True:
    display.show(Image(ring(size)))
    sleep(200)
    size = (size + 1)%4
        