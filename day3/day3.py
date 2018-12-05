import re

def readInput():
    with open("input.txt") as file:
        data = file.read()
    file.close()
    return data

def solvedAB(data, a=False):
    plans = [[0] * 1000 for i in range(1000)]
    for value in data:
        for i in range(int(value[2]),int(value[2])+int(value[4])):
            for j in range(int(value[3]), int(value[3])+int(value[5])):
                plans[i][j]+=1  
    c=0
    for i in range(len(plans)):
        for j in range(len(plans[i])):
            if plans[i][j]>1:
                c+=1
    if (not a):
        return c
    else:
        hit=False
        i=0
        while (i<len(data) and not hit):
            c=0
            for j in range(int(data[i][2]),int(data[i][2])+int(data[i][4])):
                for k in range(int(data[i][3]), int(data[i][3])+int(data[i][5])):
                    c+=plans[j][k]
            if (c==int(data[i][4])*int(data[i][5])):
                hit=True
            else:
                i+=1 
        return data[i][1]
            

def main():
    data = readInput().split('\n')
    for i,row in enumerate(data):
        data[i]=re.split(r"#| @ |,|: |x",row)
    print(solvedAB(data))
    print(solvedAB(data,True))

main()