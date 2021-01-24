import time

class logger():

    def __init__(self,fileName):
        self.fileName=fileName+".txt"

    def log(self,name):
        with open(self.fileName,"a")  as f:
            f.write(time.strftime("%H:%M:%S")+"  :  "+name+"\n")

    def clear(self):
        open(self.fileName,"w").close()
