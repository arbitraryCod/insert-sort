import time

class timeTracker():

    def __init__(self):
        self.timeElapsed=0

    def startCount(self):
        self.timeElapsed=time.time()

    def getCount(self):
        return time.time()-self.timeElapsed

class timer():

    def __init__(self,length):
        self.length=length
        self.tTracker=timeTracker()
        self.tTracker.startCount

    def timeCheck(self):
        if self.tTracker.getCount()>self.length:
            self.tTracker.startCount()
            return True
        else:
            return False
