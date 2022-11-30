"""
 Jacob Beaudin
 CSC 1800 - 2
 Python Bingo Verifier
 Due: 10/18/22
"""

import copy

#returns true if the target pattern contains a 4
def hasFour(target):
    four = False
    for r in range(len(target)):
        for c in range(len(target[0])):
            if (target[r][c] == 4):
                four = True
    return four

#rotates the parameter list 90 degrees clockwise and returns the resulting list
def matrixRotation(target):
    B = copy.deepcopy(target) #https://www.geeksforgeeks.org/difference-between-shallow-and-deep-copy-of-a-class/#:~:text=Shallow%20Copy%20stores%20the%20references,object%20in%20the%20original%20object.

    for r in range(len(target)):
        for c in range(len(target[0])):
            B[r][c] = (target[4-c][r])
    
    return B

#returns true if playerCard contains bingo and false if it does not
def isBingo(target, playerCard, bingoNums, four):
    match = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    
    #Everytime the value in playerCard[r][c] is present in bingoNums match[r][c] is set to a 1 or 4 as indicated by four
    if (four):
        for r in range(len(playerCard)):
            for c in range(len(playerCard[0])):
                for i in range(len(bingoNums)):
                    if ((playerCard[r][c] == bingoNums[i]) or (playerCard[r][c] == 0)): #determine if the value in [r][c] is present in the eligible Bingo numbers 
                            match[r][c] = 4
    else:
        for r in range(len(playerCard)):
            for c in range(len(playerCard[0])):
                for i in range(len(bingoNums)):
                    if ((playerCard[r][c] == bingoNums[i]) or (playerCard[r][c] == 0)): #determine if the value in [r][c] is present in the eligible Bingo numbers 
                            match[r][c] = 1
    
    #https://www.geeksforgeeks.org/python-logical-operators-with-examples-improvement-needed/
    #consulted for information on logical operators in Python
    
    isBingo = True
    
    #if the
    for r in range(len(target)):
        for c in range(len(target)):
            if (four):
                if ((target[r][c] == 4) and not (match[r][c] == 4)):
                    isBingo = False
            else:
                if((target[r][c] == 1) and not (match[r][c] == 1)):
                    isBingo = False
    
    return isBingo
    
    #Test cases: Valid and invalid target patterns with 4s and with 1s

#returns true if the last number called (the last index in bingoNums) contributes to the player's bingo call
def newBingo(target, playerCard, calledNums):
    new = False
    bingoNums = []
    
    for r in range(len(target)):
            for c in range(len(target[0])):
                if (target[r][c] != 0):
                    bingoNums.append(playerCard[r][c])
                    
    for i in range(len(bingoNums)):
        if (bingoNums[i] == calledNums[-1]):
            new = True
    
    return new
    
def main():
    #reads input from terminal, stores in respective list (or sublist)
    target = [[],[],[],[],[]]
    bingoNums = []
    playerCard = [[],[],[],[],[]]
    
    for lines in range(0,13,1):
        a = input()
        if (lines <= 4):
            target[lines] = a.split() #without a specifed parameter, split will occur at any white space character including newline
        if (lines == 6):
            bingoNums= a.split()
        if (lines >= 8):
            playerCard[(lines - 8)] = a.split()
    
    #https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/ used for information on list comprehension
    for i in range(0,5,1):
        target[i] = [int(x) for x in target[i]]
        
    for i in range(0,5,1):
        playerCard[i] = [int(x) for x in playerCard[i]]
        
    for i in range(0,len(bingoNums)):
        bingoNums[i] = int(bingoNums[i])
    
    four = hasFour(target)
    win = False
    
    rotate90 = matrixRotation(target)
    rotate180 = matrixRotation(rotate90)
    rotate270 = matrixRotation(rotate180)
        
    if (isBingo(target, playerCard, bingoNums, four) and newBingo(target, playerCard, bingoNums)):
        win = True
        
    if(four):
        if (isBingo(rotate90, playerCard, bingoNums, four) and newBingo(rotate90, playerCard, bingoNums)):
            win = True

    if(four):
        if (isBingo(rotate180, playerCard, bingoNums, four) and newBingo(rotate180, playerCard, bingoNums)):
            win = True

    if(four):
        if (isBingo(rotate270, playerCard, bingoNums, four) and newBingo(rotate270, playerCard, bingoNums)):
            win = True

    if(win):
        print("VALID BINGO!")
    else:
        print("NO BINGO!")
    
main()