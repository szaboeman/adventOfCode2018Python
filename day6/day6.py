import sys
import re
import os

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def manhattanDistance(i1,j1,i2,j2):
    return abs(i1-i2)+abs(j1-j2)

def minManhattanDistance(data,n,m):
    minPiece=0
    minValue=16000
    minIndex=-1
    for i,values in enumerate(data):
        md=manhattanDistance(n,m,int(values[1]),int(values[0]))
        if (minValue>md):
            minPiece=0
            minValue=md
            minIndex=i
        elif (minValue==md):
            minPiece+=1
            minIndex=-1
    return minIndex

# def areaRec(area,sig,i,j):
#     if (i>=0 and i<400 and j>=0 and j<400 and area[i][j]==sig):
#         area[i][j]='C'
#         if (i==0 or i==399 or j==0 or j==399):
#             return -10000
#         else:
#             return 1+areaRec(area,sig,i-1,j)+areaRec(area,sig,i+1,j)+areaRec(area,sig,i,j-1)+areaRec(area,sig,i,j+1)
#     return 0


def areaPiece(area,sign):
    p=0
    for i,row in enumerate(area):
        for j,value in enumerate(row):
            if (value==sign):
                if (i==0 or j==0 or i==399 or j==399):
                    return -1
                else:
                    p+=1
    return p

def solvedA(data):
    area=[[-1]*400 for _ in range(400)]
    for i,values in enumerate(data):
        area[int(values[1])][int(values[0])]=i

    for i in range(0,400):
        for j in range(0,400):
            if (area[i][j]==-1):
                area[i][j]=minManhattanDistance(data,i,j)
    
    maxArea=0
    for i,values in enumerate(data):
        partArea=areaPiece(area, i)
        if (partArea>maxArea):
            maxArea=partArea
    return maxArea
    
def solvedB(data):
    c=0
    for i in range(0,400):
        for j in range(0,400):
            sum=0
            for values in data:
                sum+=manhattanDistance(i,j,int(values[0]),int(values[1]))
            if sum<10000:
                c+=1
    return c
    
def main():
    data=readInput().split("\n")
    data=[re.split(r", ",x)  for x in data]
    print(solvedA(data))
    print(solvedB(data))

main()
