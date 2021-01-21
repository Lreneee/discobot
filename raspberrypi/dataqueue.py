import queue

global ledQueue
global servoQueue
global motorQueue

appInControl = False

def AppControlOn():
    global appInControl
    appInControl = True

def AppControlOff():
    global appInControl
    appInControl = False

def setup():
    global ledQueue
    global servoQueue
    global motorQueue
    
    ledQueue = queue.Queue()
    servoQueue = queue.Queue()
    motorQueue = queue.Queue()

def enterData(data):    
    global ledQueue
    global servoQueue
    global motorQueue
    global appInControl

    if !appInControl:
        ledQueue.put(data)
        servoQueue.put(data)
        motorQueue.put(data)
    else:
        ledQueue.put("background")
        servoQueue.put("background")
        motorQueue.put("background")
    
def getLedQueue():
    global ledQueue
    var = "empty"
    try:
        var = ledQueue.get(block=False)
    except queue.Empty:
        return var
    
    return var

def getServoQueue():
    global servoQueue
    var = "empty"
    try:
        var = servoQueue.get(block=False)
    except queue.Empty:
        return var

    return var

def getMotorQueue():
    global motorQueue
    var = "empty"
    try:
        var = motorQueue.get(block=False)
    except queue.Empty:
        return var

    return var
