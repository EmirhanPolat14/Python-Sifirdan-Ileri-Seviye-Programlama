isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]


i = 1
j = 0
while i <= len(soyisim) + 6:
    isim.insert(i,soyisim[j])
    i += 2
    j += 1

x = 0
while x < len(isim) - 1:
    print(isim[x],isim[x+1])
    x += 2

