class Hewan:
    def __init__(self, ukuran):
        self.ukuran = ukuran

    def tampilHewan(self):
        self.jenis = "Buas"
        print(self.jenis)

class Harimau(Hewan):
    def __init__(self, ukuran):
        super().__init__(ukuran)

    # overriding
    def tampilHewan(self):
        return super().tampilHewan()

class Kucing(Hewan):
    def __init__(self, ukuran):
        super().__init__(ukuran)

    # overiding
    def tampilHewan(self):
        self.jenis = "Peliharaan"
        print(self.jenis)

harimau = Harimau("besar")
harimau.tampilHewan()

kucing = Kucing("kecil")
kucing.tampilHewan()


