import random
import logger
import timeTracker
l=logger.logger("!log")
l.clear()
def isort(sortedArray,value):
    for i in range(len(sortedArray)-1):
        if sortedArray[i]>=value:
            sortedArray.insert(i,value)
            return(sortedArray)
    sortedArray.append(value)
    return(sortedArray)
    
def insertSort(sortedArray,values):
    for i in values:
        sortedArray=isort(sortedArray,i)
    return(sortedArray)

def generateValues(num):
    m=[]
    for i in range(num):
        m.append(random.randint(0,num))
    return(m)
def main():
    tTracker=timeTracker.timeTracker()
    z=""
    while z!="e":
        z=input("test:t || specific size:s || exit:e  ").lower()
        if z=="s":
            m=generateValues(int(input("size:")))
            print(insertSort([m[0]],m[1:]))
        if z=="t":
            v=[10,100,1000,10000,100000]
            for i in v:
                m=generateValues(i)
                tTracker.startCount()
                insertSort([m[0]],m[1:])
                l.log(str(i)+" time/s:"+str(tTracker.getCount()))

main()
