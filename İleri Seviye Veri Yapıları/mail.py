with open("mailler.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")
        if i.endswith(".com") and i.find("@") != -1:
            print(i)