def bilgi_kaydet_txt():
    bilgi = input("Kaydedilecek bilgiyi girin: ")
    with open("kullanici_bilgisi.txt", "a", encoding="utf-8") as dosya:
        dosya.write(bilgi + "\n")
    print("Bilgi başarıyla kaydedildi.\n")
def txt_satir_satir_oku():
    try:
        with open("kullanici_bilgisi.txt", "r", encoding="utf-8") as dosya:
            print("Dosya içeriği:")
            for satir in dosya:
                print(satir.strip())
        print()
    except FileNotFoundError:
        print("Dosya bulunamadı.\n")
import json

def sozluk_json_islemleri():
    veri = {
        "ad": "Ali",
        "yas": 25,
        "sehir": "İstanbul"
    }

    with open("veri.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)
    print("Sözlük JSON dosyasına kaydedildi.")

    with open("veri.json", "r", encoding="utf-8") as dosya:
        okunan_veri = json.load(dosya)
        print("Okunan veri:", okunan_veri, "\n")
from datetime import datetime

def tarih_yaz():
    simdi = datetime.now()
    with open("tarih_kaydi.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"Tarih: {simdi.strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("Tarih dosyaya yazıldı.\n")
import random
import string

def rastgele_sifre_uret(uzunluk=10):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    print("Oluşturulan şifre:", sifre, "\n")
