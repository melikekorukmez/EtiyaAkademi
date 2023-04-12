class ogretmen:
    def __init__(self, ad, soyad, brans):
        self.ad = ad
        self.soyad = soyad
        self.brans = brans
    
    def ogretmenYazdir(self):
        print(f"Adi: {self.ad} Soyadi: {self.soyad} Bransi: {self.brans} ")