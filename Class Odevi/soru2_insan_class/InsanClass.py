class Insan:
    def __init__(self, ad="Ahmet", soyad="Bulut", yas=21, ulke="Türkiye", sehir="Ankara"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        bilgiler = "Ad: {}\nSoyad: {}\nYaş: {}\nÜlke: {}\nŞehir: {}\nYetenekler: {}\n"
        return bilgiler.format(self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler)

    def yetenek_ekle(self):
        yeni_yetenek = input("Eklemek istediğiniz yeteneği yazın:\n")
        self.yetenekler.append(yeni_yetenek)
