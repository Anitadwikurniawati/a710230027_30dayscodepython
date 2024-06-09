class HewanPeliharaan:
    def __init__(self, nama, jenis, umur):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur

    def info(self):
        return f"{self.nama} adalah {self.jenis} berumur {self.umur} tahun"

    def tambah_umur(self, tahun):
        self.umur += tahun
        return f"Umur {self.nama} sekarang menjadi {self.umur} tahun"

class Pemilik:
    def __init__(self, nama):
        self.nama = nama
        self.hewan_peliharaan = []

    def tambah_hewan(self, hewan):
        self.hewan_peliharaan.append(hewan)

    def info_hewan_peliharaan(self):
        info = f"Pemilik: {self.nama}\n"
        info += "Daftar Hewan Peliharaan:\n"
        for hewan in self.hewan_peliharaan:
            info += hewan.info() + "\n"
        return info


hewan1 = HewanPeliharaan("Tiyo", "Anjing", 3)
hewan2 = HewanPeliharaan("Tata", "Kucing", 2)
hewan3 = HewanPeliharaan("Bg", "Burung", 1)

pemilik = Pemilik("Azzam")

pemilik.tambah_hewan(hewan1)
pemilik.tambah_hewan(hewan2)
pemilik.tambah_hewan(hewan3)

print(pemilik.info_hewan_peliharaan())

print(hewan1.tambah_umur(1))
print(hewan2.tambah_umur(2))
print(hewan3.tambah_umur(3))

print(pemilik.info_hewan_peliharaan())
