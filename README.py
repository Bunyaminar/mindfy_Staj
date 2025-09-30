def bolme_islemi():
    try:
        sayi = float(input("Bir sayı girin: "))
        sonuc = sayi / 0
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!\n")
def sayi_giris_kontrol():
    try:
        sayi = int(input("Bir tam sayı girin: "))
        print("Girdiğiniz sayı:", sayi, "\n")
    except ValueError:
        print("Hata: Lütfen sadece tam sayı girin!\n")
def liste_index_hatasi():
    liste = [10, 20, 30]
    try:
        index = int(input("0-2 arasında bir index girin: "))
        print("Seçilen eleman:", liste[index], "\n")
    except IndexError:
        print("Hata: Listenin dışında bir index girdiniz!\n")
def loglu_bolme():
    try:
        a = int(input("Bölünen: "))
        b = int(input("Bölen: "))
        print("Sonuç:", a / b)
    except Exception as e:
        with open("hata_log.txt", "a") as dosya:
            dosya.write(f"Hata: {str(e)}\n")
        print("Bir hata oluştu, detaylar log dosyasına yazıldı.\n")
def ornek_finally():
    try:
        sayi = int(input("Bir sayı girin: "))
        print("Girilen sayı:", sayi)
    except ValueError:
        print("Geçersiz giriş!")
    finally:
        print("Bu mesaj her durumda çalışır (try/except ne olursa olsun).\n")
