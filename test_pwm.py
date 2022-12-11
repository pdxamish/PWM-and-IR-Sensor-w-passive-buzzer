from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.freq(500)