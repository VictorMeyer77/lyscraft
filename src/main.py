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

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(0)
print("Starting 0")
time.sleep(5)

p.ChangeDutyCycle(3)
print("3")
time.sleep(5)

ii = 4
steps = [6, 7, 8]
current_step = -1


def increase(i, target):
    while i < target:
        print(i)
        p.ChangeDutyCycle(i)
        time.sleep(0.05)
        i += 0.02


def decrease(i, target):
    while i > target:
        print(i)
        p.ChangeDutyCycle(i)
        time.sleep(0.05)
        i -= 0.02


while True:
    s = input("commnd")
    print(s)
    if s == "a" and current_step < 3:
        current_step += 1
        increase(ii, steps[current_step])
        ii = steps[current_step]
    elif s == "z" and current_step > 0:
        current_step -= 1
        decrease(ii, steps[current_step])
        ii = steps[current_step]
    elif s == "p":
        break