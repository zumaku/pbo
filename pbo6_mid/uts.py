# UTS
# Program Konversi Suhu
# Dibuat oleh Zul Fadli Ahmad
# NIM 60200121101
# Kelas B

class Temperatur:
    value = 0
    convertedValue = 0

    def __init__(self, value):
        self.value = value;

    def getValue(self):
        return self.value

    def getConvertValue(self):
        return self.convertedValue


class Celcius(Temperatur):
    def __init__(self, value):
        super().__init__(value)

    def convertToReamur(self):
        self.convertedValue = (4/5) * self.value
        
    def convertToKelvin(self):
        self.convertedValue = self.value + 273

    def convertToFarenheit(self):
        self.convertedValue = ((9/5) * self.value) + 32


class Kelvin(Temperatur):
    def __init__(self, value):
        super().__init__(value)
    
    def convertToCelcius(self):
        self.convertedValue = self.value - 273

    def convertToReamur(self):
        self.convertedValue = (4/5) * (self.value - 273)
        
    def convertToFarenheit(self):
        self.convertedValue = (9/5) * (self.value - 273) + 32


class Farenheit(Temperatur):
    def __init__(self, value):
        super().__init__(value)

    def convertToCelcius(self):
        self.convertedValue = (5/9) * (self.value - 32)
    
    def convertToReamur(self):
        self.convertedValue = (4/9) * (self.value - 32)
        
    def convertToKelvin(self):
        self.convertedValue = (5/9) * (self.value - 32) + 273


class Reamur(Temperatur):
    def __init__(self, value):
        super().__init__(value)
    
    def convertToCelcius(self):
        self.convertedValue = (5/4) * self.value
    
    def convertToFarenheit(self):
        self.convertedValue = ((9/4) * self.value) + 32

    def convertToKelvin(self):
        self.convertedValue = ((5/4) * self.value) + 273




celcius1 = Celcius(34)
celcius1.convertToFarenheit()
print(str(celcius1.getValue()) + " C\t=  " + str(celcius1.getConvertValue()) + " F")

kelvin1 = Kelvin(200)
kelvin1.convertToCelcius()
print(str(kelvin1.getValue()) + " K\t=  " + str(kelvin1.getConvertValue()) + " C")