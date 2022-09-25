class Insan():
    def __init__(self, ad = "Ahmet", soyad = "Bulut", yas = 21, ulke = "Türkiye", sehir = "Ankara", yetenekler = []):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = yetenekler

    def kisi_bilgileri(self):
        bilgiler = "Ad: {}\n, Soyad: {}\n, Yaş: {}\n, Ülke: {}\n, Şehir: {}\n, Yetenekler: {}\n"

        print(bilgiler.format(Insan.ad, Insan.soyad))

    def yetenek_ekle(self):
        yeni_yetenek = input("Eklemek istediğiniz yeteneği yazın:\n")
        Insan().yetenekler.append(yeni_yetenek)


insan1 = Insan(Insan.kisi_bilgileri().bilgiler)

print(insan1)

# ogrenci1 = Ogrenci("Ahmet", "Tüfekçi", "9-C")
#
# ogrenci_bilgisi = " Öğrenci Adı: {}\n Öğrenci Soyadı: {}\n Öğrenci Sınıfı: {}\n Puanı: {}"
#
# sonuc = Soru().hesapla(Soru().net_sayisi("", ""))
#
# print(ogrenci_bilgisi.format(ogrenci1.ogrenci_adi, ogrenci1.ogrenci_soyadi, ogrenci1.ogrenci_sinifi, sonuc))
