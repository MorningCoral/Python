import math
import random

board = []
ROW = 3
COL = 3
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
    if who == "cp":
        symbol = "O"
    elif who == "player":
        symbol = "X"
    board[math.ceil(pos / 3) - 1][(pos % 3 - 1)] = symbol
    display()
    
def win_lose():
    for i in range (3):
        # row, column, diagonal
        if (board[i][0] == board[i][1] == board[i][2]) or (board[0][i] == board[1][i] == board[2][i]) or \
        (board[0][0] == board[1][1] == board[2][2]) or board[0][2] == board[1][1] == board[2][0]:
            print(player_count, cp_count)
            if player_count > cp_count:
                print("You Win!")
            else:
                print("You Lose!")
            return True
    return False

## main
initialise()
display()
over = False
player_count = 0
cp_count = 0
count = 0
while not over:
    # human move
    print("Player Turn")
    valid_move = False
    while not valid_move:
        move = input("Enter a move (1-9): ")
        if len(move) == 0: # presence check
            print("Please enter something")
        elif not move.isdigit(): # data type check
            print("Move must be an integer.")
        elif not 1 <= int(move) <= 9: # range check
            print("Move must be an integer from 1 to 9.")
        elif int(move) != board[math.ceil(int(move) / 3) - 1][(int(move) % 3 - 1) % 3]:
            print("Position already occupied.")
        else:
            valid_move = True
    update_board(int(move), "player")
    player_count += 1

    # check win lose
    if win_lose() == True:
        break
    
    # check draw
    if player_count == 5:
        print("Draw")
        over = True
        
    # computer move
    print("Computer Turn")
    cp_move_valid = False
    while not cp_move_valid:
        cp_move = random.randint(1,9)
        if cp_move == board[math.ceil(cp_move / 3) - 1][(cp_move % 3 - 1) % 3]:
            cp_move_valid = True
    update_board(cp_move, "cp")
    cp_count += 1
    
    #check win lose
    over = win_lose()
    
    
    
