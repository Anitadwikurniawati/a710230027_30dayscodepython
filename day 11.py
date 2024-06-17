import random

def main():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    print("Coba tebak angka tersebut dalam secepat mungkin.")
    
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0

    while guess != number_to_guess:
        guess = int(input("Masukkan tebakkanmu: "))
        number_of_guesses += 1

        if guess < number_to_guess:
            print("Terlalu rendah! Coba lagi.")
        elif guess > number_to_guess:
            print("Terlalu tinggi! Coba lagi.")

    print(f"Selamat! Anda berhasil menebak angka {number_to_guess} dalam {number_of_guesses} kali tebakan.")

if __name__ == "__main__":
    main()
