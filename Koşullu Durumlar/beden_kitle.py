boy = float(input("Boy(m):"))
kilo = int(input("Kilo(kg):"))

beden_kitle_indeksi = kilo / (boy ** 2)

if beden_kitle_indeksi < 18.5:
    print("Zayıf")
elif beden_kitle_indeksi >= 18.5 and beden_kitle_indeksi < 25:
    print("Normal")
elif beden_kitle_indeksi >= 25 and beden_kitle_indeksi < 30:
    print("Fazla Kilolu")
else:
    print("Obez")
