yas = 25
boy = 1.75
kilo = 70

print("Yaş:", yas)
print("Boy:", boy)
print("Kilo:", kilo)

sayi1 = 10
sayi2 = 3

print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)
print("Bölüm:", sayi1 / sayi2)

yas = int(input("Yaşınızı girin: "))
print("5 yıl sonraki yaşınız:", yas + 5)

print(type(42))        
print(type(3.14))      
print(type("Merhaba")) 
print(type(True))      

# Hatalı tip dönüşümü örnekleri

# Metin sayı değilse int'e çevrilemez
try:
    sayi = int("Merhaba")
except ValueError as e:
    print("Hata:", e)

# Boolean'ı yanlış kullanma
try:
    toplam = True + "Merhaba"
except TypeError as e:
    print("Hata:", e)

# Sayı yerine None kullanma
try:
    sonuc = 5 + None
except TypeError as e:
    print("Hata:", e)
