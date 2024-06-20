def hitung_rata_rata(angka_list):
    jumlah = sum(angka_list)
    rata_rata = jumlah / len(angka_list)
    return rata_rata

def main():
    angka_list = []
    
    jumlah_angka = int(input("Masukkan jumlah angka yang ingin dihitung rata-ratanya: "))
    
    for i in range(jumlah_angka):
        angka = float(input(f"Masukkan angka ke-{i+1}: "))
        angka_list.append(angka)
    
    rata_rata = hitung_rata_rata(angka_list)
    
    print(f"Rata-rata dari angka yang dimasukkan adalah: {rata_rata}")

if __name__ == "__main__":
    main()
