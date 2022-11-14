"""
Soal laporan 4

1. Buatlah class User dengan method
    a. printUsername
    b. printShowPassword
    atribut class User : username dan password
2. Buat class Mahasiswa dengan method
    a. printNIM
    b. printSemester
    atribut class Mahasiswa : nim dan semester
"""

# class User
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def printUsername(self):
        print("Username: " + self.username)

    def printShowPassword(self):
        print("Password: " + self.password)

# class Mahasiswa
class Mahasiswa(User):
    def __init__(self, username, password, nim, semester):
        super().__init__(username, password)
        self.nim = nim
        self.semester = semester
    
    def printNim(self):
        print("Nim: " + str(self.nim))

    def printSemester(self):
        print("Semester: " + str(self.semester))


# instence object
fadli = Mahasiswa("Zul Fadli", "Buahahaha", 60200121101, 3)
fadli.printUsername()
fadli.printShowPassword()
fadli.printNim()
fadli.printSemester()