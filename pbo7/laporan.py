# buat pogram beisi diagram kelas yang mengandung engkapsulation

class Mobil:
    def __init__(self, jenis, maxSpeed):
        self.__jmlBan = 4
        self.jenisMobil = jenis
        self._maxSpeed = maxSpeed

    def ubahJumlahBan(self, jmlBaru):
        self.__jmlBan = jmlBaru

    def cetakJmlBan(self):
        print("Jumlah ban " + str(self.__jmlBan))

class Sport(Mobil):
    def __init__(self, jenis, maxSpeed):
        super().__init__(jenis, maxSpeed)

    def cetakSpeed(self):
        print("Max speed " + str(self._maxSpeed))

    
class truk(Mobil):
    def __init__(self, jenis, maxSpeed):
        super().__init__(jenis, maxSpeed)



lambo = Sport("Balap", 120)
lambo.cetakSpeed()

tangki = truk("Angkutan Berat", 80)
tangki.ubahJumlahBan(6)
tangki.cetakJmlBan()