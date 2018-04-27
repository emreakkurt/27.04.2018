from soru2 import aktif,pasif

donenVarlik=128000
duranVarlik=183000

a=aktif(donenVarlik,duranVarlik)

print("aktif toplamınız:",a,"tl")

kisaVade=102000
uzunVade=150000
ozKaynak=59000

b=pasif(kisaVade,uzunVade,ozKaynak)

print("pasif toplamınız:",b,"tl")

if a==b:
    print("Kapanış bilançosu doğru hesaplanmıştır")
else:
    print("Bilanço yanlış hesaplanmıştır")
    

