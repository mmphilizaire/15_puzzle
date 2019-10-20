def swap(text,index1,index2):
    index1 = index1
    index2 = index2
    s=list(text)
    temp=s[index1]
    s[index1]=s[index2]
    s[index2]=temp
    return "".join(s)

def moves(pzzl):
    lstNextSpace = [{1,4},{0,2,5},{1,3,6},{2,7},{0,5,8},{1,4,6,9},\
    {2,5,7,10},{3,6,11},{4,9,12},{5,8,10,13},{6,9,11,14},{7,10,15},\
    {8,13},{9,12,14},{10,13,15},{11,14}]
    space = pzzl.index(" ")
    l = []
    for x in lstNextSpace[space]:
        l.append(swap(pzzl,space,x))
    return l

def output(pzzl):
    for x in range(0,4):
        print(pzzl[0+4*x]+pzzl[1+4*x]+pzzl[2+4*x]+pzzl[3+4*x])

def sumdistance(pzzl,goal):
    count = 0
    for x in range(len(pzzl)):
        count+=abs(x//4-goal.index(pzzl[x])//4)
        count+=abs(x%4-goal.index(pzzl[x])%4)
    return count

def findSolution1(puzzle,goal,pop):
    sol = []
    parseMe = [[puzzle,sumdistance(puzzle,goal),0]]
    alreadySeen = {puzzle:""}
    while parseMe:
        closest = 0
        for x in range(1,len(parseMe)):
            if parseMe[x][1]+parseMe[x][2] < parseMe[closest][1]+parseMe[closest][2]:
                closest=x
        check = parseMe.pop(closest)
        pop+=1
        if check[0] == goal:
            sol.append(goal)
            while alreadySeen[check[0]]!="":
                sol.append(alreadySeen[check[0]])
                check[0]=alreadySeen[check[0]]
            return [sol,pop]
        else:
            desc = moves(check[0])
            for x in desc:
                if not x in alreadySeen:
                    parseMe.append([x,sumdistance(x,goal),check[2]+1])
                    alreadySeen[x]=check[0]
    return [sol,pop]

def findSolution2(puzzle,goal,pop):
    sol = []
    parseMe = [[puzzle,abs(inversionCount(puzzle)),0]]
    alreadySeen = {puzzle:""}
    while parseMe:
        closest = 0
        for x in range(1,len(parseMe)):
            if parseMe[x][1]+parseMe[x][2] < parseMe[closest][1]+parseMe[closest][2]:
                closest=x
        check = parseMe.pop(closest)
        pop+=1
        if check[0] == goal:
            sol.append(goal)
            while alreadySeen[check[0]]!="":
                sol.append(alreadySeen[check[0]])
                check[0]=alreadySeen[check[0]]
            return [sol,pop]
        else:
            desc = moves(check[0])
            for x in desc:
                if not x in alreadySeen:
                    parseMe.append([x,abs(inversionCount(x)),check[2]+1])
                    alreadySeen[x]=check[0]
    return [sol,pop]

def inversionCount(pzzl):
    count = 0
    pzzl = pzzl[:pzzl.index(" ")]+pzzl[pzzl.index(" ")+1:]
    for x in range(len(pzzl)):
        for y in range(x+1,len(pzzl)):
            if ord(pzzl[x]) > ord(pzzl[y]):
                count+=1
    return count

def hasSolution(pzzl,goal):
    distance = abs((pzzl.index(" ")//4)-(goal.index(" ")//4))
    if (inversionCount(pzzl)+distance)&1 == inversionCount(goal)&1:
        return True
    else:
        return False

import sys
puzzle = sys.argv[1]
puzzle = puzzle[:puzzle.index("_")]+" "+puzzle[puzzle.index("_")+1:]
goal = "ABCDEFGHIJKLMNO "

if hasSolution(puzzle,goal):
    solution = findSolution1(puzzle,goal,0)
    for x in range(len(solution[0]))[::-1]:
        output(solution[0][x])
        print("")
    print("finding the solution took %s steps" % (len(solution[0])-1))
else:
    print("no solution :(")

