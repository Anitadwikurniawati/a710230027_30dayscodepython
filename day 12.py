def hitung_huruf(kalimat, huruf):
    jumlah = kalimat.count(huruf)
    return jumlah

def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    
    huruf = input("Masukkan sebuah huruf yang ingin dihitung: ")
    
    if len(huruf) != 1:
        print("Harap masukkan satu huruf saja.")
        return
    
    jumlah = hitung_huruf(kalimat, huruf)
    
    print(f"Huruf '{huruf}' muncul sebanyak {jumlah} kali dalam kalimat.")

if __name__ == "__main__":
    main()
