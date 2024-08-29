import serial

with serial.Serial('/dev/cu.usbmodem102', 115200, timeout=1) as ser:
    while True:
    #x = ser.read()          # read one byte
        #line = ser.read(2)        # read up to ten bytes (timeout)
        line = ser.readline()
        print(int(line))