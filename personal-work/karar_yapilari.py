vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 
final2kat  = (final * 2) 

if final < 40:
    print("kaldi")
elif ortalama < 50:
    print("kaldi")
elif vize == final2kat:
    print("kaldi")
else:
    print("gecti")