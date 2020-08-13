# Battleship game

from random import randint

# create board
ROW = 5
COL = 5
board = [["0" for COL in range(COL)] for row in range(ROW)]

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

# generate random battleship position
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

CHANCES = 4

for turn in range(CHANCES): # 4 chances
  print ("Turn", turn + 1) # indicates turn num
  thisturn = True
  while thisturn:
    guess_row = input("Guess Row (0-4): ") # player guess
    guess_col = input("Guess Col (0-4): ")
    
    if len(guess_row) == 0 or len(guess_col)== 0:
      print("Missing coordinates.")
    elif int(guess_row) not in range(ROW) or int(guess_col) not in range(COL):
      print("Oops, out of range.")
    elif board[int(guess_row)][int(guess_col)] == "X":
      print( "You guessed that one already." )
    else:
      thisturn = False
  guess_row = int(guess_row)    
  guess_col = int(guess_col)
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")  # correct guess
    break
  else:
    print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    if (turn == CHANCES - 1):
      print ("Game Over")
      board[ship_row][ship_col] = "S" # reveal answer
      print_board(board)
    else:
      print_board(board) # show status of board

# improvements:
# multiple battleships + bigger board - no overlap
# diff size battleship - connecting sides, no lying off board
# two player



