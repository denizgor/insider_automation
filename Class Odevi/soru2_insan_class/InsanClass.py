class Insan():
    def __init__(self, ad = "Ahmet", soyad = "Bulut", yas = 21, ulke = "Türkiye", sehir = "Ankara", yetenekler = []):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = yetenekler

    def kisi_bilgileri(self):
        bilgiler = "Ad: {}\nSoyad: {}\nYaş: {}\nÜlke: {}\nŞehir: {}\nYetenekler: {}\n"
        return(bilgiler.format(Insan().ad, Insan().soyad, Insan().yas, Insan().ulke, Insan().sehir, Insan().yetenekler))


    def yetenek_ekle(self):
        yeni_yetenek = input("Eklemek istediğiniz yeteneği yazın:\n")
        Insan().yetenekler.append(yeni_yetenek)
        #print(Insan().kisi_bilgileri())
        print("Yetenekler:", Insan().yetenekler)


#Test
insan1 = Insan().kisi_bilgileri()
print(insan1)

#tek bir parametre alma
#print(Insan().kisi_bilgileri(Insan().ad))
#çalışmadı

insan2 = Insan("Mustafa", "Akıncı", 24, "Türkiye", "İzmir").kisi_bilgileri()
Insan().yetenek_ekle()
print("İnsan 2:", insan2)


