import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
transit = 6
led = 26
state = 0
GPIO.setup(led, GPIO.OUT)
GPIO.setup(transit, GPIO.IN)
while True:
    if GPIO.input(transit):
        state = 0
        GPIO.output(led, state)
    else:
        state = 1
        GPIO.output(led, state) 