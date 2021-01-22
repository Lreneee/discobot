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
delay = .01
counter = 0

musicGenre = "background"

GPIO.setmode(GPIO.BCM)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

def goForward():
    GPIO.output(DIR, CCW)
    GPIO.output(DIR2, CW)
    
def goBackward():
    GPIO.output(DIR, CCW)
    GPIO.output(DIR2, CW)

def setMotorSteps():
    global counter
    
    GPIO.output(STEP, GPIO.HIGH)
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)
    
    counter = counter + 1
    if counter == 500:
        goBackward()
    elif counter == 800:
        goForward()
        counter = 0    
    
def motorStartListening():
    global musicGenre, delay, STEP, STEP2
    
    goForward()
    
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
