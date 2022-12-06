
# Class Induk Mahasiswa
class Mahasiswa:
    def __init__(self):
        self.nim = ""
        self.nama = ""

    def inputMahasiswa(self, nim, nama):
        self.nim = nim
        self.nama = nama


# sub class Reguler
class Reguler(Mahasiswa):
    def __init__(self):
        super().__init__()
        self.biayaDaftarUlang = 0
        self.danaKemahasiswaan = 0
        self.bop = 0

    def entryReguler(self, jmlSks, semester):
        self.jmlSks = jmlSks
        self.semester = semester
        if(jmlSks > 24):
            print("Maksimal 24 SKS")

    def hitungReguler(self, biayaDaftarUlang, danaKemahasiswaan, bop):
        self.biayaDaftarUlang = biayaDaftarUlang
        self.danaKemahasiswaan = danaKemahasiswaan
        self.bop = bop

        self.biayaPerSks = 75000
        self.totalUangSks = self.jmlSks * self.biayaPerSks
        self.totalPembayaran = self.biayaDaftarUlang + self.totalUangSks + self.danaKemahasiswaan + self.bop

        if(self.totalPembayaran >= 4500000):
            self.diskon =  5 / 100
        else:
            self.diskon = 0

        self.totalPembayaranAkhir = self.totalPembayaran - self.diskon

    def cetakReguler(self):
        print("Nama: " + self.nama)
        print("NIM: " + self.nim)
        print("Semester :" + str(self.semester))
        print("Biaya Daftar Ulang :" + str(self.biayaDaftarUlang))
        print("Dana Kemahasiswaan :" + str(self.danaKemahasiswaan))
        print("BOP :" + str(self.bop))
        print("Jumlah SKS :" + str(self.jmlSks))
        print("Total Pembayaran :" + str(self.totalPembayaran))
        print("Diskon :" + str(self.diskon))
        print("Total Pembayaran Akhir :" + str(self.totalPembayaranAkhir))


# sub class Eksekutif
class Eksekutif(Mahasiswa):
    def __init__(self):
        super().__init__()

    def entryEksekutif(self, jmlSks, semester):
        self.jmlSks = jmlSks
        self.semester = semester
        if(jmlSks > 24):
            print("Maksimal 24 SKS")
    
    def hitungEksekutif(self, jmlMatakuliah, danaKemahasiswaan, bop):
        self.jmlMatakuliah = jmlMatakuliah
        self.danaKemahasiswaan = danaKemahasiswaan
        self.bop = bop

        self.biayaPerSks = 85000
        self.biayaUjianPerMatakuliah = 100000
        self.totalUangSks = self.biayaPerSks * self.jmlSks
        self.totalBiayaUjian = self.jmlMatakuliah * self.biayaUjianPerMatakuliah
        self.totalPembayaran = self.bop + self.totalUangSks + self.totalBiayaUjian

        if(self.totalPembayaran >= 4500000):
            self.diskon =  5 / 100
        else:
            self.diskon = 0

        self.totalPembayaranAkhir = self.totalPembayaran - self.diskon

    def cetakEksekutif(self):
        print("Nama: " + self.nama)
        print("NIM: " + self.nim)
        print("Semester :" + str(self.semester))
        print("Jumlah Matakuliah :" + str(self.jmlMatakuliah))
        print("DanaKemahasiswaan :" + str(self.danaKemahasiswaan))
        print("BOP :" + str(self.bop))
        print("Total Biaya Ujian :" + str(self.totalBiayaUjian))
        print("Jumlah SKS :" + str(self.jmlSks))
        print("Total Pembayaran :" + str(self.totalPembayaran))
        print("Diskon :" + str(self.diskon))
        print("Total Pembayaran Akhir :" + str(self.totalPembayaranAkhir))




# fungsi main
R = Reguler()
R.inputMahasiswa("60200121101", "Fadli")
R.entryReguler(23, 4)
R.hitungReguler(500000, 1000000, 5000000)
R.cetakReguler()
print("\n")

E = Eksekutif()
E.inputMahasiswa("60300121022", "Husna")
E.entryEksekutif(23, 4)
E.hitungEksekutif(7, 1500000, 6000000)
E.cetakEksekutif()