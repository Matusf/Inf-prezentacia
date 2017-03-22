from machine import Pin
from neopixel import NeoPixel
from time import sleep

POCET_LED = 8
led_pasik = NeoPixel(Pin(4), POCET_LED)

for led in range(POCET_LED):
    led_pasik[led] = (186, 218, 85)
    sleep(1)
    led_pasik.write()

for led in range(POCET_LED-1, -1, -1):
    led_pasik[led] = (0, 0, 0)
    sleep(1)
    led_pasik.write()
