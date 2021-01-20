from time import sleep
import RPi.GPIO as GPIO

import dataqueue

DIR = 23   
STEP = 24  

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

GPIO.output(DIR, CCW)
GPIO.output(DIR2, CW)

step_count = SPR
delay = .009

musicGenre = "background"

def setMotorSteps():
    GPIO.output(STEP, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    GPIO.output(STEP2, GPIO.LOW)
    
def motorStartListening():
    global musicGenre, delay, STEP, STEP2, step_count
    
    while(True):
        data = dataqueue.getMotorQueue()
        if data != "empty":
            musicGenre = data
            
        if musicGenre != "background":
            setMotorSteps() 
        else: 
            GPIO.output(STEP, GPIO.LOW)
            GPIO.output(STEP2, GPIO.LOW)
            
if __name__ == '__main__':
    GPIO.cleanup()
