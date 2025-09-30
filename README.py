def hafta_gunleri():
    gunler = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar")
    print("Haftanın ilk 3 günü:", gunler[:3], "\n")

def kelimelerden_tekrar_ayikla():
    kelimeler = input("Kelimeleri boşlukla ayırarak girin: ").split()
    ayiklanmis = set(kelimeler)
    print("Tekrar edenler ayıklandı, benzersiz kelimeler:", ayiklanmis, "\n")

def set_islemleri():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Kesişim:", set1 & set2)
    print("Birleşim:", set1 | set2)
    print("Set1 - Set2 farkı:", set1 - set2)
    print("Set2 - Set1 farkı:", set2 - set1, "\n")

def benzersiz_karakterler():
    metin = input("Bir metin girin: ")
    karakter_seti = set(metin)
    print("Metindeki benzersiz karakterler:", karakter_seti, "\n")

def dogum_tarihi():
    gun = int(input("Doğum gününüz (gün): "))
    ay = int(input("Doğum ayınız (1-12): "))
    yil = int(input("Doğum yılınız: "))
    tarih = (gun, ay, yil)
    print("Doğum tarihi (gün, ay, yıl):", tarih, "\n")
