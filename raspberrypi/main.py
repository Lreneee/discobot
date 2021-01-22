import threading
import queue
import time 

# Setup Queue
import dataqueue
dataqueue.setup()

# Thread for Machine Learning
import mlinterface
import os
threadMusicDetector = threading.Thread(target=mlinterface.startInterface)
threadMusicDetector.start()
os.system("sudo -upi chromium http://localhost:420&")
time.sleep(10)

# Thread for ledstrip
import visualization
threadLed = threading.Thread(target=visualization.startLed)
threadLed.start()
time.sleep(10)

#Thread for motors
import motor
threadMotor = threading.Thread(target=motor.motorStartListening)
threadMotor.start()
time.sleep(10)

#Thread for servo
import servo1
threadServo = threading.Thread(target=servo1.servoStartListening)
threadServo.start()

#Thread for app discobot
import discobotapp
discobotapp.startAppBackend()
