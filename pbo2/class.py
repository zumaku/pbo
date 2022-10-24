class Mahasiswa:
    nama = "Zuma"
    kelas = 'B'
    def __init__(self):
        print("Hai " + self.nama + ", Selamat Datang!")
    def cetakKelas(self):
        print("Kamu sekarang berada di kelas " + self.kelas)

zuma = Mahasiswa()
zuma.cetakKelas()