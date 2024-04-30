# Light Dependent Resistor


# https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

for i in range(0,5):
    print GPIO.input(4)





# https://projects.raspberrypi.org/en/projects/physical-computing/10

from gpiozero import LightSensor, Buzzer

ldr = LightSensor(4)  # alter if using a different pin
while True:
    print(ldr.value)
