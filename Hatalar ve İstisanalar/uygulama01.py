liste = ["1","2","5a","10b","abc","10","50"]

"""
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
for i in liste:
    try:
        print(int(i))
    except ValueError:
        pass
#        continue ---> ikinci bir seçenek
"""



# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.
    
"""while True:
    a = input('Bir Sayı Giriniz:')
    if a == 'q':
        break
    else:
        try:
            int(a)
        except ValueError:
            print("Hatalı bir değer girdiniz")"""



# 3: Girilen parola içinde türkçe karakter hatası veriniz.
turkce_karaktereler= "ğüşıİç"

parola = input("Parolanızı girin:")

for i in parola:
    if i in turkce_karaktereler:
        raise TypeError("Parola Türkçe karakter barındıramaz!")
