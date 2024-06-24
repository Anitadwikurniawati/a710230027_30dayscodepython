class TesKepribadian:
    def __init__(self):
        self.pertanyaan = [
            "Bagaimana kamu menghabiskan akhir pekanmu?",
            "Apa jenis pekerjaan yang kamu sukai?",
            "Bagaimana kamu menghadapi masalah?"
        ]
        self.pilihan = [
            ["A. Bersosialisasi dengan teman", "B. Bersantai di rumah", "C. Melakukan aktivitas outdoor"],
            ["A. Pekerjaan yang melibatkan banyak interaksi sosial", "B. Pekerjaan yang memungkinkan kamu bekerja sendiri", "C. Pekerjaan yang menantang fisikmu"],
            ["A. Mencari bantuan dari teman", "B. Menganalisis masalah secara mendalam", "C. Mengambil tindakan segera"]
        ]
        self.jawaban = {"A": 0, "B": 0, "C": 0}

    def tanya_jawab(self):
        for i in range(len(self.pertanyaan)):
            print(f"{i+1}. {self.pertanyaan[i]}")
            for pilihan in self.pilihan[i]:
                print(pilihan)
            jawaban = input("Pilihanmu: ").strip().upper()
            if jawaban in self.jawaban:
                self.jawaban[jawaban] += 1

    def hasil_kepribadian(self):
        if self.jawaban["A"] > self.jawaban["B"] and self.jawaban["A"] > self.jawaban["C"]:
            kepribadian = "Ekstrovert"
        elif self.jawaban["B"] > self.jawaban["A"] and self.jawaban["B"] > self.jawaban["C"]:
            kepribadian = "Introvert"
        elif self.jawaban["C"] > self.jawaban["A"] and self.jawaban["C"] > self.jawaban["B"]:
            kepribadian = "Petualang"
        else:
            kepribadian = "Campuran"
        return kepribadian

    def mulai_tes(self):
        print("Selamat datang di tes kepribadian sederhana!")
        print("Jawab pertanyaan berikut dengan memilih A, B, atau C.")
        self.tanya_jawab()
        hasil = self.hasil_kepribadian()
        print(f"Kepribadianmu adalah: {hasil}")

if __name__ == "__main__":
    tes = TesKepribadian()
    tes.mulai_tes()
