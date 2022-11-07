class Car:
    _wheal = 4
    _type = " "
    _merk = " "
    _owner = " "
    color = " "
    
    def get_owner(self):
        return self._owner;
    
    def __init__(self, owner = "unknow", color = "green", merk = "unknow", types = "Sport Car", wheeldrive = 4): #untuk instense atau objek
        self._owner = owner
        self.color = color
        self._merk = merk
        self._type = types
        self._wheeldrive = wheeldrive
        
    def start_engine(self):
        print("Starting the car... ")
        print("owner: %s" % self._owner)
        print("color: %s" % self.color)
        print("merk: %s" % self._merk)
        print("type: %s" % self._type)
        print("wheeldrive: %s" % self._wheeldrive)
        
car = Car(wheeldrive = 8)
car2 = Car(owner = "Zuma", color = "red", merk = "Suzuku", types = "City Car")

car.start_engine()
car2.start_engine()
owner = car.get_owner()
owner = car2.get_owner()