# Imports go at the top
from microbit import *

n = '00900:09990:90909:00900:00900'
ne = '00999:00099:00909:09000:90000'
s = '00900:00900:90909:09990:00900'
se = '90000:09000:00909:00099:00999'
w = '00900:09000:99999:09000:00900'
sw = '00009:00090:90900:99000:99900'
e = '00900:00090:99999:00090:00900'
nw = '99900:99000:90900:00090:00009'
dirs = [n,ne,e,se,s,sw,w,nw]
while True:
    x = compass.heading()
    i = round(abs(x)/45)
    if i == 8:
        i = 0
    display.show(Image(dirs[i]))

