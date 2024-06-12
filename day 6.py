from abc import ABC, abstractmethod

class Bentuk(ABC):
    def luas(self):
        pass

class PersegiPanjang(Bentuk):
    def __init__(self, lebar, tinggi):
        self.lebar = lebar
        self.tinggi = tinggi
    
    def luas(self):
        return self.lebar * self.tinggi

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius
    
    def luas(self):
        return 3.14 * self.radius ** 2

def cetak_luas(bentuk):
    print(f"Luasnya adalah {bentuk.luas()}")

persegi_panjang = PersegiPanjang(4, 5)
lingkaran = Lingkaran(3)

cetak_luas(persegi_panjang)  
cetak_luas(lingkaran)        