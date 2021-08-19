import RPi.GPIO as GPIO
import time
from random import randrange

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization
try:
  while True:
    p.ChangeDutyCycle(randrange(0, 0.87, 0.01))
    time.sleep(randrange(500, 1000, 1)/1000)
    p.ChangeDutyCycle(randrange(0, 0.87, 0.01))
    time.sleep(randrange(500, 1000, 1)/1000)
    p.ChangeDutyCycle(randrange(0, 0.87, 0.01))
    time.sleep(randrange(500, 1000, 1)/1000)
    p.ChangeDutyCycle(randrange(0, 0.87, 0.01))
    time.sleep(randrange(500, 1000, 1)/1000)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
