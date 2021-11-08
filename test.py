import random
columns = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [], []


def computerPlays():
    computerChoice = random.randint(0, 6)
    while len(columns[computerChoice]) >= 6:
        computerChoice = random.randint(0, 6)
    columns[computerChoice].insert(0, "O")


computerPlays()
print(columns)
