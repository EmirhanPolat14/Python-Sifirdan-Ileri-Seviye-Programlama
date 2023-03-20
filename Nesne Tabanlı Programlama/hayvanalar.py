class Hayvanlar():
    def __init__(self,isim,ayak_sayısı,beslenme,üreme):
        self.isim = isim
        self.ayak_sayısı = ayak_sayısı
        self.beslenme = beslenme
        self.üreme = üreme




class Köpekler(Hayvanlar):
    def __init__(self,isim,ayak_sayısı,beslenme,üreme,cins):
        super().__init__(isim,ayak_sayısı,beslenme,üreme)
        self.cins = cins
    def __str__(self):
        return "Kaç Ayaklı = {}\nBeslenme Şekli = {}\nÜreme Biçimi = {}\nCins = {}".format(self.ayak_sayısı,self.beslenme,self.üreme,self.cins)
    def ses(self):
        print("HAV HAV")
    def evcil(self):
        evcil_mi = input("Köpek Evcil mi?")
        if evcil_mi == "Evet":
            print("Mama,su ver, tuvalete çıkar!")

class Atlar(Hayvanlar):
    def __init__(self,isim, ayak_sayısı, beslenme, üreme, yaş, cinsiyet, hadım_mı):
        super().__init__(isim, ayak_sayısı, beslenme, üreme)
        self.yaş = yaş
        self.cinsiyet = cinsiyet
        self.hadım_mı = hadım_mı
    def __str__(self):
        return "Kaç Ayaklı = {}\nBeslenme Şekli = {}\nÜreme Biçimi = {}\n Yaşı = {} ".format(self.ayak_sayısı,self.beslenme,self.üreme,self.yaş)
    def ad(self):
        if self.yaş < 1:
            print("{} Bir Tay'dır".format(self.isim))
        elif self.yaş == 1 or self.yaş == 2:
            print("{} Bir Genç At'dır".format(self.isim))
        elif self.yaş >= 4:
            if self.hadım_mı == "Hayır" and self.cinsiyet == "Erkek":
                print("{} Bir Aygır'dır".format(self.isim))
            elif self.hadım_mı == "Evet" and self.cinsiyet == "Erkek":
                print("{} Bir İğdiş'dir".format(self.isim))
            elif self.cinsiyet == "Dişi":
                print("{} Bir Kısrak'tır".format(self.isim)),

class Kuşlar(Hayvanlar):
    def __init__(self, isim, ayak_sayısı, beslenme, üreme,cins):
        super().__init__(isim,ayak_sayısı,beslenme,üreme)
        self.cins = cins

    def __str__(self):
        return "Kaç Ayaklı = {}\nBeslenme Şekli = {}\nÜreme Biçimi = {}\n Cinsi = {} ".format(self.ayak_sayısı,
                                                                                             self.beslenme, self.üreme,
                                                                                             self.cins)
    def ses(self):
        print("Cik Cik")

    def uçabilir_mi(self):
        if self.cins == "Penguen" or self.cins == "Tavuk" or self.cins == "Deve Kuşu" or self.cins == "Tavus Kuşu":
            print("Uçma yeteneğini evrimsel olarak kaybetmiştir")
        else:
            print("Büyük ihtimalle uçar...")


Karabaş = Köpekler("Karabaş",4,"Etçil","Memeli","Kangal")
Beyaz_saray = Atlar("Beyaz Saray", 4,"Otçul","Memeli",5,"Erkek","Evet")
Cici_kuş = Kuşlar("Cici Kuş",2,"Otçul","Yumurta","Penguen")


