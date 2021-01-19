import threading
import queue
import time 
import os
import dataqueue
import mlinterface      # Flask server as interface Machine Learning model
#import motor            # Bipolair motors
#import servo            # Servo's for the arms
import discobotapp      # Web app communication API
import visualization    # Led strip

# Setup Queue
dataqueue.setup()

# Start threads
threadMusicDetector = threading.Thread(target=mlinterface.startInterface)
threadMusicDetector.start()
#os.system("sudo -upi chromium http://localhost:420")
time.sleep(10)
print("Delay over")
# while(True):
#     data = dataqueue.extractData()
#     if (data != "empty"):
#         print("Main prints: " + data)

# Thread for ledstrip
threadLed = threading.Thread(target=visualization.startLed)
threadLed.start()

# threadMotor = threading.Thread(target=motor.motorStartListening)
# threadMotor.start()

# time.sleep(2)
# threadServo = threading.Thread(target=servo.servoStartListening)
# threadServo.start()

#threadApp = threading.Thread(target=discobotapp.startAppBackend)
#threadApp.start()
discobotapp.startAppBackend()
