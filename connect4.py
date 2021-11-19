import random
print(r"""/


                                        _    _  _   
                                       | |  | || |  
   ___  ___   _ __   _ __    ___   ___ | |_ | || |_ 
  / __|/ _ \ | '_ \ | '_ \  / _ \ / __|| __||__   _|
 | (__| (_) || | | || | | ||  __/| (__ | |_    | |  
  \___|\___/ |_| |_||_| |_| \___| \___| \__|   |_|  
                                                
            """)
print("connect4 By Sepehr Sahraian")
print("AP CSP Class")
print('')



# global var

global moves
userWon = False
computerWon = False
XScore = 0
OScore = 0


columnNumber = (
    "   1   ", "   2   ", "   3   ", "   4   ", "   5   ", "   6   ", "   7   "
)


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


def changeColumns():
    columns[selectedIndex].append("X")


def changeTable():
    rows[5-((len(columns[selectedIndex]))-1)][selectedIndex] = xSelected


def computerPlays():
    # this functions lets the computer to pick a column based on lists. There is no 7
    global computerChoice
    computerChoice = random.randint(0, 6)
    while len(columns[computerChoice]) >= 6:
        computerChoice = random.randint(0, 6)
    columns[computerChoice].append("O")
    rows[5-((len(columns[computerChoice]))-1)][computerChoice] = oSelected
	


def checkWin(index):
	# if all 4 discs are in the same columns
    if len(columns[index]) >= 4:
        if columns[index][len(columns[index])-1] == columns[index][len(columns[index])-2] == columns[index][len(columns[index])-3] == columns[index][len(columns[index])-4]:
            return True
    # if marbles horizontally match
    if index >= 0 and index <= 3:
        if len(columns[index]) <= len(columns[index+1]):
            if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index+1]:
                if len(columns[index+1]) <= len(columns[index+2]):
                    if rows[5-((len(columns[index]))-1)][index+1] == rows[5-((len(columns[index]))-1)][index+2]:
                        if len(columns[index+2]) <= len(columns[index+3]):
                            if rows[5-((len(columns[index]))-1)][index+2] == rows[5-((len(columns[index]))-1)][index+3]:
                                return True
    if index >= 1 and index <= 4:
        if len(columns[index]) <= len(columns[index-1]):
            if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index-1]:
                if len(columns[index]) <= len(columns[index+1]):
                    if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index+1]:
                        if len(columns[index+1]) <= len(columns[index+2]):
                            if rows[5-((len(columns[index]))-1)][index+1] == rows[5-((len(columns[index]))-1)][index+2]:
                                return True
    if index >= 2 and index <= 5:
        if len(columns[index]) <= len(columns[index-1]):
            if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index-1]:
                if len(columns[index-1]) <= len(columns[index-2]):
                    if rows[5-((len(columns[index]))-1)][index-1] == rows[5-((len(columns[index]))-1)][index-2]:
                        if len(columns[index]) <= len(columns[index+1]):
                            if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index+1]:
                                return True
    if index >= 3 and index <= 6:
        if len(columns[index]) <= len(columns[index-1]):
            if rows[5-((len(columns[index]))-1)][index] == rows[5-((len(columns[index]))-1)][index-1]:
                if len(columns[index-1]) <= len(columns[index-2]):
                    if rows[5-((len(columns[index]))-1)][index-1] == rows[5-((len(columns[index]))-1)][index-2]:
                        if len(columns[index-2]) <= len(columns[index-3]):
                            if rows[5-((len(columns[index]))-1)][index-2] == rows[5-((len(columns[index]))-1)][index-3]:
                                return True
    # diagonally left to right upwards
    # 1 in the first column
    if index <= 3:
        if len(columns[index+1]) > len(columns[index]):
            if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])]:
                if len(columns[index+2]) > len(columns[index+1]):
                    if columns[index][len(columns[index])-1] == columns[index+2][len(columns[index])+1]:
                        if len(columns[index+3]) > len(columns[index+2]):
                            if columns[index][len(columns[index])-1] == columns[index+3][len(columns[index])+2]:
                                return True
    # 2 in the second column
    if index >= 1 and index <= 4 and len(columns[index]) >= 2:
        if (len(columns[index]) - len(columns[index-1])) <= 1:
            if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])-2]:
                if len(columns[index+1]) > len(columns[index]):
                    if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])]:
                        if len(columns[index+2]) > len(columns[index+1]):
                            if columns[index][len(columns[index])-1] == columns[index+2][len(columns[index])+1]:
                                return True
    # 3 in the third column
    if index >= 2 and index <= 5 and len(columns[index]) >= 3:
        if (len(columns[index]) - len(columns[index-1])) <= 1:
            if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])-2]:
                if (len(columns[index]) - len(columns[index-2])) <= 2:
                    if columns[index][len(columns[index])-1] == columns[index-2][len(columns[index])-3]:
                        if len(columns[index+1]) > len(columns[index]):
                            if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])]:
                                return True
    # 4 in the fourth column
    if index >= 3:
        if (len(columns[index]) - len(columns[index-1])) <= 1 and len(columns[index]) >= 4:
            if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])-2]:
                if (len(columns[index]) - len(columns[index-2])) <= 2:
                    if columns[index][len(columns[index])-1] == columns[index-2][len(columns[index])-3]:
                        if (len(columns[index]) - len(columns[index-3])) <= 3:
                            if columns[index][len(columns[index])-1] == columns[index-3][len(columns[index])-4]:
                                return True
    # diagonally left to right downwards
    # 4 in the first column
    if index <= 3:
        if len(columns[index]) >= 4 and (len(columns[index])-len(columns[index+1])) <= 1:
            if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])-2]:
                if (len(columns[index+1])-len(columns[index+2])) <= 1:
                    if columns[index][len(columns[index])-1] == columns[index+2][len(columns[index])-3]:
                        if (len(columns[index+2])-len(columns[index+3])) <= 1:
                            if columns[index][len(columns[index])-1] == columns[index+3][len(columns[index])-4]:
                                return True
    # 3 in the second column
    if index >= 1 and index <= 4 and len(columns[index]) >= 3:
        if (len(columns[index]) - len(columns[index+1])) <= 1:
            if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])-2]:
                if (len(columns[index+1]) - len(columns[index+2])) <= 1:
                    if columns[index][len(columns[index])-1] == columns[index+2][len(columns[index])-3]:
                        if len(columns[index-1]) >= len(columns[index])+1:
                            if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])]:
                                return True
    # 2 in the third column
    if index >= 2 and index <= 5 and len(columns[index]) >= 2:
        if (len(columns[index]) - len(columns[index+1])) <= 1:
            if columns[index][len(columns[index])-1] == columns[index+1][len(columns[index])-2]:
                if len(columns[index-1]) >= len(columns[index])+1:
                    if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])]:
                        if len(columns[index-2]) >= len(columns[index])+2:
                            if columns[index][len(columns[index])-1] == columns[index-2][len(columns[index])+1]:
                                return True
    # 1 in the fourth column
    if index >= 3:
        if len(columns[index-1]) >= len(columns[index])+1:
            if columns[index][len(columns[index])-1] == columns[index-1][len(columns[index])]:
                if len(columns[index-2]) >= len(columns[index])+2:
                    if columns[index][len(columns[index])-1] == columns[index-2][len(columns[index])+1]:
                        if len(columns[index-3]) >= len(columns[index])+3:
                            if columns[index][len(columns[index])-1] == columns[index-3][len(columns[index])+2]:
                                return True

print("You're X Let's go!")
print('')
print("X: " , XScore)
print("O: " , OScore)


# game loop
while True:
	moves = 0
	#data is stores here
	columns =  [], [], [], [], [], [], []
	#displayed table
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

	while moves < 42:
		printTable()
		selection()
		changeColumns()
		changeTable()
		if checkWin(selectedIndex):
			userWon = True
			break
		moves += 1
		computerPlays()
		if checkWin(computerChoice):
			computerWon = True
			break
		moves += 1

	printTable()

	# following statements determine how the game has ended

	if userWon:
		print('')
		print("You Won")
		print("Good Job!")
		XScore += 1
		print("X: " , XScore)
		print("O: " , OScore)

	if computerWon:
		print('')
		print("I Won!")
		OScore += 1
		print("X: " , XScore)
		print("O: " , OScore)

	if moves >= 42:
		print('1')
		print("Game Tied!")
		print("X: " , XScore)
		print("O: " , OScore)
	print("Do You Want to Continue? (Y/N)")
	response = str(input())
	if response == "N": break
	while response != "Y" and response != "N":
		print("Do You Want to Continue? (Y/N)")
		response = str(input())
		if response == "N": break