def pisagor():
    pisagor_list = list()
    for a in range(1,101):
        for b in range(1,101):
            c = (a ** 2 + b ** 2) ** 0.5
            if (c == int(c)):
                pisagor_list.append((a, b, int(c)))

    return pisagor_list


for i in pisagor():
    print(i)






