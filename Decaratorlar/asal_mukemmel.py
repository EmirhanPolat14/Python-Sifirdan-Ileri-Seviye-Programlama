def ekstra(fonk):

    def wrapper():
        print("Asal Sayılar:")
        for sayı in range(1,1000):
            toplam = 0
            i = 1
            while i < sayı:
                if sayı % i == 0:
                    toplam += i
                i += 1
            if toplam == sayı:
                print(sayı)
        fonk()
    return wrapper

@ekstra
def asal():
    print("Asal Sayılar:")
    for sayı in range(2,1000):
        i = 2
        say = 0
        while i < sayı:
            if sayı % i == 0:
                say += 1
            i += 1
        if say == 0:
            print(sayı)

asal()

