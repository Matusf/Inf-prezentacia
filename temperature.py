from onewire import OneWire
from machine import Pin
from ds18x20 import DS18X20
from time import sleep

one_wire_pin = DS18X20(OneWire(Pin(2)))

# Získame adresy všetkých teplomer pripojených k pinu (funkcia vracia list)
ds18b20_zariadenia = one_wire_pin.scan()
print("Počet nájdených nájdených teplomerov:", len(ds18b20_zariadenia))

while True:
   # Inicializuje sa citanie teploty
   one_wire_pin.convert_temp()
   # musíme počkať aspoň 750 ms
   sleep(.75)

   print('Prečítané teploty:', end=' ')

   for adresa in ds18b20_zariadenia:
      print(one_wire_pin.read_temp(adresa), end = ' ')
   print()
