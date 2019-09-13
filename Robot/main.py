import time
from machine import I2C
# Import ServoCtrl, classe pour le controleur PMW
from servoctrl import ServoCtrl

# Initialise le bus I2C
i2c = I2C( 0, pins=('P9','P10') )

# Crée l'objet pour controleur PWM.
# Utilise l'adresse par défaut du contrôleur 0x40
driver = ServoCtrl( i2c )

# Passer d'un angle de 10 à 170° par pas de 10 degrés
for i in range( 1, 18 ):                                                    
     driver.position( 15, i*10 )                                             
     time.sleep( 1 ) # Attendre une seconde