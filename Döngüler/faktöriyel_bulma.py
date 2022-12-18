print("""***********************************

Faktöriyel Bulma Programı


Çıkmak için q'ya basın.
***********************************""")

while True:
    sayı = input("Sayı:")
    if sayı == "q":
        print("Program Sonlandırılıyor...")
        break

    else:
        sayı = int(sayı)

        faktöriyel = 1


        for i in range(2,sayı+1):

            faktöriyel *= i
        print("{}! = {} ".format(sayı,faktöriyel))

