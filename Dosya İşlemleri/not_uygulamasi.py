def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    
    ad_soyad = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >=90:
        harf = "AA"
    elif ortalama <= 89 and ortalama >= 85:
        harf = "BA" 
    elif ortalama <= 84 and ortalama >= 80:
        harf = "BB"
    elif ortalama <= 79 and ortalama >= 75:
        harf = "CB"
    elif ortalama <= 74 and ortalama >= 70:
        harf = "CC" 
    elif ortalama <= 69 and ortalama >= 65:
        harf = "DC"
    elif ortalama <= 64 and ortalama >= 60:
        harf = "DD"
    elif ortalama <= 59 and ortalama >= 50:
        harf = "FD"
    else:
        harf = "FF"
    
    return f"{ad_soyad}: {harf}\n"
def ortalamalari_oku():
    with open("sinav_notlari.txt","r+",encoding="utf-8") as file:
        for satir in file:

            print(not_hesapla(satir))

def not_gir():
    ad = input("Öğrenci adı:")
    soyad = input("Öğrenci soyadı:")
    not1 = input("not1:")
    not2 = input("not2:")
    not3 = input("not3:")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3+'\n')

def not_kayit():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))
    
    with open("sonuclar.txt","w",encoding="utf-8") as file2:
        for i in liste:

            file2.write(i)

while True:
    islem = int(input("1-Notları Oku\n2-Not Gir\n3-Notları Kaydet\n4-Çıkış Yap\n"))

    if islem == 1:
        ortalamalari_oku()
    elif islem == 2:
        not_gir()
    elif islem == 3:
        not_kayit()
    else:
        break