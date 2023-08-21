"""# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
sayi = float(input("Bir sayı giriniz:"))

kontrol = sayi > 0 and sayi < 100
result = f"{sayi} sayısı 0-100 arasında mı: {kontrol}"""

"""# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input("Lütfen bir sayı giriniz:"))

kontrol = sayi > 0 and sayi % 2 == 0

result = f"{sayi} sayısı hem pozitif hem de çift mi: {kontrol} """

"""# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = 'email@sadikturan.com'
# password = 'abc123'

email = input("email adresinizi giriniz:")
password = input("şifrenizi giriniz:")

kontrol = email == 'email@sadikturan.com' and password == 'abc123'

result = f"Parola ve kullanıcı adresi doğru mudur: {kontrol}"""

"""# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1 = int(input("1.sayı:"))
sayi2 = int(input("2.sayı:"))
sayi3 = int(input("3.sayı:"))

kontrol1 = sayi1 > sayi2 and sayi1 > sayi3
kontrol2 = sayi2 > sayi1 and sayi2 > sayi3
kontrol3 = sayi3 > sayi1 and sayi3 > sayi2

result = f"{sayi1} en büyük sayı mıdır: {kontrol1} \n{sayi2} en büyük sayı mıdır: {kontrol2}\n{sayi3} en büyük sayı mıdır: {kontrol3}"""


"""# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın
vize1 = float(input("1. vize notunuz:")) 
vize2 = float(input("2. vize notunuz:")) 
final = float(input("final notunuz:")) 

sonuc = ((vize1  + vize2) * 0.6) / 2 + (final *0.4)

kontrol = (sonuc >= 50 and final >= 50) or final >= 70 

result = f"Öğrencinin ortalaması:{sonuc}\nÖğrencinin geçme durumu:{kontrol}"""

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input("Adınız:")
kilo = float(input("Kilonuz(kg):"))
boy = float(input("Boyunuz(m):"))

indeks = kilo / boy ** 2

zayif = indeks >= 0 and indeks <=18.4
normal = indeks >= 18.5 and indeks <=24.9
fazla_kilolu = indeks >= 25 and indeks <=29.9
şişman = indeks >= 30


kiloindeks = f"{ad} kişisinin beden indeksi:{indeks}"
result = f"\n{ad} zayıftır:{zayif}\n{ad} normal kilodadır:{normal}\n{ad} fazla kiloludur:{fazla_kilolu}\n{ad} şişman(obez)dir:{şişman}\n"
print(kiloindeks,result)