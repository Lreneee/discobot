import queue

global entryQueue
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
    global entryQueue
    global ledQueue
    global servoQueue
    global motorQueue

    entryQueue = queue.Queue()
    ledQueue = queue.Queue()
    servoQueue = queue.Queue()
    motorQueue = queue.Queue()

def enterData(data):    
    global ledQueue
    global servoQueue
    global motorQueue

    ledQueue.put(data)
    servoQueue.put(data)
    motorQueue.put(data)

def getLedQueue():
    global ledQueue
    var = "empty"
    try:
        var = ledQueue.get(block=False)
    except queue.Empty:
        return var
    if appInControl:
        return "led-off"

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

# def enterData(data):
#     global entryQueue
#     print("queue gets " + data)
#     entryQueue.put(data)

# def extractData():
#     global entryQueue
#     var = "empty"
#     try:
#         var = entryQueue.get(block=False)
#     except queue.Empty:
#         return var

#     print("queue shares " + var)
#     return var
