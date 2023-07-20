# masse gpio 6
# signal gpio 7
# commence a avancer vers 7 duty cycle

"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)


p.start(0)
print("Starting 0")
time.sleep(5)

duty_cycle = 3.0

p.ChangeDutyCycle(duty_cycle)
time.sleep(5)

while duty_cycle < 8.0:
    duty_cycle += 0.1
    p.ChangeDutyCycle(duty_cycle)
    print(duty_cycle)
    time.sleep(0.1)

time.sleep(10)



p.stop()
GPIO.cleanup()"""

from gpiozero import Servo
from time import sleep

servo = Servo(12)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)