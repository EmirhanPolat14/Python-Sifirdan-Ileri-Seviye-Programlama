sayi = input("Sayı Giriniz:")
basamak = len(sayi)
toplam = 0
i = 0

while basamak > i:
    a = int(sayi[i]) ** basamak
    toplam += a
    i += 1
if toplam == int(sayi):
    print("{} bir armstrong sayısıdır.".format(sayi))
else:
    print("{} bir armstrong sayısı değildir.".format(sayi))
