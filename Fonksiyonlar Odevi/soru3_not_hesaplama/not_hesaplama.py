def nothesaplama():
  def kullanici_girdi_kontrol(kullanici_girdisi):
    if kullanici_girdisi >= 0 and kullanici_girdisi <= 100:
      return kullanici_girdisi
    else:
      kullanici_girdisi = int(input("Yalnızca 0 ile 100 arasında bir sayı girin. \n"))
      return kullanici_girdi_kontrol(kullanici_girdisi)
        
  vize1 = int(input("Birinci vize notunu girin:\n (0 - 100) "))
  vize2 = int(input("İkinci vize notunu girin:\n (0 - 100) "))
  final = int(input("Final notunu girin:\n (0 - 100) "))
  
  vize1 = kullanici_girdi_kontrol(vize1)
  vize2 = kullanici_girdi_kontrol(vize2)
  final = kullanici_girdi_kontrol(final)  
    
  toplamnot = round((vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40))
  
  if toplamnot >= 90:
    print("Öğrenci Notu: AA")
  elif toplamnot >= 85:
    print("Öğrenci Notu: BA")
  elif toplamnot >= 80:
    print("Öğrenci Notu: BB")
  elif toplamnot >= 75:
    print("Öğrenci Notu: CB")
  elif toplamnot >= 70:
    print("Öğrenci Notu: CC")
  elif toplamnot >= 65:
    print("Öğrenci Notu: DC")
  elif toplamnot >= 60:
    print("Öğrenci Notu: DD")
  elif toplamnot >= 55:
    print("Öğrenci Notu: FD")
  elif toplamnot < 50:
    print("Öğrenci Notu: FF")

nothesaplama()
