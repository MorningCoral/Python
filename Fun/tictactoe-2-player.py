import math
import random

board = []
ROW = 3
COL = 3
available = [i for i in range(1,10)]
def initialise():
    i = 1
    for row in range(ROW):
        board.append([])
        for col in range(COL):
            board[row].append(i)
            i += 1

def display():
    for row in range(ROW):
        for col in range(COL):
            print(board[row][col], end='')
        print()

def update_board(pos, who):
    symbol = None
    if who == "p1":
        symbol = "O"
    elif who == "p2":
        symbol = "X"
    board[math.ceil(pos / 3) - 1][(pos % 3 - 1)] = symbol
    available.remove(pos)
    display()

def win_lose():
    for i in range (3):
        # row, column, diagonal
        if (board[i][0] == board[i][1] == board[i][2]) or (board[0][i] == board[1][i] == board[2][i]) or \
        (board[0][0] == board[1][1] == board[2][2]) or board[0][2] == board[1][1] == board[2][0]:
            return True
    return False

def get_move(who):
    valid_move = False
    while not valid_move:
        move = input(who+"'s turn. Enter a move (1-9): ")
        if len(move) == 0: # presence check
            print("Please enter something")
        elif not move.isdigit(): # data type check
            print("Input must be an number.")
        elif not 1 <= int(move) <= 9: # range check
            print("Move must be a number from 1 to 9.")
        elif int(move) != board[math.ceil(int(move) / 3) - 1][(int(move) % 3 - 1) % 3]:
            print("Position already occupied.")
        else:
            valid_move = True
    return int(move)

## main
initialise()
display()
game_over = False
player_count = 0
cp_count = 0

while not game_over:
    # Player 1
    move = get_move("Player 1")
    update_board(int(move), "p1")

    # check draw
    if len(available) == 0:
        print("Draw")
        game_over = True
        
    # check win lose
    if win_lose() == True:
        print("Player 1 wins!")
        break

    # Player 2
    move = get_move("Player 2")
    update_board(int(move), "p2")

    # check win lose
    if win_lose() == True:
        print("Player 2 wins!")
        over = True
        

    

    

