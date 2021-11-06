print("connect4 By Sepehr Sahraian")
print("AP CSP Mr. Keithley")
print('')
columnNumber = [
    "   1   ", "   2   ", "   3   ", "   4   ", "   5   ", "   6   ", "   7   "
]
row1 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]
row2 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]
row3 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]
row4 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]
row5 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]
row6 = [
    "|     |", "|     |", "|     |", "|     |", "|     |", "|     |", "|     |"
]

column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []
column7 = []

#global var
xSelected = "|  X  |"
oSelected = "|  O  |"


def printTable():
    print('')
    print(columnNumber)
    print('')
    print(row1)
    print('')
    print(row2)
    print('')
    print(row3)
    print('')
    print(row4)
    print('')
    print(row5)
    print('')
    print(row6)


def selection():
    print("Make a Selection 1-7")
    global columnSelected
    columnSelected = input()


print("I'm X you're O Let's go!")
printTable()
selection()
