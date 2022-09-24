class Ogrenci():
    """Bu sınıftan bir obje oluşturmak için öğrencinin adını, soyadını ve sınıfını
    string olarak girin."""

    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinifi = ogrenci_sinifi


class Soru():
    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        girdi_alindi = False

        while girdi_alindi == False:
            dogru_sayisi = int(input("Doğru sayısını girin. \n"))

            if dogru_sayisi <= 50 and dogru_sayisi >= 0:
                print("Doğru Sayısı: ", dogru_sayisi)
                yanlis_sayisi = int(input("Yanlış sayısını girin. \n"))

                if yanlis_sayisi <= 50 and yanlis_sayisi >= 0:
                    print("Yanlış Sayısı:", yanlis_sayisi)
                    girdi_alindi = True

                    if dogru_sayisi + yanlis_sayisi > 50:
                        print("Doğru ve yanlış sayısı toplamı 50'den büyük olamaz.")
                        Soru.net_sayisi(self, "", "")

            else:
                print("0 ile 50 arasında bir sayı girin.")

        return dogru_sayisi - (yanlis_sayisi * 0.25)

    def hesapla(self, net_sayisi):
        return net_sayisi * 2


ogrenci1 = Ogrenci("Ahmet", "Tüfekçi", "9-C")
ogrenci_bilgisi = " Öğrenci Adı: {}\n Öğrenci Soyadı: {}\n Öğrenci Sınıfı: {}\n Puanı: {}"

sonuc = Soru().hesapla(Soru().net_sayisi("", ""))
print(ogrenci_bilgisi.format(ogrenci1.ogrenci_adi, ogrenci1.ogrenci_soyadi, ogrenci1.ogrenci_sinifi, sonuc))

