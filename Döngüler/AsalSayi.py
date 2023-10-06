sayi = int(input("Bir sayı giriniz:"))
asal_mi = True


if sayi == 1:
    asal_mi=False        
for i in range(2,sayi):
    if sayi % i == 0:
        asal_mi=False
        break

if asal_mi:
    print(f"{sayi} sayısı asal bir sayıdır.")
else:
  print(f"{sayi} sayısı asal bir sayı değildir.")
  
        
    
