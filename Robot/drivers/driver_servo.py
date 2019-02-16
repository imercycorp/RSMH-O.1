class Servo:
    
    clockRate = 120
    def __init__(self, nexus, addr, angle):
        self.nexus = nexus
        self.addr = addr
        self.angle = angle

    def write(self):
        self.nexus.writeto(self.addr, bytes([self.angle]))