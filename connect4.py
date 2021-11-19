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


def checkPlayerWin():
    # if all 4 discs are in the same columns
    if len(columns[selectedIndex]) >= 4:
        if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex][len(columns[selectedIndex])-2] == columns[selectedIndex][len(columns[selectedIndex])-3] == columns[selectedIndex][len(columns[selectedIndex])-4]:
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
    # diagonally left to right upwards
    # 1 in the first column
    if selectedIndex <= 3:
        if len(columns[selectedIndex+1]) > len(columns[selectedIndex]):
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])]:
                if len(columns[selectedIndex+2]) > len(columns[selectedIndex+1]):
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+2][len(columns[selectedIndex])+1]:
                        if len(columns[selectedIndex+3]) > len(columns[selectedIndex+2]):
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+3][len(columns[selectedIndex])+2]:
                                return True
    # 2 in the second column
    if selectedIndex >= 1 and selectedIndex <= 4 and len(columns[selectedIndex]) >= 2:
        if (len(columns[selectedIndex]) - len(columns[selectedIndex-1])) <= 1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])-2]:
                if len(columns[selectedIndex+1]) > len(columns[selectedIndex]):
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])]:
                        if len(columns[selectedIndex+2]) > len(columns[selectedIndex+1]):
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+2][len(columns[selectedIndex])+1]:
                                return True
    # 3 in the third column
    if selectedIndex >= 2 and selectedIndex <= 5 and len(columns[selectedIndex]) >= 3:
        if (len(columns[selectedIndex]) - len(columns[selectedIndex-1])) <= 1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])-2]:
                if (len(columns[selectedIndex]) - len(columns[selectedIndex-2])) <= 2:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-2][len(columns[selectedIndex])-3]:
                        if len(columns[selectedIndex+1]) > len(columns[selectedIndex]):
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])]:
                                return True
    # 4 in the fourth column
    if selectedIndex >= 3:
        if (len(columns[selectedIndex]) - len(columns[selectedIndex-1])) <= 1 and len(columns[selectedIndex]) >= 4:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])-2]:
                if (len(columns[selectedIndex]) - len(columns[selectedIndex-2])) <= 2:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-2][len(columns[selectedIndex])-3]:
                        if (len(columns[selectedIndex]) - len(columns[selectedIndex-3])) <= 3:
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-3][len(columns[selectedIndex])-4]:
                                return True
    # diagonally left to right downwards
    # 4 in the first column
    if selectedIndex <= 3:
        if len(columns[selectedIndex]) >= 4 and (len(columns[selectedIndex])-len(columns[selectedIndex+1])) <= 1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])-2]:
                if (len(columns[selectedIndex+1])-len(columns[selectedIndex+2])) <= 1:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+2][len(columns[selectedIndex])-3]:
                        if (len(columns[selectedIndex+2])-len(columns[selectedIndex+3])) <= 1:
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+3][len(columns[selectedIndex])-4]:
                                return True
    # 3 in the second column
    if selectedIndex >= 1 and selectedIndex <= 4 and len(columns[selectedIndex]) >= 3:
        if (len(columns[selectedIndex]) - len(columns[selectedIndex+1])) <= 1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])-2]:
                if (len(columns[selectedIndex+1]) - len(columns[selectedIndex+2])) <= 1:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+2][len(columns[selectedIndex])-3]:
                        if len(columns[selectedIndex-1]) >= len(columns[selectedIndex])+1:
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])]:
                                return True
    # 2 in the third column
    if selectedIndex >= 2 and selectedIndex <= 5 and len(columns[selectedIndex]) >= 2:
        if (len(columns[selectedIndex]) - len(columns[selectedIndex+1])) <= 1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex+1][len(columns[selectedIndex])-2]:
                if len(columns[selectedIndex-1]) >= len(columns[selectedIndex])+1:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])]:
                        if len(columns[selectedIndex-2]) >= len(columns[selectedIndex])+2:
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-2][len(columns[selectedIndex])+1]:
                                return True
    # 1 in the fourth column
    if selectedIndex >= 3:
        if len(columns[selectedIndex-1]) >= len(columns[selectedIndex])+1:
            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-1][len(columns[selectedIndex])]:
                if len(columns[selectedIndex-2]) >= len(columns[selectedIndex])+2:
                    if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-2][len(columns[selectedIndex])+1]:
                        if len(columns[selectedIndex-3]) >= len(columns[selectedIndex])+3:
                            if columns[selectedIndex][len(columns[selectedIndex])-1] == columns[selectedIndex-3][len(columns[selectedIndex])+2]:
                                return True


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
	


def checkComputerWin():
	# if all 4 discs are in the same columns
    if len(columns[computerChoice]) >= 4:
        if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice][len(columns[computerChoice])-2] == columns[computerChoice][len(columns[computerChoice])-3] == columns[computerChoice][len(columns[computerChoice])-4]:
            return True
    # if marbles horizontally match
    if computerChoice >= 0 and computerChoice <= 3:
        if len(columns[computerChoice]) <= len(columns[computerChoice+1]):
            if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+1]:
                if len(columns[computerChoice+1]) <= len(columns[computerChoice+2]):
                    if rows[5-((len(columns[computerChoice]))-1)][computerChoice+1] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+2]:
                        if len(columns[computerChoice+2]) <= len(columns[computerChoice+3]):
                            if rows[5-((len(columns[computerChoice]))-1)][computerChoice+2] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+3]:
                                return True
    if computerChoice >= 1 and computerChoice <= 4:
        if len(columns[computerChoice]) <= len(columns[computerChoice-1]):
            if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-1]:
                if len(columns[computerChoice]) <= len(columns[computerChoice+1]):
                    if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+1]:
                        if len(columns[computerChoice+1]) <= len(columns[computerChoice+2]):
                            if rows[5-((len(columns[computerChoice]))-1)][computerChoice+1] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+2]:
                                return True
    if computerChoice >= 2 and computerChoice <= 5:
        if len(columns[computerChoice]) <= len(columns[computerChoice-1]):
            if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-1]:
                if len(columns[computerChoice-1]) <= len(columns[computerChoice-2]):
                    if rows[5-((len(columns[computerChoice]))-1)][computerChoice-1] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-2]:
                        if len(columns[computerChoice]) <= len(columns[computerChoice+1]):
                            if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice+1]:
                                return True
    if computerChoice >= 3 and computerChoice <= 6:
        if len(columns[computerChoice]) <= len(columns[computerChoice-1]):
            if rows[5-((len(columns[computerChoice]))-1)][computerChoice] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-1]:
                if len(columns[computerChoice-1]) <= len(columns[computerChoice-2]):
                    if rows[5-((len(columns[computerChoice]))-1)][computerChoice-1] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-2]:
                        if len(columns[computerChoice-2]) <= len(columns[computerChoice-3]):
                            if rows[5-((len(columns[computerChoice]))-1)][computerChoice-2] == rows[5-((len(columns[computerChoice]))-1)][computerChoice-3]:
                                return True
    # diagonally left to right upwards
    # 1 in the first column
    if computerChoice <= 3:
        if len(columns[computerChoice+1]) > len(columns[computerChoice]):
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])]:
                if len(columns[computerChoice+2]) > len(columns[computerChoice+1]):
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+2][len(columns[computerChoice])+1]:
                        if len(columns[computerChoice+3]) > len(columns[computerChoice+2]):
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+3][len(columns[computerChoice])+2]:
                                return True
    # 2 in the second column
    if computerChoice >= 1 and computerChoice <= 4 and len(columns[computerChoice]) >= 2:
        if (len(columns[computerChoice]) - len(columns[computerChoice-1])) <= 1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])-2]:
                if len(columns[computerChoice+1]) > len(columns[computerChoice]):
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])]:
                        if len(columns[computerChoice+2]) > len(columns[computerChoice+1]):
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+2][len(columns[computerChoice])+1]:
                                return True
    # 3 in the third column
    if computerChoice >= 2 and computerChoice <= 5 and len(columns[computerChoice]) >= 3:
        if (len(columns[computerChoice]) - len(columns[computerChoice-1])) <= 1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])-2]:
                if (len(columns[computerChoice]) - len(columns[computerChoice-2])) <= 2:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-2][len(columns[computerChoice])-3]:
                        if len(columns[computerChoice+1]) > len(columns[computerChoice]):
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])]:
                                return True
    # 4 in the fourth column
    if computerChoice >= 3:
        if (len(columns[computerChoice]) - len(columns[computerChoice-1])) <= 1 and len(columns[computerChoice]) >= 4:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])-2]:
                if (len(columns[computerChoice]) - len(columns[computerChoice-2])) <= 2:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-2][len(columns[computerChoice])-3]:
                        if (len(columns[computerChoice]) - len(columns[computerChoice-3])) <= 3:
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-3][len(columns[computerChoice])-4]:
                                return True
    # diagonally left to right downwards
    # 4 in the first column
    if computerChoice <= 3:
        if len(columns[computerChoice]) >= 4 and (len(columns[computerChoice])-len(columns[computerChoice+1])) <= 1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])-2]:
                if (len(columns[computerChoice+1])-len(columns[computerChoice+2])) <= 1:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+2][len(columns[computerChoice])-3]:
                        if (len(columns[computerChoice+2])-len(columns[computerChoice+3])) <= 1:
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+3][len(columns[computerChoice])-4]:
                                return True
    # 3 in the second column
    if computerChoice >= 1 and computerChoice <= 4 and len(columns[computerChoice]) >= 3:
        if (len(columns[computerChoice]) - len(columns[computerChoice+1])) <= 1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])-2]:
                if (len(columns[computerChoice+1]) - len(columns[computerChoice+2])) <= 1:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+2][len(columns[computerChoice])-3]:
                        if len(columns[computerChoice-1]) >= len(columns[computerChoice])+1:
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])]:
                                return True
    # 2 in the third column
    if computerChoice >= 2 and computerChoice <= 5 and len(columns[computerChoice]) >= 2:
        if (len(columns[computerChoice]) - len(columns[computerChoice+1])) <= 1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice+1][len(columns[computerChoice])-2]:
                if len(columns[computerChoice-1]) >= len(columns[computerChoice])+1:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])]:
                        if len(columns[computerChoice-2]) >= len(columns[computerChoice])+2:
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-2][len(columns[computerChoice])+1]:
                                return True
    # 1 in the fourth column
    if computerChoice >= 3:
        if len(columns[computerChoice-1]) >= len(columns[computerChoice])+1:
            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-1][len(columns[computerChoice])]:
                if len(columns[computerChoice-2]) >= len(columns[computerChoice])+2:
                    if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-2][len(columns[computerChoice])+1]:
                        if len(columns[computerChoice-3]) >= len(columns[computerChoice])+3:
                            if columns[computerChoice][len(columns[computerChoice])-1] == columns[computerChoice-3][len(columns[computerChoice])+2]:
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