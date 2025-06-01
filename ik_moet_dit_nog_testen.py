from machine import Pin
import utime

#variabele
massa = 0.5
K_veer = 100

#meet tijd
tijd_meet = 5

# arrays
Afstand = []
a_sensor = []

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
def ultra():
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
   distance = ((timepassed * 0.0343) / 2) + 0.4
   versnelling = (distance * K_veer)/massa
   print("The distance from object is ",distance,"cm")
   Afstand.append(distance)
   a_sensor.append(versnelling)

while utime < tijd_meet:
   ultra()
   utime.sleep(1)