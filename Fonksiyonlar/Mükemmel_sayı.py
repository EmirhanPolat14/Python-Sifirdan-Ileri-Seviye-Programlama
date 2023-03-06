def mükemmel_sayı(a):
    toplam = 0
    for i in range(1,a):
        if a % i == 0:
            toplam += i
    return toplam == a

for i in range(1,1001):
    if mükemmel_sayı(i):
        print("Mükemmel sayı:",i)

