class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.fakultas = []

    def tambah_fakultas(self, fakultas):
        self.fakultas.append(fakultas)

    def deskripsi(self):
        deskripsi_fakultas = "\n".join([f.deskripsi() for f in self.fakultas])
        return f"Universitas {self.nama} memiliki fakultas:\n{deskripsi_fakultas}"

class Fakultas:
    def __init__(self, nama):
        self.nama = nama
        self.prodi = []

    def tambah_prodi(self, prodi):
        self.prodi.append(prodi)

    def deskripsi(self):
        deskripsi_prodi = "\n".join([p.deskripsi() for p in self.prodi])
        return f"Fakultas {self.nama}:\n{deskripsi_prodi}"

class ProgramStudi:
    def __init__(self, nama, jenjang):
        self.nama = nama
        self.jenjang = jenjang

    def deskripsi(self):
        return f"- {self.nama} ({self.jenjang})"

universitas = Universitas("Indonesia")

fakultas_teknik = Fakultas("Teknik")
fakultas_ekonomi = Fakultas("Ekonomi")
fakultas_ilmu_komputer = Fakultas("Ilmu Komputer")

fakultas_teknik.tambah_prodi(ProgramStudi("Teknik Informatika", "S1"))
fakultas_teknik.tambah_prodi(ProgramStudi("Teknik Sipil", "S1"))

fakultas_ekonomi.tambah_prodi(ProgramStudi("Manajemen", "S1"))
fakultas_ekonomi.tambah_prodi(ProgramStudi("Akuntansi", "S1"))

fakultas_ilmu_komputer.tambah_prodi(ProgramStudi("Sistem Informasi", "S1"))
fakultas_ilmu_komputer.tambah_prodi(ProgramStudi("Ilmu Komputer", "S1"))

universitas.tambah_fakultas(fakultas_teknik)
universitas.tambah_fakultas(fakultas_ekonomi)
universitas.tambah_fakultas(fakultas_ilmu_komputer)

print(universitas.deskripsi())
