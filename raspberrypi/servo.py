import RPi.GPIO as GPIO
import time

servoPIN = 17
servo2PIN = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servo2PIN, 50)
p.start(2.5) # Initialization
p2.start(2.5)

def retrieveData():
  data = dataqueue.getServoQueue()
  if (data != "empty"):
      print("Motor prints: " + data)

def servoStartListening():
  try:
    while True:
      retrieveData()

      time.sleep(0.2)
      p.ChangeDutyCycle(2.5)
      p2.ChangeDutyCycle(2.5)
      time.sleep(0.2)
      p.ChangeDutyCycle(7.5)
      p2.ChangeDutyCycle(7.5)
      time.sleep(0.2)
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

if __name__ == '__main__':
  servoStartListening()
