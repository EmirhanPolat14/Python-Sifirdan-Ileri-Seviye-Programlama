def ebob_bul(sayi1,sayi2):
    i = 1
    ebob =1
    while sayi1 >= i and sayi2 >= i:
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob *= i
        i += 1
    return ebob

sayi1 = int(input("Birinci Sayıyı Giriniz:"))
sayi2 = int(input("İkinci Sayıyı Giriniz:"))

print("Ebob:",ebob_bul(sayi1,sayi2))