class DAC:
    def __init__(self, voltage):
        try:
            if(0<=voltage and voltage <=5):
                self.voltage = voltage
            else:
                voltage = input("enter a voltage between 0 and 5 (end values included)")
                self.__init__(voltage)
        except ZeroDivisionError:
            self.analong_as_num = 0

    def ToDigital(self):
        self.analong_as_num = 5/self.voltage
        try:
            digital = bin(int(1023//self.analong_as_num))[2:]
            while len(digital) != 10:
                digital = "0" + digital 
        except ZeroDivisionError:
            digital = "0000000000"
        return digital

    def SetDigitalValue(self,value):
        mult = int(value,2)
        self.voltage = (5/1023)*mult

a = DAC(2.5)
print(a.ToDigital())
a.SetDigitalValue("1000111011")
print(a.voltage)