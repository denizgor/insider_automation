def sayi_atama():
  sayi_input = input("İki basamaklı bir sayi girin. ")
  return sayi_input

def sayi_okunusu():
  atanan_sayi = int(sayi_atama())
  basamaklar = []
  
  for sayi in str(atanan_sayi):
      basamaklar.append(int(sayi))

  onluk = ""
  birlik = ""
  
  okunuslar = {1 : ["on", "bir"], 2 : ["yirmi", "iki"], 3 : ["otuz", "üç"], 4 : ["kırk",   "dört"], 5 : ["elli", "beş"], 
               6 : ["altmış", "altı"], 7 : ["yetmiş", "yedi"], 8 : ["seksen", "sekiz"], 9 : ["doksan","dokuz"], }
  
  if atanan_sayi >= 10 and atanan_sayi <= 99:
      for key in okunuslar:
        if basamaklar[0] == key:
            onluk = (okunuslar[key][0])
        if basamaklar[1] == key:
            birlik = (okunuslar[key][1])      
   
      print(f" Sayı okunuşu: {onluk}{birlik}")
  else:
    print("Sadece iki basamaklı sayılar girebilirsiniz. \n")
    sayi_okunusu()

sayi_okunusu()  

sayi_okunusu()  
