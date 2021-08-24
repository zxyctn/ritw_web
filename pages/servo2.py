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
    p.ChangeDutyCycle(randrange(0, 100, 1))
    print('First movement')

    p.ChangeDutyCycle(randrange(0, 100, 1))
    print('Second movement')

    p.ChangeDutyCycle(randrange(0, 100, 1))
    print('Third movement')

    p.ChangeDutyCycle(randrange(0, 100, 1))
    print('Last movement')

    print('1 second delay')
    time.sleep(1)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
