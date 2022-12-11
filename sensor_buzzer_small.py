from hcsr04 import HCSR04
from time import sleep
from machine import Pin, PWM

sensor = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=10000)
buzzerPIN=15
BuzzerObj = PWM(Pin(buzzerPIN))
led1=Pin(16,Pin.OUT)
led2=Pin(17,Pin.OUT)
led3=Pin(18,Pin.OUT)
led4=Pin(19,Pin.OUT)
led5=Pin(20,Pin.OUT)
led6=Pin(21,Pin.OUT)


def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.1))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)
    

c1 = 30
c2 = 65
c3 = 130
c4 = 260
c5 = 560
c6 = 1046
c7 = 2093
c8 = 4186

while True:
    distance = sensor.distance_cm()      ####mm()
    print('Distance:', distance, 'cm')
    if distance > 60:
        buzzer(BuzzerObj,c1,0.5,0.1)
    elif distance > 45:
        buzzer(BuzzerObj,c2,0.5,0.1)
    elif distance > 30:
        buzzer(BuzzerObj,c3,0.5,0.1)
    elif distance > 22:
        buzzer(BuzzerObj,c4,0.5,0.1)
    elif distance > 17:
        buzzer(BuzzerObj,c5,0.5,0.1)
    elif distance > 12:
        buzzer(BuzzerObj,c6,0.5,0.1)
    elif distance > 8:
        buzzer(BuzzerObj,c7,0.5,0.1)
    elif distance > 5:
        buzzer(BuzzerObj,c8,0.5,0.1)
    sleep(.2)
    
