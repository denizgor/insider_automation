

def sayi_atama():
  sayi_input = input("İki basamaklı bir sayi girin. ")
  return sayi_input



def sayi_okunusu():
  atanan_sayi = int(sayi_atama())
  basamaklar = []
  
  if atanan_sayi >= 10 and atanan_sayi <= 99:
    for sayi in str(atanan_sayi):
      basamaklar.append(int(sayi))
    
    if basamaklar[0] == 1:
      birinci_basamak = "on"
    elif basamaklar[0] == 2:
      birinci_basamak = "yirmi"
    elif basamaklar[0] == 3:
      birinci_basamak = "otuz"
    elif basamaklar[0] == 4:
      birinci_basamak = "kırk"
    elif basamaklar[0] == 5:
      birinci_basamak = "elli"
    elif basamaklar[0] == 6:
      birinci_basamak = "altmış"
    elif basamaklar[0] == 7:
      birinci_basamak = "yetmiş"
    elif basamaklar[0] == 8:
      birinci_basamak = "seksen"
    elif basamaklar[0] == 9:
      birinci_basamak = "doksan"
   
  
    if basamaklar[1] == 1:
      ikinci_basamak = "bir"
    elif basamaklar[1] == 2:
      ikinci_basamak = "iki"
    elif basamaklar[1] == 3:
      ikinci_basamak = "üç"
    elif basamaklar[1] == 4:
      ikinci_basamak = "dört"
    elif basamaklar[1] == 5:
      ikinci_basamak = "beş"
    elif basamaklar[1] == 6:
      ikinci_basamak = "altı"
    elif basamaklar[1] == 7:
      ikinci_basamak = "yedi"
    elif basamaklar[1] == 8:
      ikinci_basamak = "sekiz"
    elif basamaklar[1] == 9:
      ikinci_basamak = "dokuz"
    elif basamaklar[1] == 0:
      ikinci_basamak = ""
   
    print(birinci_basamak + ikinci_basamak)
  else:
    print("Sadece iki basamaklı sayılar girebilirsiniz. \n")
    sayi_okunusu()

sayi_okunusu()  
