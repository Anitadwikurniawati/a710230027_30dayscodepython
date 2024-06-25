import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    
    try:
        min_range = int(input("Masukkan angka minimum: "))
        max_range = int(input("Masukkan angka maksimum: "))
        
        if min_range >= max_range:
            print("Angka minimum harus lebih kecil dari angka maksimum.")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")
        return
    
    print(f"Saya memikirkan sebuah angka antara {min_range} dan {max_range}.")
    
    number_to_guess = random.randint(min_range, max_range)
    attempts = 0
    guess_history = []
    
    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1
            guess_history.append(guess)
            
            if guess < number_to_guess:
                print("Terlalu rendah! Coba lagi.")
            elif guess > number_to_guess:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Anda berhasil menebak angka dalam {attempts} percobaan.")
                print(f"Riwayat tebakan Anda: {guess_history}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka bulat.")

if __name__ == "__main__":
    main()
