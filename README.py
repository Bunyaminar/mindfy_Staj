def toplam(sayi1, sayi2):
    return sayi1 + sayi2
def asal_mi(sayi):
    if sayi <= 1:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True
def ortalama_hesapla(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)
def metni_ters_cevir(metin):
    return metin[::-1]
def karelerini_al(liste):
    return [x**2 for x in liste]

print("Toplam:", toplam(5, 8))
print("Asal mı:", asal_mi(29))
print("Ortalama:", ortalama_hesapla([10, 15, 20]))
print("Ters:", metni_ters_cevir("Python"))
print("Kareler:", karelerini_al([1, 2, 3, 4]))
