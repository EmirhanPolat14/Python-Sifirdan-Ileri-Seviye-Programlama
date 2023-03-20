import random
import time


class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal



    def tv_ac(self):

        if self.tv_durum == "Açık":
            print("Televizyon zaten açık...")

        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = "Açık"
    def tv_kapat(self):

        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı...")

        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):
        print("Ses Ayarlamak için '+' ve '-' işaretlerini kullanınız...")
        ses_aç = input("Ses Aç veya Kapat:")
        if ses_aç == "+":
            self.tv_ses += 1

        elif ses_aç == "-":
            if self.tv_ses == 0:
                print("Televizyon Sesi Kısık")
            else:
                self.tv_ses -= 1
    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi....")
    def rastgele_kanal(self):
        rastgele = random.randint(len(self.kanal_listesi) - 1)

        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki kanal:", self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki Kanal: {}".format(self.tv_durum, self.tv_ses,
                                                                                        self.kanal_listesi, self.kanal)
    def sosyal(self):
        print("""
        Platform Listesi:
        0. Çıkış Yapmak
        1. Youtube
        2. Netflix
        3. Blu TV
        4. Amazon Prime
        5. TOD
        6. Disney+
        
        """)
        platformlar = ["Youtube","Netflix","Blu TV","Amazon Prime","TOD","Disney+"]
        while True:
            platform_kodu = input("Platform Kodunu Giriniz:")
            if platform_kodu == "1":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'a Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break
            elif platform_kodu == "2":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'e Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break
            elif platform_kodu == "3":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'ye Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break
            elif platform_kodu == "4":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'a Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break
            elif platform_kodu == "5":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'a Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break

            elif platform_kodu == "6":
                print("Giriş yapılıyor lütfen bekleyiniz...")
                time.sleep(2)
                print("{}'a Hoşgeldiniz!".format(platformlar[int(platform_kodu) - 1]))
                break






kumanda = Kumanda()

print("""

Televizyon Uygulaması

1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

8. Dijital Platformlar


Çıkmak için "0"a basın.
""")

while True:
    işlem = input("İşlem Seçiniz:")

    if işlem == "0":
        print("Çıkış Yapılıyor....")
        break
    elif işlem == "1":
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile parçalayarak girin:")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem == "5":

        print("Kanal Sayısı", len(kumanda))
    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    elif işlem == "8":
        kumanda.sosyal()
        break
    else:
        print("Geçersiz işlem....")
