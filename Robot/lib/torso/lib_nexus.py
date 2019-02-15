from machine import I2C

def Nexus_Init(pin_master, hz):
    nexus = I2C(pin_master, pin('P9','P10'))
    nexus.init(I2C.MASTER, baudrate=hz)
    return nexus

    #nexus.deinit()

def Nexus_Scan(nexus, nb_servo):
    nexus_list = nexus.scan()
    return List_select(nexus_list, nb_servo)


#pouet = Nexus_Init(0, 9600)
#pouet2 = Nexus_Scan(pouet)