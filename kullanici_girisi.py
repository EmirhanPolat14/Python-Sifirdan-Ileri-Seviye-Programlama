print("""****************
Kullanıcı Girişi
********************

""")

sys_kullanıcı_adı = "Ep1104"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if kullanıcı_adı == sys_kullanıcı_adı and sys_parola == parola:
    print("Giriş Başarılı..")
elif kullanıcı_adı != sys_kullanıcı_adı or sys_parola != parola:
    print("Hatalı Kullanıcı Adı veya Şifre Girdiniz")