#NEWTON RAPHSON İLE KAREKÖK HESAPLAMA

def f(x):
    return(x**2-a) 
#x**2=a eşitliğinden a sayısının karekökü hesaplanır

def fi(x):
    return(2*x)
    
x2,t=0,1
def hata(x1,x2):
    return((x1-x2)/x1)

x1 = int(input("Bir başlangıç değeri girin: "))
a = int(input("Karekökünün alınmasını istediğiniz sayı:"))

if(a>=0):
    while(abs(hata(t,x2))> 0.0001):  
      x2 = x1 - f(x1)/fi(x1)  
      print(x1, x2, hata(x2,x1))
      t=x1
      x1=x2
      
else:
    print("Karekök için sıfırdan büyük bir sayı giriniz")