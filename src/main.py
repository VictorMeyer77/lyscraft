# masse gpio 6
# signal gpio 7
# commence a avancer vers 7 duty cycle

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)


p.start(0)
print("Starting 0")
time.sleep(5)

duty_cycle = 3.0

p.ChangeDutyCycle(duty_cycle)
time.sleep(5)


while duty_cycle < 10.0:
    duty_cycle += 0.1
    p.ChangeDutyCycle(duty_cycle)
    print(duty_cycle)
    time.sleep(0.1)

time.sleep(2)

while duty_cycle > 0.1:
    duty_cycle -= 0.1
    p.ChangeDutyCycle(duty_cycle)
    print(duty_cycle)
    time.sleep(0.1)

p.stop()
GPIO.cleanup()