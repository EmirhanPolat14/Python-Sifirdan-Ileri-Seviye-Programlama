sayilar = [1,3,5,7,9,12,19,21]

"""# 1: sayilar listesini while ile ekrana yazdırın.
i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1"""

"""# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm  tek sayıları ekrana yazdırın.
basla = int(input("Başlangıç Değeri:"))
bitis = int(input("Bitis Değeri:"))
i = basla + 1

while i < bitis:
    if i % 2 == 1:
        print(i)
    i += 1"""

"""# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100

while i > 2:
    i -= 1
    print(i)"""

"""# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
num1 = input("Aralarda boşluk bırakarak 5 tane sayı giriniz:")
nums = num1.split(" ")

i = 0
temp = 0
j = len(nums) - 1
while j > 0:
    while i < len(nums) - 1:

        if nums[i] > nums[i + 1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
            
        i += 1
    i = 0
    j -= 1
print(nums)"""

#Yol 2:
numbers = []
i = 0
while i<5:
     sayi = int(input('sayı: '))
     numbers.append(sayi)
     i+=1
numbers.sort()
print(numbers)

"""# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urun_sayisi= int(input("Ürün Sayısı:"))
urunler = []

i = 0
while i < urun_sayisi:
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        "name": name,
        "price": price
    })
    i += 1

for urun in urunler:
    print(f"Ürün Adı: {urun['name']} Ürün Fiyatı: {urun['price']}")"""
