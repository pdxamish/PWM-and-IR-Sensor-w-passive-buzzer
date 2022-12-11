# PWM-and-Ultra -Sonic-Sensor-w-passive-buzzer on Pi Pico
Using Pi Pico to "play" different notes depending on where my hand is to the board. HC-SR04 IR Sensor, passive buzzerUsing Micropython

Kinda fun project to get to know the Pi Pico.  I was at first using the IR Sensor and passive bizzer with different feequencies but decided to use them together.  I will input the text file with all of the frequency and notes/octives is saved.  You can you also save the notes as a dictionary or Tuple but this was easiest since I just concatenatated it in excel. Make sure you have a passive not an active buzzer and we are using 3.3v.

The files include very basic Micropython code that helps with both the IR Sensor and the active buzzer playing "music"  I included the pokemon one just for reference as it sounds nothing like the song.  Please use and add and give me suggestions

This is a poor man's Theremin but if someone wanted to mess with it a little more it would not be that difficult. There is the ability to use more inouts and outputs pins to get different effect.  Using the Pico makes it portable and easy to prototype.  Onlinesequencer.net is a good place to get Midi notes of songs.  There is a way to convert the audio on there into something usable Micropython code but I didn't get it to work and moved on

My Ceiling was 165 cm and the IR Sensor has a max distance of 250 cm.  I am sure there is an easier way than doing a bunch of if else statements and would love to hear it since it was kinda annoying and long types out


