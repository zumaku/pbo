# Class declaration
class Pet:
    def __init__(self, nama, umur, lvlkelaparan):
        self.nama = nama
        self.umur = umur
        self.lvlKelaparan = lvlkelaparan


class Kucing(Pet):
    def __init__(self, nama, umur, lvlkelaparan):
        super().__init__(nama, umur, lvlkelaparan) 


class Kelinci(Pet):
    def __init__(self, nama, umur, lvlkelaparan):
        super().__init__( nama, umur, lvlkelaparan)


class Action:
    def makan(self, makanan):
        print("Makanannya: " + makanan + "\n")

    def info(self, lawan):
        print("Nama: " + lawan.nama)
        print("Umur: " + lawan.umur)
        print("Level Kelaparan: " + str(lawan.lvlKelaparan))




# Main
kucing = Kucing("Bimo", "3 Tahun", 12)
kelinci = Kelinci("Biku", "1 Tahun 3 Bulan", 10)


aksiKucing = Action()
aksiKucing.info(kucing)
aksiKucing.makan("Ikan")

aksiKelinci = Action()
aksiKelinci.info(kelinci)
aksiKelinci.makan("Wortel")
