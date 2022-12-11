#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Oct 6th, 2021
# Version: 1.0

from machine import Pin, PWM
from time import sleep

buzzerPIN=15
BuzzerObj = PWM(Pin(buzzerPIN))

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


#set translation table from note to frequency
c6= 1047
f5 = 698
e5 = 659
a5 = 880
g5 = 783
fs3= 184


buzzer(BuzzerObj,c6,0.25,0.1)
buzzer(BuzzerObj,a5,.25,0.1)
buzzer(BuzzerObj,g5,.25,0.1)
buzzer(BuzzerObj,c6,0.25,0.1)
buzzer(BuzzerObj,f5,0.25,0.1)
buzzer(BuzzerObj,f5,0.25,0.1)
buzzer(BuzzerObj,f5,0.25,0.1)
buzzer(BuzzerObj,e5,0.25,0.1)
buzzer(BuzzerObj,f5,0.25,0.1)
buzzer(BuzzerObj,e5,1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)
buzzer(BuzzerObj,fs3,.1,0.1)





#Deactivates the buzzer
BuzzerObj.deinit()
