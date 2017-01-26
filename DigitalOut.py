from machine import Pin
pin_diody = Pin(14, Pin.OUT)

# Nastavenie hodnoty
pin_diody.value(0)
pin_diody.value(1)
# Vypis hodnoty
print(pin_diody.value())
