from machine import Pin, PWM
from time import sleep

pin_diody = Pin(14, Pin.OUT)

# 50 krat za sekundu blikne
# S polovicnou intenzitou [max je 1024]
pwm = PWM(pin_diody, freq=50, duty=512)

# pwm.deinit() Zastavi blikanie
