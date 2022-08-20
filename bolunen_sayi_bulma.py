def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
  tam_bolunenler = []

  min_sayi = int(input("Minimum sayıyı girin:\n"))
  while min_sayi <= 0:
    print("Minimum sayı 0'dan büyük olmalıdır")
    min_sayi = int(input("Minimum sayıyı girin:\n"))

  max_sayi = int(input("Maksimum sayıyı girin:\n"))
  while max_sayi < min_sayi:
    print("Maksimum sayı minimum sayıdan küçük olamaz.")
    max_sayi = int(input("Maksimum sayıyı girin:\n"))
  
  bolen_sayi = int(input("Bölen sayıyı girin:\n"))
  while bolen_sayi > max_sayi:
    print("Bölen sayı maksimum sayıdan büyük olamaz.")
    bolen_sayi = int(input("Bölen sayıyı girin:\n"))
  
  for sayi in range(min_sayi, max_sayi):
    if sayi % bolen_sayi == 0:
      tam_bolunenler.append(sayi)
  
  print("Tam Bölünenler: ",tam_bolunenler)
  print("Tam Bölünen Sayı Adedi: ", len(tam_bolunenler))
  return(tam_bolunenler, len(tam_bolunenler))
  
bolunen_sayi_bulma(min_sayi="", max_sayi="", bolen_sayi="")
