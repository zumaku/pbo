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

    def info(self, nama, umur, lvlkelaparan):
        print("Nama: " + nama)
        print("Umur: " + umur)
        print("Level Kelaparan: " + str(lvlkelaparan))





# Main
kucing = Kucing("Bimo", "3 Tahun", 12)
kelinci = Kelinci("Biku", "1 Tahun 3 Bulan", 10)


aksiKucing = Action()
aksiKelinci = Action()

aksiKucing.info(kucing.nama, kucing.umur, kucing.lvlKelaparan)
aksiKucing.makan("Ikan")

aksiKelinci.info(kelinci.nama, kelinci.umur, kelinci.lvlKelaparan)
aksiKelinci.makan("Wortel")
