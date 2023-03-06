birler = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}
onlar = {1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan"}

def sayi_oku(sayi):
    a = sayi // 10
    b = sayi % 10

    return onlar[a] + " " + birler[b]


sayi = int(input("Bir Sayı Giriniz:"))
print(sayi_oku(sayi))
