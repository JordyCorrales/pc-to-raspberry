import RPi.GPIO as GPIO
import time

pin = int(4)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
for x in range(0, 5):
  print("on {}".format(x))
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(1)
  print("off {}".format(x))
  GPIO.output(pin, GPIO.LOW)
GPIO.cleanup()