def not_hesapla(satır):
    satır = satır[:-1]

    liste = satır.split(",")


    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * 3/10 + not2 * 3/10 + not3 * 4/10

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------->" + harf + "\n"

def kaldı_geçti(satır):
    satır = satır[:-3] + "," + satır[-3:-1]

    liste = satır.split(",")

    isim = liste[0]

    harf_not = liste[1]

    if harf_not == "FF":
        durum = "Kaldı"
    elif harf_not == "FD":
        durum = "Koşullu Kaldı"
    elif harf_not == "DD" or "DC":
        durum = "Koşullu Geçti"
    else:
        durum = "Geçti"
    return isim + " " + durum + "\n"






with open("dosya.txt","r",encoding="utf-8") as file:

    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

with open("notlar.txt","w",encoding="utf-8") as file2:

    for i in eklenecekler_listesi:
        file2.write(i)

with open("notlar.txt","r+",encoding="utf-8") as file3:

        kalanlar = []
        geçenler = []

        for i in file3:
            if "Kaldı" in kaldı_geçti(i):
                kalanlar.append(kaldı_geçti(i))
            else:
                geçenler.append(kaldı_geçti(i))

with open("kalanlar.txt", "w", encoding="utf-8") as file4:
    for i in kalanlar:
        file4.write(i)


with open("geçenler.txt","w",encoding="utf-8") as file5:
    for i in geçenler:
        file5.write(i)
