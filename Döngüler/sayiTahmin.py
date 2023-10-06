'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''
import random
hak = int(input("Kaç hak istiyorsanız rakam ile yazınız."))
puan = 100
sayi = random.randint(1,100)


i = 0
while i < hak:
    tahmin = int(input("1-100 arası bir tahmin yapınız:"))
    if tahmin < sayi:
        print("yukarı")
        puan = puan - int(100/hak) 
    elif tahmin > sayi:
        print("aşağı")
        puan = puan - int(100/hak)
    else:
        print(f"Doğru Tahmin! \nPuanınız:{puan}")
        break
    i += 1

if puan == 0:
    print("Maalesef hakkınız doldu :(")

        
