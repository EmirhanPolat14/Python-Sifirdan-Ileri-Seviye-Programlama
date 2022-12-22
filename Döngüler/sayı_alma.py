print("""******************
Programdan çıkmak için 'q'ya basınız!!!
******************


""")
toplam = 0

while True:
    a = input("Bir Sayı Giriniz:")
    if a == "q":
        print("Girilen Sayıların Toplamı = {}\nProgramdan çıkılıyor...".format(toplam))
        break
    else:
        toplam += int(a)