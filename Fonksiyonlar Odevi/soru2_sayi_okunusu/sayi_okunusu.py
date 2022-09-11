def sayi_atama():
    sayi_input = input("İki basamaklı bir sayi girin. ")

    return sayi_input


def sayi_okunusu():
    atanan_sayi = int(sayi_atama())

    if atanan_sayi >= 10 and atanan_sayi <= 99:
        
        birlik = atanan_sayi % 10
        onluk = int((atanan_sayi - birlik) / 10)

        okunuslar = {0: ["", ""], 1: ["on", "bir"], 2: ["yirmi", "iki"], 3: ["otuz", "üç"], 4: ["kırk", "dört"],
                 5: ["elli", "beş"], 6: ["altmış", "altı"], 7: ["yetmiş", "yedi"], 8: ["seksen", "sekiz"],
                 9: ["doksan", "dokuz"], }

        for key in okunuslar:
            if onluk == key:
                onluk = (okunuslar[key][0])

            if birlik == key:
                birlik = (okunuslar[key][1])

            elif type(onluk) is str and type(birlik) is str:
                break

    else:
        print("Sadece iki basamaklı sayılar girebilirsiniz. \n")

        sayi_okunusu()

    okunus = "Sayı okunuşu: {}{}"
    print(okunus.format(onluk, birlik))
