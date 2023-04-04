import random
import time


print("""*************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.


************""")


rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz:"))

    if tahmin < rastgele_sayı:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Biraz çık...")
        tahmin_hakkı -= 1
    elif tahmin > rastgele_sayı:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print("Biraz in...")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("!İşte Bildin!",rastgele_sayı)
        break
    if tahmin_hakkı == 0:
        print("Tahmin Hakkın Biti :(")
        print("Doğru Cevap:",rastgele_sayı)
        break




