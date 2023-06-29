names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]
"""
# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
result = names

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
result = names

# 3-  "Deniz" ismini listeden siliniz.
names.remove("Deniz")
result = names"""

# 4-  "Deniz" isminin indeksi nedir ?
result = names.index("Deniz")

# 5-  "Ali" listenin bir elemanı mıdır ?
result = "Ali" in names


# 6-  Liste elemanlarını ters çevirin.
result = names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
result = names.sort()


# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
years.reverse()

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result3 = str.split(",")
"""
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(max(years),min(years))

# 11- years dizisinde kaç tane 1998 değeri vardır ?
result3 = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)"""

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
liste = [input("Marka 1:"),input("Marka 2:"),input("Marka 3:")]
print(liste)
"""result2 = years
result = names
print(result3)"""
