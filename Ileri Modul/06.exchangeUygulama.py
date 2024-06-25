import requests
import json

api_key = "your api key"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_döviz = input("Hangi para birimini bozdurmak istiyorsunuz:")
alinacak_döviz = input("Hangi para birimini almak istiyorsunuz:")
miktar = int(input(f"Ne {bozulan_döviz} bozdurmak istiyorsunuz:" ))

sonuc = requests.get(api_url + bozulan_döviz)
sonuc = json.loads(sonuc.text)
doviz = sonuc["conversion_rates"][alinacak_döviz]

print("1 {0} anlık olarak {1} {2} değerindedir".format(bozulan_döviz, doviz, alinacak_döviz))
print("{} {} = {} {}".format(miktar, bozulan_döviz, doviz * miktar, alinacak_döviz))

