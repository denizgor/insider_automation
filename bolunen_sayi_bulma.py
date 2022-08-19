def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
  tam_bolunenler = []
  for sayi in range(min_sayi, max_sayi):
    if sayi % bolen_sayi == 0:
      tam_bolunenler.append(sayi)
  # print(range(min_sayi, max_sayi))
  # print("Tam Bölünenler: ",tam_bolunenler)
  # print("Değerler: ", len(tam_bolunenler))
  return(tam_bolunenler, len(tam_bolunenler))
  
bolunen_sayi_bulma(12,103,6)