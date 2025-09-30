def resit_kontrol():
    yas = int(input("Yaşınızı girin: "))
    if yas >= 18:
        print("Reşitsiniz.\n")
    else:
        print("Reşit değilsiniz.\n")

def not_kontrol():
    not_ = float(input("Notunuzu girin (0-100): "))
    if not_ >= 50:
        print("Geçtiniz.\n")
    else:
        print("Kaldınız.\n")

def sayi_tahmin():
    dogru_sayi = 7
    tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
    if tahmin == dogru_sayi:
        print("Tebrikler! Doğru tahmin.\n")
    else:
        print("Yanlış tahmin. Doğru sayı:", dogru_sayi, "\n")

def en_buyuk_bul():
    sayi1 = float(input("1. sayıyı girin: "))
    sayi2 = float(input("2. sayıyı girin: "))
    sayi3 = float(input("3. sayıyı girin: "))
    en_buyuk = max(sayi1, sayi2, sayi3)
    print("En büyük sayı:", en_buyuk, "\n")

def sayi_durumu():
    sayi = float(input("Bir sayı girin: "))
    if sayi > 0:
        print("Pozitif bir sayı.\n")
    elif sayi < 0:
        print("Negatif bir sayı.\n")
    else:
        print("Sayı sıfır.\n")

def menu():
    while True:
        print("=== İşlem Menüsü ===")
        print("1 - Reşitlik Kontrolü")
        print("2 - Not ile Geçti/Kaldı")
        print("3 - Sayı Tahmin Oyunu")
        print("4 - En Büyük Sayıyı Bul")
        print("5 - Sayı Durumu (Pozitif/Negatif/Sıfır)")
        print("0 - Çıkış")
        
        secim = input("Bir işlem seçin (0-5): ")

        if secim == "1":
            resit_kontrol()
        elif secim == "2":
            not_kontrol()
        elif secim == "3":
            sayi_tahmin()
        elif secim == "4":
            en_buyuk_bul()
        elif secim == "5":
            sayi_durumu()
        elif secim == "0":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen 0-5 arası bir sayı girin.\n")

# Programı başlat
menu()
