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
                        dogru_sayisi = int(input("Doğru sayısını girin. \n"))
                        yanlis_sayisi = int(input("Yanlış sayısını girin. \n"))

                else:
                    print("Yanlış sayısı 0 ile 50 arasında olmalıdır.")

            else:
                print("Doğru sayısı 0 ile 50 arasında olmalıdır.")

        return dogru_sayisi - (yanlis_sayisi * 0.25)

    def hesapla(self, net_sayisi):
        return net_sayisi * 2
