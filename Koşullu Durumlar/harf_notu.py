v1 = int(input("Birinci Vize Notunuz:"))
v2 = int(input("İkinci Vize Notunuz:"))
f = int(input("Final Notunuz:"))
t_n = (v1 * 0.3) + (v2 * 0.3) + (f * 0.4)

if t_n >= 90:
    print("AA")
elif t_n >= 85:
    print("BA")
elif t_n >= 80:
    print("BB")
elif t_n >= 75:
    print("CB")
elif t_n >= 70:
    print("CC")
elif t_n >= 65:
    print("DC")
elif t_n >= 60:
    print("DD")
elif t_n >= 55:
    print("FD")
else:
    print("FF")