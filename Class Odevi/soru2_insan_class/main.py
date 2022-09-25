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


#Test
insan1 = Insan().kisi_bilgileri()





print(insan1)

#tek bir parametre alma
#print(Insan().kisi_bilgileri(Insan().ad))

# ogrenci1 = Ogrenci("Ahmet", "Tüfekçi", "9-C")
#
# ogrenci_bilgisi = " Öğrenci Adı: {}\n Öğrenci Soyadı: {}\n Öğrenci Sınıfı: {}\n Puanı: {}"
#
# sonuc = Soru().hesapla(Soru().net_sayisi("", ""))
#
# print(ogrenci_bilgisi.format(ogrenci1.ogrenci_adi, ogrenci1.ogrenci_soyadi, ogrenci1.ogrenci_sinifi, sonuc))
