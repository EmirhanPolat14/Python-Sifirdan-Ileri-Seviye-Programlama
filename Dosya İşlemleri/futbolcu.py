#def takımlar(satır):
    #satır = satır[:-1]
    #liste = satır.split(",")


with open("futbolcular.txt","r+",encoding="utf-8") as file:
    liste = list()
    galatasaray = list()
    fenerbahçe = list()
    beşiktaş = list()

    for i in file:
        i = i[:-1]
        i = i.split(",")
        liste.append(i)
    print(liste)

    for i in liste:
        if i[1] == "Galatasaray":
            galatasaray.append(i[0])
        elif i[1] == "Fenerbahçe":
            fenerbahçe.append(i[0])
        else:
            beşiktaş.append(i[0])
    print(galatasaray,fenerbahçe,beşiktaş)

with open("Galatasaray.txt","w",encoding="utf-8") as file2:
    for i in galatasaray:
        i = i + "\n"
        file2.write(i)


with open("Fenerbahçe.txt","w",encoding="utf-8") as file3:
    for i in fenerbahçe:
        i = i + "\n"
        file3.write(i)


with open("Beşiktaş.txt","w",encoding="utf-8") as file4:
    for i in beşiktaş:
        i = i + "\n"
        file4.write(i)
