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
wlan.connect('Android', auth=(network.WLAN.WPA2, '12345678'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())