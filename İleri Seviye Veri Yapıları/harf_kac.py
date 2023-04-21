a = list("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb".lower())

harf_frekans = dict()

for i in a:
    if i in harf_frekans:
        harf_frekans[i] += 1
    else:
        harf_frekans[i] = 1

for kelime,sayi in harf_frekans.items():
    print("Metin içinde {} harfinden {} tane vardır.".format(kelime,sayi))



