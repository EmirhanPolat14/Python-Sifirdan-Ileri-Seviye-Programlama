import os
text = []
mp4 = []
pdf = []

for klasor_yolu, klasor_isim, dosya_isim in os.walk("C:/Users/LEGION"):
    for i in dosya_isim:
        if i.endswith(".txt"):
            i = i + "\n"
            text.append(i)
        elif i.endswith("mp4"):
            i = i + "\n"
            mp4.append(i)
        elif i.endswith("pdf"):
            i = i + "\n"
            pdf.append(i)

with open("txt_dosyaları.txt", "w", encoding="utf-8") as file:

    for j in text:
        
        file.write(j)

with open("mp4_dosyaları.txt", "w", encoding="utf-8") as file:

    for a in mp4:

        file.write(a)


with open("pdf_dosyaları.txt", "w", encoding="utf-8") as file:

    for x in pdf:

        file.write(x)
