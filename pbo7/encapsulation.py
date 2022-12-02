# ENGCAPSULATION

# Public Modifier       ex: property            Dapat diakses di semua kelas
# Protected Modifier    ex: _Property           Dapat diakses di dalam kelas dan sub kelasnya, tapi tidak bisa diakses di luar kelas.
# Private Modifier      ex: __property          Hanya dapat diakses di dalam kelasnya saja, tapi tidak bisa diakses di sub kelas dan di luar kelas tersebut.

class Component:
    def __init__(self, enable, background, border):
        self.enable = enable
        self.__background = background          # private
        self._border = border                   # protected

    def getBg(self):                            # fungsi untuk mengakses private background
        print(self.__background)

    def ubahBg(self, bg):                       # fungsi untuk mengubah private background
        self.__background = bg

class Button(Component):
    def _init_(self, enable, background):
        super()._init_(enable, background)

    def getBorder(self):                        # fungsi untuk mengakses protected border
        print(self._border)

    def ubahBorder(self, border):               # fungsi untuk mengubah protected border
        self._border = border


button = Button(True, "White", "Black")

print(button.enable)

button.getBg()              # memanggil bg
button.ubahBg("Green")      # mengubah bg
button.getBg()              # mengambil bg

button.getBorder()          # memanggil border
button.ubahBorder("Grey")   # mengubah bg
button.getBorder()          # memanggil bg

# print(button.__background)