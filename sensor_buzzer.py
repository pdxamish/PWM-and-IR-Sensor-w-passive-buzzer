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
    
gy9=13290
g9=12544
fy9=11840
f9=11175
e9=10548
dy9=9956
d9=9397
cy9=8870
c9=8372
b8=7902
ay8=7459
a8=7040
gy8=6645
g8=6272
fy8=5920
f8=5588
e8=5274
dy8=4978
d8=4699
cy8=4435
c8=4186
b7=3951
ay7=3729
a7=3520
gy7=3322
g7=3136
fy7=2960
f7=2794
e7=2637
dy7=2489
d7=2349
cy7=2217
c7=2093
b6=1976
ay6=1865
a6=1760
gy6=1661
g6=1568
fy6=1480
f6=1397
e6=1319
dy6=1245
d6=1175
cy6=1109
c6=1047
b5=988
ay5=932
a5=880
gy5=831
g5=784
fy5=740
f5=698
e5=659
dy5=622
d5=587
cy5=554
c5=523
b4=494
ay4=466
a4 =440
gy4=415
g4=392
fy4=370
f4=349
e4=330
dy4=311
d4=294
cy4=277
c4 =262
b3=247
ay3=233
a3=220
gy3=208
g3=196
fy3=185
f3=175
e3=165
dy3=156
d3=147
cy3=139
c3=131
b2=123
ay2=117
a2=110
gy2=104
g2=98
fy2=93
f2=87
e2=82
dy2=78
d2=73
cy2=69
c2=65
b1=62
ay1=58
a1=55
gy1=52
g1=49
fy1=46
f1=44
e1=41
dy1=39
d1=37
cy1=35
c1=33
b0=31
ay0=29
a0=28

while True:
    distance = sensor.distance_cm()      ####mm()
    print('Distance:', distance, 'cm')
    if distance > 166:
        buzzer(BuzzerObj,c1,0.5,0.1)
    elif distance > 160:
        buzzer(BuzzerObj,d1,0.5,0.1)
    elif distance > 155:
        buzzer(BuzzerObj,e1,0.5,0.1)
    elif distance > 150:
        buzzer(BuzzerObj,f1,0.5,0.1)
    elif distance > 145:
        buzzer(BuzzerObj,g1,0.5,0.1)
    elif distance > 140:
        buzzer(BuzzerObj,a1,0.5,0.1)
    elif distance > 135:
        buzzer(BuzzerObj,b1,0.5,0.1)
    elif distance > 130:
        buzzer(BuzzerObj,c2,0.5,0.1)
    elif distance > 125:
        buzzer(BuzzerObj,d2,0.5,0.1)
    elif distance > 120:
        buzzer(BuzzerObj,e2,0.5,0.1)
    elif distance > 115:
        buzzer(BuzzerObj,f2,0.5,0.1)
    elif distance > 110:
        buzzer(BuzzerObj,g2,0.5,0.1)
    elif distance > 105:
        buzzer(BuzzerObj,a2,0.5,0.1)
    elif distance > 100:
        buzzer(BuzzerObj,b2,0.5,0.1)
    elif distance > 95:
        buzzer(BuzzerObj,c3,0.5,0.1)
    elif distance > 90:
        buzzer(BuzzerObj,d3,0.5,0.1)
    elif distance > 85:
        buzzer(BuzzerObj,e3,0.5,0.1)
    elif distance > 80:
        buzzer(BuzzerObj,f3,0.5,0.1)
    elif distance > 75:
        buzzer(BuzzerObj,g3,0.5,0.1)
    elif distance > 70:
        buzzer(BuzzerObj,a3,0.5,0.1)
    elif distance > 65:
        buzzer(BuzzerObj,b3,0.5,0.1)
    elif distance > 60:
        buzzer(BuzzerObj,c4,0.5,0.1)
    elif distance > 58:
        buzzer(BuzzerObj,d4,0.5,0.1)
    elif distance > 56:
        buzzer(BuzzerObj,e4,0.5,0.1)
    elif distance > 54:
        buzzer(BuzzerObj,f4,0.5,0.1)
    elif distance > 52:
        buzzer(BuzzerObj,g4,0.5,0.1)
    elif distance > 50:
        buzzer(BuzzerObj,a4,0.5,0.1)
    elif distance > 47:
        buzzer(BuzzerObj,b4,0.5,0.1)
    elif distance > 44:
        buzzer(BuzzerObj,c5,0.5,0.1)
    elif distance > 42:
        buzzer(BuzzerObj,d5,0.5,0.1)
    elif distance > 40:
        buzzer(BuzzerObj,e5,0.5,0.1)
    elif distance > 38:
        buzzer(BuzzerObj,f5,0.5,0.1)
    elif distance > 36:
        buzzer(BuzzerObj,g5,0.5,0.1)
    elif distance > 34:
        buzzer(BuzzerObj,a5,0.5,0.1)
    elif distance > 32:
        buzzer(BuzzerObj,b5,0.5,0.1)
    elif distance > 30:
        buzzer(BuzzerObj,c6,0.5,0.1)
    elif distance > 28:
        buzzer(BuzzerObj,d6,0.5,0.1)
    elif distance > 26:
        buzzer(BuzzerObj,e6,0.5,0.1)
    elif distance > 24:
        buzzer(BuzzerObj,f6,0.5,0.1)
    elif distance > 22:
        buzzer(BuzzerObj,g6,0.5,0.1)
    elif distance > 20:
        buzzer(BuzzerObj,a6,0.5,0.1)
    elif distance > 18:
        buzzer(BuzzerObj,b6,0.5,0.1)
    elif distance > 16:
        buzzer(BuzzerObj,c7,0.5,0.1)
    elif distance > 14:
        buzzer(BuzzerObj,d7,0.5,0.1)
    elif distance > 12:
        buzzer(BuzzerObj,e7,0.5,0.1)
    elif distance > 10:
        buzzer(BuzzerObj,f7,0.5,0.1)
    elif distance > 9 :
        buzzer(BuzzerObj,g7,0.5,0.1)
    elif distance > 8:
        buzzer(BuzzerObj,a7,0.5,0.1)
    elif distance > 7:
        buzzer(BuzzerObj,b7,0.5,0.1)
    elif distance > 6:
        buzzer(BuzzerObj,c8,0.5,0.1)
    elif distance > 5:
        buzzer(BuzzerObj,d8,0.5,0.1)
    elif distance > 4:
        buzzer(BuzzerObj,e8,0.5,0.1)
    elif distance > 3:
        buzzer(BuzzerObj,f8,0.5,0.1)
    elif distance > 2:
        buzzer(BuzzerObj,g8,0.5,0.1)
    elif distance > 1:
        buzzer(BuzzerObj,a8,0.5,0.1)
    elif distance > .5:
        buzzer(BuzzerObj,b8,0.5,0.1)
    
    
