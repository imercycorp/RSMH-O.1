from machine import I2C
from lib_list import List

class Nexus:
    
    def Init(self, pin_master, hz):
        self.nexus = I2C(pin_master, pin('P9','P10')) #SDA = P9 CLK = P10
        self.nexus.init(I2C.MASTER, baudrate=hz)
        return self.nexus

    def Scan(self, nexus, nb_servo):
        self.nexus_scan_list = nexus.scan()
        return List.select(self.nexus_list, nb_servo)

    def GetList(self, nexus):
        self.nexus_list = nexus.scan()
        return self.nexus_list

#pouet = Nexus_Init(0, 9600)
#pouet2 = Nexus_Scan(pouet)