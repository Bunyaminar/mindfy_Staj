def tek_sayilari_yazdir():
    print("1'den 100'e kadar olan tek sayılar:")
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end=' ')
    print("\n")

def ortalama_hesapla():
    sayilar = []
    for i in range(5):
        sayi = float(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)
    ortalama = sum(sayilar) / len(sayilar)
    print("Girilen sayıların ortalaması:", ortalama, "\n")

def carpim_tablosu():
    print("1'den 10'a kadar çarpım tablosu:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print()

def toplam_100():
    toplam = sum(range(1, 101))
    print("1'den 100'e kadar olan sayıların toplamı:", toplam, "\n")

def cift_sayilari_listele():
    sinir = int(input("Kaça kadar olan çift sayıları listelemek istersiniz? "))
    print(f"0'dan {sinir}'e kadar olan çift sayılar:")
    for i in range(0, sinir + 1, 2):
        print(i, end=' ')
    print("\n")

    
