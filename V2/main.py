from mpmath import *
mp.dps = 100; mp.pretty = True
x = fadd(1, 2)
with open('main.txt', 'w') as txt:
    txt.write(x)
with open('main.csv', 'w') as csv:
    y = ()
    z = 1
    csv.write('Number, Value')
    for num in str(x):
        if num = '.':
            csv.write(f'Decimal, {num}')
        else:
            csv.write(f'{z},{num}')
        csv.flush()
        z+=1
