from mpmath import *
import csv
mp.dps = 100; mp.pretty = True
x = mpf(426880)*sqrt(10005)*(nsum(lambda q: ((mpf(-1))^(q)*fac((mpf(6)*q))*(mpf(545140134*q+13591409)))/((fac(mpf(3*q)))*(fac(q)^(mpf(3)))*(mpf(-262537412640768000))^(q)), [0, inf]))^mpf(-1)
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))