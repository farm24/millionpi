from mpmath import *
import csv
mp.dps = 100000; mp.pretty = True
x = mpf(1)/mpf(3)
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))