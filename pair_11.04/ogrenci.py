class ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

    def ogrenciYazdir(self):
        print(f"Adi: {self.ad} Soyadi: {self.soyad} Numarasi: {self.numara} ")