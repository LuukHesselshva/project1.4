from machine import Pin
import utime
import os

#csv naam
file_name = 'test.csv'
#pauze
pause = 0.1

#variabele
massa = 0.5
K_veer = 100
d0 = 0

#tijd
tijd_meet = 5
t0 = utime.ticks_ms()
run = True

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
def ultra():
# meten met de sensor
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
# berekeningen 
   distance = (((timepassed * 0.0343) / 2) + 0.4) - d0
   versnelling = ((distance/100) * K_veer)/massa
   tijd_run = (utime.ticks_ms()-t0)/1000
# print gegevens   
   print(tijd_run,"s",distance,"cm",distance,"m/s^2")
# Check if CSV file exists, if not create it with header
   if not file_name in os.listdir():
     with open(file_name, 'w') as file:
       file.write('tijd,uitwijking,versnelling\n')
# Append temperature data to CSV file
   with open(file_name, 'a') as file:
           file.write('{},{},{}\n'.format(tijd_run,distance, versnelling))
   if tijd_run < tijd_meet:
      return True
   elif tijd_run > tijd_meet:
      return False
while run == True:
   run = ultra()
   utime.sleep(pause)