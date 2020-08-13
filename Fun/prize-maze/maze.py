from random import randint
### Task 4.1 - Read and display maze ###
maze = []
try:
    infile = open("MAZE.TXT", 'r')
    for line in infile:
        row = []
        for char in line.rstrip():
            if char == 'P' or char == 'O':
                char = '.'
            row.append(char)
        maze.append(row)

except FileNotFoundError:
    print("MAZE.TXT not found")

def displayMaze(maze):
    for row in maze:
        for char in row:
            print(char, end='')
        print()
    print()

### Task 4.2 - place prize in random position ###
placed = False
while not placed:
    randRow = randint(0,10)
    randCol = randint(0, 9)
    # check random position is empty
    if maze[randRow][randCol] == '.': 
        maze[randRow][randCol] = 'P'
        placed = True

### Task 4.3 and 4.4 ###

# Starting position of player
playerX = 4
playerY = 5

# place player
maze[playerY][playerX] = 'O'










# move player
def movePlayer(playerX, playerY, move, maze):
    moveX, moveY = playerX, playerY
    # next positions based on input directions
    if move == 'U':
        moveY -= 1
    elif move == 'D':
        moveY += 1
    elif move == 'L':
        moveX -= 1
    elif move == 'R':
        moveX += 1

    # if next position is wall
    if maze[moveY][moveX] == "X":
        # display
        displayMaze(maze)
        return playerX, playerY, False, maze

    # if next position is empty
    elif maze[moveY][moveX]  == '.':
        # change curr pos to empty
        maze[playerY][playerX] = '.'
        # move player to next pos
        maze[moveY][moveX] = 'O'
        # display
        displayMaze(maze)
        return moveX, moveY, False, maze

    # if next position is prize position
    elif maze[moveY][moveX]  == 'P':
        print("Player has reached the prize")
        return moveX, moveY, True, maze

# main
displayMaze(maze)
win = False     # game state
prevMove = None # previous move

while not win:
    move = input("Your move (U,D,L,R or Enter to use prev move): ") # get input
    if move in ['','U','D','L','R']: # valid input
        if move == "":
            playerX, playerY, win, maze = movePlayer(playerX, playerY, prevMove, maze)
        else:
            playerX, playerY, win, maze = movePlayer(playerX, playerY, move, maze)
            prevMove = move
    else: # invalid input
        print("Invalid input")
