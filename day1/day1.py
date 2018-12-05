import sys
import os

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(data):
    sum=0
    for value in data:
        sum+=int(value)
    return sum

def solvedB(data):
    arr=set()
    sum=0
    i=0
    while (not sum in arr):
        arr.add(sum)     
        sum+=int(data[i])
        i+=1
        if (i==len(data)):
            i=0
    return sum

def main():
    data = readInput().split("\n")
    print(solvedA(data))
    print(solvedB(data))


main()
