from mpmath import *
import csv
mp.dps = 100000; mp.pretty = True
x = mpf(1)/mpf(3)
with open('main.txt', 'w', newline='') as txt:
    txt.write(str(x))
with open('main.csv', 'w', newline='') as csva:
    csvr = csv.writer(csva)
    y = ()
    z = 1
    csvr.writerow(['Number', 'Value'])
    for num in str(x):
        if num == '.':
            y=['Decimal', '.']
            csvr.writerow(y)
        else:
            y = [z, num]
            csvr.writerow(y)
        z+=1
        y=[]
