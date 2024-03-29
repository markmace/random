# slow_program.py
from decimal import *

def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    
    while s!= lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -=2
    return +s

print(exp(Decimal(150)))
print(exp(Decimal(400)))
print(exp(Decimal(3000)))
