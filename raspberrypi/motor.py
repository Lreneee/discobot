from time import sleep
import RPi.GPIO as GPIO

DIR = 23   # Direction GPIO Pin
STEP = 24  # Step GPIO Pin
DIR2 = 25
STEP2 = 4
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 1000   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR, CW)
GPIO.output(DIR2, CCW)

step_count = SPR
delay = .005

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)
GPIO.output(DIR2, CW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()
