import sys
import itertools

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedA(data):
    two=0
    three=0
    for value in data:
        partTwo=0
        partThree=0
        for i in range(97,123):
            if value.count(chr(i))==2:
                partTwo+=1
            if value.count(chr(i))==3:
                partThree+=1
        if (partTwo>0):
            two+=1
        if (partThree>0):
            three+=1
    print(two, three)
    return two*three

def diffNumb(str1,str2):
    diffN=0
    for i in range(len(str1)):
        if (str1[i]!=str2[i]):
            diffN+=1
    return diffN

def solvedB(data):
    hit={}
    for pair in itertools.combinations(data, 2):
        if (diffNumb(pair[0],pair[1])==1):
            hit=pair
            break
    answer=""
    for i in range(len(hit[0])):
        if (hit[0][i]==hit[1][i]):
            answer+=str(hit[0][i])
    return (answer)


def main():
    data = readInput().split("\n")
    # print(solvedA(data))
    print(solvedB(data))


main()
