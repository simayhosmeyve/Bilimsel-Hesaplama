#EULER SAYISI HESAPLAMA
#Math kütüphanesi kullanarak
from math import factorial
n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += 1/factorial(n)
    n += 1
print(e)


#Decimal modülü kullanarak
from decimal import *
getcontext().prec = 17
#17 basamağa kadar hassasiyet belirledik
n,e,e1 = 0,1,0
while(e!=e1):
    e = e1
    e1 += Decimal(1/factorial(n))
    n += 1
print(e)