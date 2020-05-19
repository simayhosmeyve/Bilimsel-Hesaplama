#HATALI POZİTİF
"""Test bütün pozitifleri yakalar ama bazen negatifler de 
pozitif gösterilebilir"""
#HATALI NEGATİF 
"""Test bütün negatifleri yakalar ama bazen pozitifler de
negatif gösterilebilir"""

secim = int(input("Hesaplanacak dogrulugu seciniz: Hatalı pozitif icin(1),Hatalı negatif için(0)"))
toplum_kisi = int(input("Toplumdaki kisi sayısı:"))
sıklık = int(input("Hastalıgın görülme sıklıgı: (Kac kiside bir?))"))
test_dogruluk = int(input("Test sonucu yüzdelik dogrulugu:"))

while(test_dogruluk>100 or test_dogruluk<0):
    print("Gecerli bir yüzdelik giriniz")
    test_dogruluk = int(input("Test sonucu yüzdelik dogrulugu:"))

while(secim == 1):
    kesin_ihtimal = toplum_kisi/sıklık
    olası_ihtimal = ((toplum_kisi-kesin_ihtimal)*(100-test_dogruluk))/100
    olasılık = float(kesin_ihtimal/(kesin_ihtimal+olası_ihtimal))
    print("Test pozitifse hasta olma olasılıgı:" + str(olasılık))
    break

while(secim == 0):
    kesin_ihtimal = toplum_kisi-(toplum_kisi/sıklık)
    olası_ihtimal = ((toplum_kisi-kesin_ihtimal)*(100-test_dogruluk))/100
    olasılık = float(olası_ihtimal/(kesin_ihtimal+olası_ihtimal))
    print("Test pozitifse hasta olma olasılıgı:" + str(olasılık))
    break