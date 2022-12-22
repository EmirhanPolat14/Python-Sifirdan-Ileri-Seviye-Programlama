liste1 = list(range(1,101))

liste2 = [i * 2 for i in liste1 if not i > 50]
print(liste2)
