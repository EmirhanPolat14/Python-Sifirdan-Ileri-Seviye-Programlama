'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        '128': {
        },
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''



numara1 = input("Öğrenci Numarası:")
ad1 = input("Öğrencinin İsmi:")
soyad1 = input("Öğrencinin Soyismi:")
telno1 = input("Öğrencinin Telefonu:")

numara2 = input("Öğrenci Numarası:")
ad2 = input("Öğrencinin İsmi:")
soyad2 = input("Öğrencinin Soyismi:")
telno2 = input("Öğrencinin Telefonu:")

numara3 = input("Öğrenci Numarası:")
ad3 = input("Öğrencinin İsmi:")
soyad3 = input("Öğrencinin Soyismi:")
telno3 = input("Öğrencinin Telefonu:")

ogrenciler = {numara1: {
    "ad": ad1,
    "soyad":soyad1,
    "telefon": telno1
}, numara2: {"ad": ad2,
    "soyad":soyad2,
    "telefon": telno2},
    numara3: {"ad": ad3,
    "soyad": soyad3,
    "telefon": telno3}

           }
print(ogrenciler[input("numara:")])