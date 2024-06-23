class Khodam:
    def __init__(self, name, element, description):
        self.name = name
        self.element = element
        self.description = description
    
    def get_info(self):
        return f"Nama Khodam: {self.name}\nElemen: {self.element}\nDeskripsi: {self.description}"

khodam_list = [
    Khodam("Khodam Api", "Api", "Khodam yang berhubungan dengan elemen api, seringkali dianggap kuat dan penuh energi."),
    Khodam("Khodam Air", "Air", "Khodam yang berhubungan dengan elemen air, dikenal tenang dan penuh ketenangan."),
    Khodam("Khodam Tanah", "Tanah", "Khodam yang berhubungan dengan elemen tanah, stabil dan kokoh."),
    Khodam("Khodam Angin", "Angin", "Khodam yang berhubungan dengan elemen angin, cepat dan tidak mudah ditebak.")
]

def find_khodam(description):
    for khodam in khodam_list:
        if khodam.element.lower() in description.lower():
            return khodam.get_info()
    return "Deskripsi tidak sesuai dengan jenis khodam yang diketahui."

description = input("Masukkan deskripsi khodam: ")

khodam_info = find_khodam(description)
print(khodam_info)
