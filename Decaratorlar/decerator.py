def ekstra(fonk):
    def wrapper(sayılar):
        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:
            if sayı % 2 == 0:
                çiftler_toplamı += sayı
                çift_sayılar += 1
            else:
                tekler_toplamı += sayı
                tek_sayılar += 1
        print("Çift Sayıların Ortalaması:{}\nTek Sayıların Ortalaması:{}".format(çiftler_toplamı / çift_sayılar,tekler_toplamı /tek_sayılar))
        fonk(sayılar)
    return wrapper

@ekstra
def ortalamabul(sayılar):

    toplam = 0

    for i in sayılar:
        toplam += i
    print("Genel Ortalama:",toplam / len(sayılar))

ortalamabul([1,2,3,4,60,62,34,100,105])