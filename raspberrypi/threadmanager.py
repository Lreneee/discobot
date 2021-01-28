import time 
import threading
import sys 

global threadMusicDetector
global threadLed
global threadMotor
global threadServo

def startThreads():
    global threadMusicDetector, threadLed, threadMotor, threadServo

    # Thread for Machine Learning
    import mlinterface
    import os
    threadMusicDetector = threading.Thread(target=mlinterface.startInterface)
    threadMusicDetector.start()
    os.system("sudo -upi chromium http://localhost:420&")
    time.sleep(10)

    # # Thread for ledstrip
    import visualization
    threadLed = threading.Thread(target=visualization.startLed)
    threadLed.start()
    time.sleep(10)

    # #Thread for motors
    import motor
    threadMotor = threading.Thread(target=motor.motorStartListening)
    threadMotor.start()
    time.sleep(10)

    # #Thread for servo
    import servo1
    threadServo = threading.Thread(target=servo1.servoStartListening)
    threadServo.start()
    time.sleep(5)

    # #Thread for app discobot
    import discobotapp
    discobotapp.startAppBackend()

def getThreadStatus():
    global threadMusicDetector, threadLed, threadMotor, threadServo

    print(threading.enumerate())

    print("threadMusicDetector is alive: \t" + str(threadMusicDetector.is_alive()))
    print("threadLed is alive:\t\t " + str(threadLed.is_alive()))
    print("threadMotor is alive:\t\t " + str(threadMotor.is_alive()))
    print("threadServo is alive: \t\t" + str(threadServo.is_alive()))

def stopThreads():
    sys.exit("Discobot is gratefully making use of naptime...")

 