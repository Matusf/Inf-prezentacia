from machine import Pin
from neopixel import NeoPixel

POCET_LED = 8
led_pasik = NeoPixel(Pin(4), POCET_LED)

led_pasik[0] = (255, 0, 0) # set to red, full brightness
led_pasik[1] = (0, 128, 0) # set to green, half brightness
led_pasik[2] = (0, 0, 64)  # set to blue, quarter brightness

led_pasik.write()
