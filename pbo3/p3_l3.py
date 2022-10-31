class pelajar:
    nip = 0
    nama = "unknow"
    nilaiUjian1 = 0
    nilaiUjian2 = 0
    nilaiTugas = 0
    
    def nilaiAkhir(self):
        na = (self.nilaiUjian1 * 35 / 100) + (self.nilaiUjian2 * 40 / 100) + (self.nilaiTugas * 25 /100)
        print(
        "Data Pelajar: \n" +
        "NIP: " + str(self.nip) + "\n" +
        "Nama" + self.nama + "\n" +
        "N. Ujian 1: " + str(self.nilaiUjian1) + "\n" +
        "N. Ujian 2: " + str(self.nilaiUjian2) + "\n" +
        "N. Tugas: " + str(self.nilaiTugas) + "\n" +
        "N. Rata2 Ujian: " + str(na/2)
        )
        self.isLulus(na)
        
    def isLulus(self, na):
        status ="unknow"
        if(na>=60):
            status="Lulus"
        else:
            status="Tidak Lulus"
        print("Nilai akhir: " + str(na))
        self.status(status)
            
    def status(self, status):
        print("Status: " + status)
        
#instansiasi objek
zuma = pelajar()
zuma.nip=101
zuma.nama="Zul Fadli Ahmad"
zuma.nilaiUjian1=80
zuma.nilaiUjian2=89
zuma.nilaiTugas=85
zuma.nilaiAkhir()