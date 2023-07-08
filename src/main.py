import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

duty_cycle = 0.0

p.start(duty_cycle)

while duty_cycle < 10.0:
    duty_cycle += 0.1
    p.ChangeDutyCycle(duty_cycle)
    print(duty_cycle)
    time.sleep(0.1)

while duty_cycle > 0.0:
    duty_cycle -= 0.1
    p.ChangeDutyCycle(duty_cycle)
    print(duty_cycle)
    time.sleep(0.1)

p.stop()
GPIO.cleanup()