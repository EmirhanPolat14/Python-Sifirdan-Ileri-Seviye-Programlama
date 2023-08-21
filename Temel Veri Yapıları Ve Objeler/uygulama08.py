"""# 1- Girilen 2 sayıdan hangisi büyüktür ?
a = int(input("Sayı1:"))
b = int(input("Sayı2:"))
result = (a > b)
print(f"{a} sayısı {b} sayısından büyük mü?" +  str(result))"""

"""# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1 = float(input("1.Vize Notu:"))
vize2 = float(input("2.Vize Notu:"))
final = float(input("Final Notu:"))

ortalama = (vize1 + vize2) * 0.3 + final * 0.40
result = ortalama"""


"""# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input("Sayı giriniz:"))

tekcift = sayi % 2 == 0
result = f"Girilen sayı çift midir? " + str(tekcift)"""

"""# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi = int(input("Bir sayı giriniz:"))

negatifpozitif = sayi > 0 and sayi != 0

result = f"Girilen sayı pozitif midir?" + "\n" + str(negatifpozitif)"""


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = input("Email adresi:")
sifre = input("şifreniz:")

dogrumu = email == "email@sadikturan.com" and sifre == "abc123"

result = "Girilen email ve pasaport:" + " " + str(dogrumu)


print(result)