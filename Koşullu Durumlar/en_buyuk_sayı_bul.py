a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = int(input("Üçüncü Sayı:"))

if a > b and a > c:
    print("En Büyük Sayı:",a)
elif b > a and b > c:
    print("En Büyük Sayı:",b)
else:
    print("En Büyük Sayı:",c)
