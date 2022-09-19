from mpmath import *
import csv
mp.dps = 100; mp.pretty = True
x = (mpf(426880)*sqrt(10005))*(nsum(lambda q: ((fac((mpf(6)*q)*(mpf(545140134)*q+mpf(13591409))) )/(fac(mpf(3)*q)*(fac(q)**(3)*(-262537412640768000)**(q))) ), [0, inf]))**(mpf(-1))
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))9