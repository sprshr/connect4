import random
print("connect4 By Sepehr Sahraian")
print("AP CSP Mr. Keithley")
print('')


#global var

global columns
global rows
global moves


columnNumber = (
    "   1   ", "   2   ", "   3   ", "   4   ", "   5   ", "   6   ", "   7   "
)

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
    global selectedColumn
    selectedColumn = int(input())
    # input check
    while selectedColumn > 7:
        print("Select a Number Between the Given Range")
        selectedColumn = int(input())
    while len(columns[selectedColumn-1]) >= 6:
        print("Column Selected Is Full! Try Agian")
        selectedColumn = int(input())


def changeColumns():
    columns[selectedColumn - 1].insert(0, "X")


def changeTable():
    rows[5-((len(columns[selectedColumn-1]))-1)
         ][selectedColumn - 1] = xSelected

# this functions lets the computer to pick a column based on lists. There is no 7


def computerPlays():
    computerChoice = random.randint(0, 6)
    while len(columns[computerChoice]) >= 6:
        computerChoice = random.randint(0, 6)
    columns[computerChoice].insert(0, "O")
    rows[5-((len(columns[computerChoice]))-1)
         ][computerChoice] = oSelected


print("You're X Let's go!")


# game loop
moves = 0
while moves < 42:
    printTable()
    selection()
    changeColumns()
    changeTable()
    moves += 1
    computerPlays()
    moves += 1
printTable()
print("Game Tied")
