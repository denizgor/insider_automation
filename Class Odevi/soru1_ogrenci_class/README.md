
Test kodu:
ogrenci1 = Ogrenci("Ahmet", "Tüfekçi", "9-C")
ogrenci_bilgisi = " Öğrenci Adı: {}\n Öğrenci Soyadı: {}\n Öğrenci Sınıfı: {}\n Puanı: {}"

sonuc = Soru().hesapla(Soru().net_sayisi("", ""))
print(ogrenci_bilgisi.format(ogrenci1.ogrenci_adi, ogrenci1.ogrenci_soyadi, ogrenci1.ogrenci_sinifi, sonuc))
