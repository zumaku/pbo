# class bangun datar
class BangunDatar:
    def __init__(self, luas):
        self.luas = luas

    def showLuas(self):
        print("Luas : ", self.luas)

# class persegi
class Persegi(BangunDatar):                         #inheritance di python, class parent diletakkan di dalam paratmeter class child
    def __init__(self, sisi):
        self.sisi = sisi
        super().__init__(self.sisi*4)               #super() ini mengakses constructor di class parent. Jadi.. self.sisi*4   itu menjadi parameter untuk constructor di class BangunDatar

    def infoLengkap(self):
        self.showLuas()                             #memanggil method yang ada di parent
        print("Sisi : ", self.sisi)

    def showLuas(self):                             #Ini adalah Overreading.
        print("Show luas baru")
        super().showLuas()


# calss segi tiga
class segiTiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.luas = int((alas*tinggi)/2)
        super().__init__(self.luas)

    def showLuas(self):                             #Ini adalah Overreading.
        print("Show luas Segitiga")
        super().showLuas()



persegi1 = Persegi(40)
persegi1.infoLengkap()
persegi1.showLuas()

segitiga = segiTiga(20, 20)
segitiga.showLuas()


# Istilah
# ==> Overreading. Ialah suatu istilah pada inheritance dimana methot atau property class parent didefenisikan kembali di class childnya, dan itu bisa dengan nilai berbeda. Ini biasa digunakan jika ingin menambahkan atau mengubah sesuatu yang berbeda untuk kelas tersebut, tapi masih menggunakan method atau property yang sama dengan parennya. Ini tidak berpengaruh pada method atau property aslinya di parent.
# ==> Overloading. Ialah sebiah method yang bisa membuat dua atau lebih method dengan nama yang sama dalam sebuah class, namun tipe dan jumlah argumentnya berbeda satu sama lain. Ini tidak ada kaitannya dengan parentnya. Sayangnya di Python tidak mendukung overloading ini