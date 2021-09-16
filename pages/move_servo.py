import RPi.GPIO as GPIO
import time
from random import randrange

servoPIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(0) 

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

def move_servo_pi():
    SetAngle(randrange(0, 100, 1))
    print('First movement')

    SetAngle(randrange(0, 100, 1))
    print('Second movement')

    SetAngle(randrange(0, 100, 1))
    print('Third movement')

    SetAngle(randrange(0, 100, 1))
    print('Last movement')

    print('1 second delay')
    time.sleep(1)