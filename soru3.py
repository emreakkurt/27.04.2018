def etkilesim(begeni,yorum,paylasim,icerik,takipci):
    eoran=((begeni+yorum+paylasim)/icerik/takipci)*100
    return eoran

def basari(a):
    if a>0.2:
        print("Başarılı")
    elif a<0.2:
        print("Başarısız")
