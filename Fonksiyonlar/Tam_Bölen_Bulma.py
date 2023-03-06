def tam_bolen(a):
    tam_bolenler = []
    for i in range(2,a):
        if a % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler

while True:

    sayı = input("Sayı:")
    if sayı == "q":
        break
    else:
        sayı = int(sayı)
        print("Tam bölenler:",tam_bolen(sayı))
