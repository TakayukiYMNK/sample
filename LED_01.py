import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
do = 39
re = 37
mi = 35
fa = 33
so = 31
ra = 29
si = 27
do2 = 25
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)
try:
    while 1:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
