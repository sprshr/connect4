import random
print(r"""\


                                        _    _  _   
                                       | |  | || |  
   ___  ___   _ __   _ __    ___   ___ | |_ | || |_ 
  / __|/ _ \ | '_ \ | '_ \  / _ \ / __|| __||__   _|
 | (__| (_) || | | || | | ||  __/| (__ | |_    | |  
  \___|\___/ |_| |_||_| |_| \___| \___| \__|   |_|  
                                                
            """)
print("connect4 By Sepehr Sahraian")
print("AP CSP Mr. Keithley")
print('')


# global var

global moves
userWon = False
computerWon = False


columnNumber = (
    "   1   ", "   2   ", "   3   ", "   4   ", "   5   ", "   6   ", "   7   "
)

# visual game board
rows = [[
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
], [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
], [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
], [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
], [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
], [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]]

# data is stored here
columns = [], [], [], [], [], [], []


xSelected = "|  X  |"
oSelected = "|  O  |"

# game functions


def printTable():
    print('')
    print(columnNumber)
    print('')
    print(rows[0])
    print('')
    print(rows[1])
    print('')
    print(rows[2])
    print('')
    print(rows[3])
    print('')
    print(rows[4])
    print('')
    print(rows[5])


def selection():
    print("Make a Selection 1-7")
    global selectedIndex
    selectedIndex = int(input())-1
    # input check
    while selectedIndex > 6 or selectedIndex < 0:
        print("Select a Number Between the Given Range")
        selectedIndex = int(input())-1
    while len(columns[selectedIndex]) >= 6:
        print("Column Selected Is Full! Try Agian")
        selectedIndex = int(input()) - 1


def checkPlayerWin():
    # if all 4 discs are in the same columns
    if len(columns[selectedIndex]) >= 4:
        if columns[selectedIndex][0] == columns[selectedIndex][1] == columns[selectedIndex][2] == columns[selectedIndex][3]:
            return True
    # if marbles horizontally match
    if selectedIndex >= 0 and selectedIndex <= 3:
        if len(columns[selectedIndex]) <= len(columns[selectedIndex+1]):
            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+1]:
                if len(columns[selectedIndex+1]) <= len(columns[selectedIndex+2]):
                    if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+1] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+2]:
                        if len(columns[selectedIndex+2]) <= len(columns[selectedIndex+3]):
                            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+2] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+3]:
                                return True
    if selectedIndex >= 1 and selectedIndex <= 4:
        if len(columns[selectedIndex]) <= len(columns[selectedIndex-1]):
            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-1]:
                if len(columns[selectedIndex]) <= len(columns[selectedIndex+1]):
                    if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+1]:
                        if len(columns[selectedIndex+1]) <= len(columns[selectedIndex+2]):
                            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+1] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+2]:
                                return True
    if selectedIndex >= 2 and selectedIndex <= 5:
        if len(columns[selectedIndex]) <= len(columns[selectedIndex-1]):
            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-1]:
                if len(columns[selectedIndex-1]) <= len(columns[selectedIndex-2]):
                    if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-1] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-2]:
                        if len(columns[selectedIndex]) <= len(columns[selectedIndex+1]):
                            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex+1]:
                                return True
    if selectedIndex >= 3 and selectedIndex <= 6:
        if len(columns[selectedIndex]) <= len(columns[selectedIndex-1]):
            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-1]:
                if len(columns[selectedIndex-1]) <= len(columns[selectedIndex-2]):
                    if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-1] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-2]:
                        if len(columns[selectedIndex-2]) <= len(columns[selectedIndex-3]):
                            if rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-2] == rows[5-((len(columns[selectedIndex]))-1)][selectedIndex-3]:
                                return True


def changeColumns():
    columns[selectedIndex].insert(0, "X")


def changeTable():
    rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] = xSelected
# this functions lets the computer to pick a column based on lists. There is no 7


def computerPlays():
    global computerChoice
    computerChoice = random.randint(0, 6)
    while len(columns[computerChoice]) >= 6:
        computerChoice = random.randint(0, 6)
    columns[computerChoice].insert(0, "O")
    rows[5-((len(columns[computerChoice]))-1)
         ][computerChoice] = oSelected


def checkComputerWin():
    if len(columns[computerChoice]) >= 4:
        if columns[computerChoice][0] == columns[computerChoice][1] == columns[computerChoice][2] == columns[computerChoice][3]:
            return True


print("You're X Let's go!")


# game loop
moves = 0
while moves < 42:
    printTable()
    selection()
    changeColumns()
    changeTable()
    if checkPlayerWin():
        userWon = True
        break
    moves += 1
    computerPlays()
    if checkComputerWin():
        computerWon = True
        break
    moves += 1

printTable()

# following statements determine how the game has ended

if userWon:
    print('')
    print("You Won")
    print("Good Job!1")

if computerWon:
    print('')
    print("I Won!")

if moves >= 42:
    print('1')
    print("Game Tied!")
