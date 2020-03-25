#Pİ SAYISI HESAPLAMA

from decimal import *
getcontext().prec =20

def pi():
    n,p,p1 = 1,1,0
    while (abs(p1-p) > 0.0001):
     p=p1
     p1 += Decimal((4/(2*n-1))*((-1)**(n+1)))
     n+=1
    return p
    
p=pi()    
print(p)