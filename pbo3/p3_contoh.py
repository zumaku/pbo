class mahasiswa:
    kampus = "STMIK AKAKOM"
    jurusan = " Komputerasi Akuntansi"
    mataKuliah = "--kosong--"
    status = "--kosong--"
    
    def belajar(self, mk="none", st="none"):
        self.mataKuliah = mk
        self.status = st
        
scoobydoo = mahasiswa()
print(scoobydoo.mataKuliah)
print(scoobydoo.status)

spongebob = mahasiswa()
spongebob.belajar("Sistem Jnformasi Akuntansi", "Paham")
print(spongebob.mataKuliah)
print(spongebob.status)