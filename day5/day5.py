import sys
import os
def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(polymer):
    i=65
    while (i<91):
        if (polymer.find((chr(i+32)+chr(i)))>-1):
            polymer=polymer.replace(chr(i+32)+chr(i),"")
            i=64
        elif (polymer.find((chr(i)+chr(i+32)))>-1):
            polymer=polymer.replace(chr(i)+chr(i+32),"")
            i=64
        i+=1
    return len(polymer)

def solvedB(polymer):
    i=65
    minValue=1000000    
    for i in range(65,91):
        p=polymer
        p=p.replace(chr(i),"")
        p=p.replace(chr(i+32),"")
        newLen=solvedA(p)
        if (newLen<minValue):
            minValue=newLen
    return minValue


def main():
    polymer  =readInput()
    print(solvedA(polymer))
    print(solvedB(polymer))

main()
