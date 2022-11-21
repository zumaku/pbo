# Buatlah studi kasus OOP dengan membuat 3 Class yang berbeda dan buatlah setiap class memanggil class yang lainnya dan gunakan Polymorphism dan Inheritance.

# parent class
class Mobil:
    def __init__(self, warna):
        self.warna = warna

    def showJenis(self):
        self.jenis = "Normal"
        return "Tipe Mobil " + self.jenis

# class mobil normal, child dari class Mobil
class Normal(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    # overriding
    def showJenis(self):
        return super().showJenis()

# class mobil sport, child class Mobil
class Sport(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    # overiding
    def showJenis(self):
        self.jenis = "Sport"
        return "Tipe Mobil " + self.jenis

# class mobil truk, child class Mobil
class Truk(Mobil):
    def __init__(self, warna):
        super().__init__(warna)

    # overriding
    def showJenis(self):
        self.jenis = "Truk"
        return "Tipe Mobil " + self.jenis


# instansiasi objek
sedan = Normal("Putih")
print("Sedan " + sedan.showJenis())

lambo = Sport("Merah")
print("Lambo " + lambo.showJenis())

tangki = Truk("Hitam")
print("Tangki " + tangki.showJenis())

# may video link https://www.youtube.com/watch?v=X6wXbLBfHAM