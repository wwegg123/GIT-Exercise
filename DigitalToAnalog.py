class DAC:
    def __init__(self, voltage,max_volt = 5, bits = 10):
        try:
            if(0<=voltage and voltage <= max_volt):
                self.voltage = voltage
                self.bits = bits
                self.max_volt = max_volt
            else:
                voltage = input("enter a voltage between 0 and 5 (end values included)")
                self.__init__(voltage,max_volt,bits)
        except ZeroDivisionError:
            self.analong_as_num = 0

    def ToDigital(self):
        self.analong_as_num = self.max_volt/self.voltage
        try:
            options = ""
            for i in range(self.bits):
                options = "1" + options
            options = int(options,2)
            digital = bin(int(options//self.analong_as_num))[2:]
            while len(digital) != self.bits:
                digital = "0" + digital 
        except ZeroDivisionError:
            digital = ""
            for i in range (self.bits):
                digital = "0" + digital
        return digital

    def SetDigitalValue(self,value):
        options = ""
        for i in range(self.bits):
            options = "1" + options
        options = int(options,2)
        mult = int(value,2)
        self.voltage = (self.max_volt/options)*mult

a = DAC(2.5,10,10)
print(a.ToDigital())
a.SetDigitalValue("1011000011")
print(a.voltage)
