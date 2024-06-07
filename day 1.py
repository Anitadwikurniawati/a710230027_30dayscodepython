class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"{self.nama} - Harga: {self.harga} - Stok: {self.stok}"

class Toko:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
        print(f"Produk {produk.nama} telah ditambahkan ke toko {self.nama}.")

    def tampilkan_produk(self):
        print(f"Daftar Produk di {self.nama}:")
        for produk in self.daftar_produk:
            print(produk)

if __name__ == "__main__":
    toko = Toko("Toko Serba Ada")

    produk1 = Produk("Permen Chupa Chups", 5000, 7)
    produk2 = Produk("Susu Tujuh Kurma", 8000, 5)
    toko.tambah_produk(produk1)
    toko.tambah_produk(produk2)

    toko.tampilkan_produk()