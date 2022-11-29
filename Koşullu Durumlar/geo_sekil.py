şekil = input("Hangi Şekli İstiyorsun? (Üçgen ya da Dörtgen):")

if şekil == "Dörtgen" and şekil == "dörtgen":
    a = int(input("Birinci Kenar:"))
    b = int(input("İkinci Kenar:"))
    c = int(input("Üçüncü Kenar:"))
    d = int(input("Dördüncü Kenar:"))
    if a == b and b == c and c == d:
        print("Kare")
    elif a == b or a == c or a == d or b == c or b == d or c == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")
elif şekil == "Üçgen" or şekil == "üçgen":
    e = int(input("Birinci Kenar:"))
    f = int(input("İkinci Kenar:"))
    g = int(input("Üçüncü Kenar:"))
    if f + g > e > abs(f - g) and e + g > e > abs(e - g) and e + g > e > abs(e - g) and e + f > e > abs(e - f):
        if e == f == g:
            print("Eşkenar Üçgen")
        elif e == f or f == g or e == g:
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmiyor!")
else:
    print("Geçersiz Şekil")






