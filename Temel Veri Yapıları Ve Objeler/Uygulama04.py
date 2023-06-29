# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ["Bmw","Mercedes","Opel","Mazda"]

# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)

"""# 3-  Listenin ilk ve son elemanı nedir ?
print(arabalar[0],arabalar[3])"""

# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[3] = "Toyota"
#print(arabalar)

# arabalar[-1]= 'Toyota'

# 5-  Mercedes listenin bir elemanı mıdır ?
result = "Mercedes" in arabalar

# 6-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]

# 7-  Listenin ilk 3 elemanını alın.
result = arabalar[0:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-1],arabalar[-2] = "Renault","Toyota"
result = arabalar

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ["Audi","Nissan"]

# 10- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar

# 11- Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ["Yiğit Bilgi", 2010, (70,60,70)]
studentB = ["Sena Turan", 1999, (80,80,70)]
studentC = ["Ahmet Turan", 1998, (80,70,90)]


# 13- Liste elemanlarını ekrana yazdırınız.
result = [studentA] + [studentB] + [studentC]
print(result)