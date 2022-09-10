from mpmath import *
import csv
mp.dps = 100; mp.pretty = True
x = mpf(426880)*sqrt(10005)*(nsum(lambda q: ((-1)^(q)*fac((6*q))*(545140134*q+13591409))/((fac(3*q))*(fac(q)^(3))*(-262537412640768000)^(q)), [0, inf]))^-1
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))