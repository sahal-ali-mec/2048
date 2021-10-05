
import random
import copy
size = 4                            #size of the board
limit = 2048                        #final value to win the game
def display():                      #to display the board

    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numspaces = len(str(largest))

    for row in board:
        currentRow = "|"
        for element in row:
            if element == 0:
                currentRow += " " * numspaces + "|"
            else:
                currentRow += (" " * (numspaces - len(str(element)))) + str(element) + "|"

        print(currentRow)
    print()

def mergeOneRowLeft(row):                   # to merge one row to left
    for j in range(size-1):
        for i in range(size-1,0,-1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
    
    for i in range(size-1):
        if row[i] == row[i+1]:
            row[i]*= 2
            row[i+1] = 0

    for i in range(size-1,0,-1):
        if row[i-1] == 0:
            row[i-1]= row[i]
            row[i] = 0
    return row 

def mergeLeft(currentBoard):
    # merge every row in the board left
    for i in range(size):
        currentBoard[i] = mergeOneRowLeft(currentBoard[i])

    return currentBoard
# this function reverses the order of one row
def reverse(row):
    # add all the elemeents of the row to a new list, in reverse order
    new = []
    for i in range (size-1,-1,-1):
        new.append(row[i])
    return new

def mergeRight(currentBoard):
    # merge every row in the board right
    for i in range(size):
        #reverse the row , merge to the left, then reverse back
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowLeft(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

def transpose(currentBoard):             
    # to transpose the board
    for j in range(size):
        for i in range(j,size):
            if not i==j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def mergeUp(currentBoard):  # to merge the board up
    # transpose the board
    # merge the board to left
    # transpose back the board
    currentBoard = transpose(currentBoard)
    currentBoard = mergeLeft(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def mergeDown(currentBoard):  # to merge the board down
     # transpose the board
    # merge the board to right
    # transpose back the board
    currentBoard = transpose(currentBoard)
    currentBoard = mergeRight(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard


def RandomValue():    # initially for random numbers in board
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

def NewRandomValue():  # new random number in board after each move
    rowNum = random.randint(0,3)
    colNum = random.randint(0,3)

    while not board[rowNum][colNum] == 0: 
        rowNum = random.randint(0,3)
        colNum = random.randint(0,3) 

    board[rowNum][colNum] = RandomValue()

# to check if the user is won
def won():
    for row in board:
        if limit in row:
            return True
    return False 

# to check if user has lost
def lose():
    # two copies of the board
    tempboard1= copy.deepcopy(board)
    tempboard2= copy.deepcopy(board)

    # test every possible move 
    tempboard1 = mergeDown(tempboard1)
    if tempboard1== tempboard2:
        tempboard1 = mergeUp(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1= mergeLeft(tempboard1)
            if (tempboard1==tempboard2):
                tempboard1==mergeRight(tempboard1)
                if (tempboard1==tempboard2):
                    return True
    return False

board = []   # empty board
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    board.append(row)
num = 2
while num > 0:
    rowNum = random.randint(0,3)
    colNum = random.randint(0,3)

    if board [rowNum][colNum]== 0:
        board[rowNum][colNum] = RandomValue()
        num -= 1

print ("welcome to 2048 ! your goal is to combine the values to get the number 2048. you have to enter 1 to merge left, 2 to megr right, 3 to merge up and 4 to merge down \n")

display()
gameover= False       # setting game is not over

while not gameover:
    move = int(input("select the direction"))      # to enter the user input

    validInput = True  #assuming input is valid

    if move == 1:
        board = mergeLeft(board)
    elif move == 2:
        board = mergeRight(board)
    elif move == 3:
        board = mergeUp(board)
    elif move == 4:
        board == mergeDown(board)
    else : 
        validInput= False    # input is not valid

    if not validInput:       
        print("the input is invalid, enter a valid input")
    
    else :
        #test if the user have won
        if won():
            display()
            print("you won!")
            gameover= True
        else:
            NewRandomValue()       # create a new random value on board after each move
            display()               

            # if they lost
            if lose():
                print("sorry no moves left, you lose")
                gameover == True
