'''
Asistensi Laporan 4
1. Buat class kota dengan atribut totalOrang dan method info yang menampilkan totalOrang.
2. Buat class orang yang inherit dari class kota dengan atribut nama dan nik dengan method info yang menampilkan nama, nik, dan totalOrang.
*setiap pembuatan objek, totalOrang akan bertambah satu.
'''

class kota:
    totalOrang = 0
    def __init__(self):
        kota.totalOrang += 1

    def info(self):
        print("Total Orang: " + str(self.totalOrang))

class orang(kota):
    def __init__(self, nama, nik):
        super().__init__()
        self.nama = nama
        self.nik = nik

    def info(self):
        print("Nama: " + self.nama)
        print("NIK: " + str(self.nik))
        super().info()

tes = orang("Zuma", 101)
tes.info()
# imang = orang("Iman", 103)

