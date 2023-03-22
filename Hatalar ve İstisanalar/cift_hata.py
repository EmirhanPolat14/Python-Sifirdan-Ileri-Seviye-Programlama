def cift_mi(a):
    if a % 2 == 0:
        return a
    else:
        raise ValueError


liste = [2,4,6,8,23,45,44,68,14,28,20,36,789]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass
