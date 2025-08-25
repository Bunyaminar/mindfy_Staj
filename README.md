def isim_listesi_olustur():
    isimler = []
    for i in range(3):
        isim = input(f"{i+1}. ismi girin: ")
        isimler.append(isim)
    print("Oluşturulan liste:", isimler, "\n")
    return isimler

def ilk_son_yazdir(liste):
    if liste:
        print("İlk eleman:", liste[0])
        print("Son eleman:", liste[-1], "\n")
    else:
        print("Liste boş.\n")

def liste_ters_ve_sirala(liste):
    ters = list(reversed(liste))
    print("Ters çevrilmiş liste:", ters)
    try:
        sirali = sorted(liste)
        print("Sıralanmış liste:", sirali, "\n")
    except TypeError:
        print("Liste sıralanamıyor (farklı türde elemanlar olabilir).\n")

def karma_liste_olustur():
    karma = ["elma", 42, "muz", 3.14, "armut", 7]
    print("Karma liste:", karma, "\n")
    return karma

def ortadaki_elemani_sil(liste):
    if not liste:
        print("Liste boş, silinecek bir şey yok.\n")
        return liste
    orta_index = len(liste) // 2
    silinen = liste.pop(orta_index)
    print(f"Ortasındaki eleman '{silinen}' silindi.")
    print("Yeni liste:", liste, "\n")
    return liste
