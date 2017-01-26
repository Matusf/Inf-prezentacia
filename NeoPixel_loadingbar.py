from machine import Pin
from neopixel import NeoPixel
from time import sleep

POCET_LED = 8
led_pasik = NeoPixel(Pin(4), POCET_LED)

for led in range(POCET_LED):
    led_pasik[led] = (156, 188, 55)
    sleep(1)
    led_pasik.write()
