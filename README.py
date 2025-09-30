def ogrenci_bilgileri():
    ogrenci = {
        "ad": input("Öğrencinin adı: "),
        "yas": int(input("Öğrencinin yaşı: ")),
        "not": float(input("Öğrencinin notu: "))
    }
    print("Öğrenci bilgileri:", ogrenci, "\n")
    return ogrenci

def harf_frekansi():
    kelime = input("Bir kelime girin: ")
    frekans = {}

    for harf in kelime:
        frekans[harf] = frekans.get(harf, 0) + 1

    print("Harf frekansları:", frekans, "\n")

def telefon_rehberi():
    rehber = {}
    while True:
        print("1 - Kişi Ekle\n2 - Kişi Ara\n3 - Rehberi Göster\n0 - Çıkış")
        secim = input("Seçim: ")
        if secim == "1":
            ad = input("Kişi adı: ")
            numara = input("Telefon numarası: ")
            rehber[ad] = numara
        elif secim == "2":
            ad = input("Aranacak kişinin adı: ")
            if ad in rehber:
                print(f"{ad} numarası: {rehber[ad]}")
            else:
                print("Kişi bulunamadı.")
        elif secim == "3":
            print("Rehber:", rehber)
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.\n")

def alisveris_listesi():
    liste = {}
    adet = int(input("Kaç ürün eklemek istiyorsunuz? "))
    for _ in range(adet):
        urun = input("Ürün adı: ")
        fiyat = float(input("Fiyatı: "))
        liste[urun] = fiyat
    print("Alışveriş listesi:", liste, "\n")
    return liste

def sozluk_goster(sozluk):
    print("Anahtarlar:", list(sozluk.keys()))
    print("Değerler:", list(sozluk.values()), "\n")
