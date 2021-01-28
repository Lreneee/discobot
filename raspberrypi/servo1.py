import RPi.GPIO as GPIO
import time
import dataqueue

servoPIN = 22
servoPIN2 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p2 = GPIO.PWM(servoPIN2, 50)
p.start(0)
p2.start(0)
musicGenre = "background" 


def setAngle(angle):
  duty = angle/18+2
  GPIO.output(servoPIN, True)
  GPIO.output(servoPIN2, True)
  p.ChangeDutyCycle(duty)
  p2.ChangeDutyCycle(duty)
  time.sleep(1)
  GPIO.output(servoPIN, False)
  GPIO.output(servoPIN2, False)
  p.ChangeDutyCycle(0)
  p2.ChangeDutyCycle(0)

def retrieveData():
  data = dataqueue.getServoQueue()
  if (data != "empty"):
      print("Motor prints: " + data)

def servoStartListening():
  global musicGenre
  try:
    while True:
      data = dataqueue.getServoQueue()
      if data != "empty":
          musicGenre = data
      if musicGenre != "background":
#          p.ChangeDutyCycle(2)
#          p2.ChangeDutyCycle(2)
#          time.sleep(0.5)
#          p.ChangeDutyCycle(4)
#          p2.ChangeDutyCycle(4)
#          time.sleep(0.5)
           setAngle(90)
           time.sleep(2)
           setAngle(0)
  except KeyboardInterrupt:
    p.stop()
    p2.stop()
    GPIO.cleanup()

if __name__ == '__main__':
  servoStartListening()
