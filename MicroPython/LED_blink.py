from machine import Pin

# Funkcia sleep zastavi cinnost dosky na cas dany parametrom[sekundy]
from time import sleep

pin_diody = Pin(14, Pin.OUT)

while True:
    # LEDka sa vypne
    pin_diody.value(0)
    # Doska spi pol sekundy
    sleep(.5)
    #  LEDka sa zapne
    pin_diody.value(1)
    # Doska spi pol sekundy
    sleep(.5)
