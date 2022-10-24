# Membuat 3 class, 2 atribut, construktor dan 3 objek

class mahasiswa:
    nama = "Zuma"
    kelas = 'B'
    def __init__(self):
        print("Hai " + self.nama + " dari kelas " + self.kelas + ", Selamat Datang!")

class dosen:
    nama = "Hima"
    dospen = 3
    def __init__(self):
        print("Dengan nama dosen " + self.nama)

class matkul:
    matkul = "Anatomi"
    jam = 10
    def __init__(self):
        print("Kamu mengambil mata kuliah " + self.matkul)

mhs = mahasiswa()
dos = dosen()
matkul = matkul()