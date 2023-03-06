def ekok_bul(sayi1,sayi2):
    i = 2
    ekok = 1
    while sayi1 >= i and sayi2 >= i:
        if sayi1 % i == 0 and sayi2 % i == 0:
            sayi1 /= i
            sayi2 /= i
            ekok *= i
            print(i, ekok, sayi1, sayi2)
        elif sayi1 % i == 0:
            sayi1 /= i
            ekok *= i
            print(i, ekok, sayi1, sayi2)
        elif sayi2 % i == 0:
            sayi2 /= i
            ekok *= i
            print(i, ekok, sayi1, sayi2)
        else:
            i += 1
        if sayi1 == 1 or sayi2 == 1:
            ekok *= sayi2 * sayi1
    return ekok










sayi1 = int(input("Birinci Sayıyı Giriniz:"))
sayi2 = int(input("İkinci Sayıyı Giriniz:"))

print("Ekok:",ekok_bul(sayi1,sayi2))











