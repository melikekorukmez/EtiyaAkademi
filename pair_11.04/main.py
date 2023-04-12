# bir okul kayıt sistemi kodlayalım:
# Öğrenci ve öğretmen classları farklı dosyalarda oluştur.
# Classlar en az 2 property 2 method barındırmalı.
# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım.
# Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim.
# Konsolda test edelim
# Classlarımızın içerisinde self keywordü kullanlaım. Class içi fonksiyonlarda içerisindeki propertylerden yararlanalım.

from ogrenci import ogrenci
from ogretmen import ogretmen

def listeyeEkle():
    ogrenciListesi.append(ogrenci1)
    ogretmenListesi.append(ogretmen1)

def listeyiYazdir():
    for i in ogrenciListesi:
        print(i.ogrenciYazdir())
    
    for i in ogretmenListesi:
        print(i.ogretmenYazdir())

ogrenciListesi = []
ogretmenListesi = []

ogrenci1 = ogrenci("mel","kor",35)
ogretmen1 = ogretmen("alp","demir","matematik")

listeyeEkle()
listeyiYazdir()


