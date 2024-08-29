def on_forever():
    serial.write_line(str(input.temperature()))
    basic.pause(100)
basic.forever(on_forever)

