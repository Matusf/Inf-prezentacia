from machine import Pin

pin_diody = Pin(14, Pin.OUT)
pin_tlacitka = Pin(0, Pin.IN)

# Pyta sa na hodnotu z tlacitka a podla nej nastavuje LEDku
while True:
   pin_diody.value(pin_tlacitka.value())
