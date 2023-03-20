import random
import time

class bilgisayar():
    def __init__(self,marka,model,ram,işlemci,ekran_kartı,fiyat,depolama):
        self.marka = marka
        self.model = model
        self.ram = ram
        self.işlemci = işlemci
        self.ekran_kartı = ekran_kartı
        self.fiyat = fiyat
        self.depolama = depolama

    def __str__(self):
        return "Marka: {}\nModel: {}\nRam: {}\nİşlemci: {}\n Ekran Kartı: {}\nFiyat: {}".format(self.marka,self.model,self.ram,self.işlemci,self.ekran_kartı,self.fiyat)
    def __len__(self):
        print(self.depolama)
        return self.depolama
    def __del__(self):
        print("Bilgisayar siliniyor...")


PC1 = bilgisayar("Lenova","Legion","16 GB","Intel Core i7-9750H",": Geforce GTX1660Ti",19000,512)

print("""

Bilgisayar Uygulaması

1. PC Bilgilerini Göster

2. Depolama 

3. PC'yi Sil


Çıkmak için "0"a basın.
""")

while True:
    işlem = input("İşlem Seçiniz:")

    if işlem == "0":
        print("Çıkış Yapılıyor....")
        break
    elif işlem == "1":
        print(PC1)
    elif işlem == "2":
        len(PC1)
    elif işlem == "3":
        print("PC siliniyor...")
        time.sleep(2)
        print("Silme İşlemi Başarıyla Gerçekleşti!")
        del PC1
        break
    else:
        print("Geçersiz işlem....")


