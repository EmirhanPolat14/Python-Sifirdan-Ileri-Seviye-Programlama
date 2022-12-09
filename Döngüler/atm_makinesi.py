print("""*************************************
Atm Makinesine Hoşgeldiniz

İşlemler;
1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Programdan çıkmak için 'q'ya basınız
*************************************
""")

bakiye = 1000

while True:
   a = input("İşlem Kodunu Giriniz:")

   if a == "q":
       print("Yine Bekleriz")
       break
   elif a == "1":
       print("Bakiyeniz:{}TL ".format(bakiye))
   elif a == "2":
       b = int(input("Yatırılacak Miktar:"))
       bakiye += b
   elif a == "3":
       c = int(input("Çekilecek Miktar:"))
       if c > bakiye:
           print("Yetersiz Bakiye")
           continue
       bakiye -= c
   else:
       print("Hatalı İşlem Seçtiniz...!")

