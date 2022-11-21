# membuat kelas mobil sebagai parent
class Mobil:
    def __init__(self, warna):
        self.warna = warna

    # method showJenis untuk overreading nantinya
    def showJenis(self):
        self.jenis = "Biasa"
        return "Tipe Mobil " + self.jenis




# class sedan, child dari mobil
class Normal(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    def showJenis(self):
        return "Tipe Mobil " + super().showJenis()




# class lambo, child dari mobil
class Sport(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    # overreading
    def showJenis(self):
        self.jenis = "Sport"
        return "Tipe Mobil " + self.jenis




# calss truck, child dari mobil
class Truk(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    # overread
    def showJenis(self):
        self.jenis = "Truk"
        return "Tipe Mobil " + self.jenis





# instansi objek
sedan = Normal("Putih")
print("Warna Mobil " + sedan.warna)
print(sedan.showJenis())

lambo = Sport("Merah")
print("Warna Mobil " + lambo.warna)
print(lambo.showJenis())
