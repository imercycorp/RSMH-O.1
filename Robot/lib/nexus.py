from machine import I2C
from servoctrl import ServoCtrl

class Nexus:
    
    def __init__(self, pin):
        try:
            self.pin = pin
            self.nexus_init = I2C(self.pin, I2C.MASTER)
            self.driver = ServoCtrl(self.nexus_init)
        except:
            print("[NEXUS] Erreur : Impossible de ce connecter au port I2C '" + self.pin + "'")
    
    def move(self, id_s, pos):
        self.id = id_s
        self.pos = pos
        try: 
            self.driver.position(self.id, self.pos)
            return "OK : Action effectue"
        except:
            return "[NEXUS] Erreur : Communication impossible avec '" + self.id + "'"