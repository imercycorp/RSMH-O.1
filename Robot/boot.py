# boot.py -- run on boot-up
import os
from machine import UART
import network
import time

#OS
uart = UART(0, 115200)
os.dupterm(uart)

# WiFi
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('Livebox-81C0', auth=(network.WLAN.WPA2, 'hjSxdW6szteD5WAZgu'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())