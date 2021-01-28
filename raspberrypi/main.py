import threadmanager
import time

# Setup Queue
import dataqueue
dataqueue.setup()

threadmanager.startThreads()

threadmanager.getThreadStatus()

time.sleep(60)

threadmanager.stopThreads()