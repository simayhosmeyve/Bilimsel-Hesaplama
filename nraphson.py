def f(x):
    return x**2-4*x+3  

def df_dx(x):
    return 2*x-4


def benzerlikhesap(f, x1, x2):
    if f(x1) < f(x2):
        x1, x2 = x2, x1
    if f(x1) * f(x2) == 0:
        print('Girdiginiz degerlerden birisi denklem kokudur')
    elif f(x1) * f(x2) > 0:
        print('Girdiginiz aralikta tek kok yoktur')
    else:
        x1_t = x1
        iter = 0
        while True:
            x1 = (f(x1)*x2-f(x2)*x1) / (f(x1)-f(x2))
            iter += 1
            if abs(f(x1)-f(x1_t)) < 0.0001:
                print('Kok : ', x1, 'iterasyon sayisi:',iter)
                return x1, iter
            x1_t = x1

def newtonraphson(f, f_d, x):
    iter = 0
    if f(x) != 0:
        while abs(f(x) / f_d(x)) >= 0.0001:
            iter += 1
            x -= f(x) / f_d(x)
    print('Kok: ', x, 'iterasyon sayisi:',
          iter)

    return x, iter


def main():
    x1 = int(input('x1 degerini giriniz:'))
    x2 = int(input('x2 degerini giriniz:'))
    x3 = int(input('x3 degerini giriniz(2. fonksiyon icin):'))
    
    benzerlikhesap(f, x1, x2)
    newtonraphson(f, df_dx, x3)



main()