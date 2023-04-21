with open("siir.txt","r+",encoding="utf-8") as file:
    a = ""

    for i in file:
        a += i[0]
print(a)