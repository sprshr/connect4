print("connect4 By Sepehr Sahraian")
print("AP CSP Mr. Keithley")
print('')


#global var
global columns
global rows


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


def changeColumns():
    columns[selectedColumn - 1].insert(0, "O")


def changetable():
    rows[5-((len(columns[selectedColumn-1]))-1)
         ][selectedColumn - 1] = xSelected


print("You're X Let's go!")
printTable()
selection()
changeColumns()
changetable()
printTable()
