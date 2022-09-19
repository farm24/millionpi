from mpmath import *
import csv
mp.dps = 100; mp.pretty = True
x = mpf()*sqrt()*(nsum(lambda q: (), [0, inf]))**(mpf(-1))
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))