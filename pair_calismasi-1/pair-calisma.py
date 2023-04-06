vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 
print("Ortalaman:", ortalama)

if 0 <= ortalama and ortalama <= 49:
    print("FF")
elif 50 <= ortalama and ortalama <= 59:
    print("DD")
elif 60 <= ortalama and ortalama <= 69:
    print("CC")
elif 70 <= ortalama and ortalama <= 79:
    print("BB")
elif 80 <= ortalama and ortalama <= 100:
    print("Av") 