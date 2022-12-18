a = int(input("Sayı Gir:"))
i = 1
toplam = 0

while a > i:
    if a % i == 0:
        toplam += i
    i += 1
if toplam == a:
    print("{} bir mükemel sayıdır.".format(a))
else:
    print("{} bir mükemmel sayı değildir!".format(a))








