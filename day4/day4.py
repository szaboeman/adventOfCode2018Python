import sys
import re
import datetime
from operator import itemgetter

def readInput():
    with open("n:\\projects\\adventofcode2018\\day4\\input.txt") as file:
        data = file.read()
    file.close()
    return data
def findIndexGuardId(guards,guardId):
    i=0
    for guard in list(guards):
        if (guard["id"]==guardId):
            return i
        i+=1
    return -1

def solvedAB(data,taskB=False):
    guards=[]
    guardId=""
    guardLoc=-1
    start=-1
    for value in list(data):
        if ("id" in list(value.keys())):
            guardId=value["id"]
            guarLoc=findIndexGuardId(guards,guardId)
            if (guarLoc==-1):
                guard=dict()
                guard["id"]=value["id"]
                guard["minutes"]=[0]*60
                guards.append(guard)
        elif ("activity" in list(value.keys())):
            if (value["activity"]=="start sleep"):
                start=value["time"]
            else:
                end=value["time"]
                for i in range(start.minute,end.minute):
                    guards[guarLoc]["minutes"][i]+=1

    maximum=dict()
    maximum["day"]=-1
    maximum["id"]=-1

    if (not taskB):
        maximum["sum"]=-1
        for i,value in enumerate(list(guards)):
            c=0
            for j, minute in enumerate(value["minutes"]):
                if (minute>0): 
                    c+=minute
            if maximum["sum"]<c:
                maximum["sum"]=c
                maximum["day"]=value["minutes"].index(max(value["minutes"]))
                maximum["id"]=value["id"]

        return int(maximum["day"])*int(maximum["id"])
    else:
        maximum["value"]=-1
        for i,value in enumerate(list(guards)):
            if (max(value["minutes"])>maximum["value"]):
                maximum["value"]=max(value["minutes"])
                maximum["day"]=value["minutes"].index(max(value["minutes"]))
                maximum["id"]=value["id"]

        return int(maximum["day"])*int(maximum["id"])


def prepareData(data):
    for i,values in enumerate(data):
        ds=re.split(r"-| |\:|\] |\#",values[1:len(data[i])])
        dt=datetime.datetime(int(ds[0]), int(ds[1]), int(ds[2]),int(ds[3]),int(ds[4]))
        data[i]={}
        data[i]['time']=dt
        if (ds[5]=="Guard"):
            data[i]['id']=ds[7]
        if (ds[5]=="falls"):
            data[i]['activity']="start sleep"
        if (ds[5]=="wakes"):
            data[i]['activity']="start awake"
    return sorted(data, key=itemgetter('time'))


def main():
    data = readInput().split("\n")
    data=prepareData(data)
    print(solvedAB(data))
    print(solvedAB(data,True))

main()
