class person:
    #nama = "unknow"
    #umur = 0
    def __init__ (self):
        self.nama = "Zuma"
        self.umur = 0
    def setNama(self, nama="Pakdiya"):
        self.nama=nama
    def getNama(self):
        return self.nama
  
person1 = person()
print(person1.getNama())
person1.setNama()
print(person1.getNama())