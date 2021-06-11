import RPi.GPIO as GPIO
import time


pin = int(4)
i = int(0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

while i > 5:
  print("on")
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(1)
  print("off")
  GPIO.output(pin, GPIO.LOW)
  i += 1

GPIO.cleanup()