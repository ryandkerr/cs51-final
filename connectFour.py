# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

global playersTurn
global board

first = raw_input("Let's play Connect Four! "
                    "Would you like to go first? (y/n):\n")

#easy/med/hard modes

gameOver = False

def init(first):
  if (first != "y") & (first != "n"):
    first = raw_input("Sorry, I don't understand! Please type 'y' or 'n':\n")
    if (first != "y") and (first != "n"):
      init(first)
  print "Okay, you'll be red (R).\n"
  printBoard(board)

def move(playersTurn):
  if gameOver:
    print "Game over! Somebody wins!"
  elif playersTurn:
    playersTurn = False
    movePlayer(playersTurn)
  else:
    playersTurn = True
    moveAI(playersTurn)

def movePlayerHelp():
  printBoard(board)
  move(False)

def movePlayer(playersTurn):
  cell = raw_input("Please choose a column (0-6):\n")
  if cell not in ['0','1','2','3','4','5','6']:
    movePlayer(False)
  else:
    cell = int(cell)
    if board[5][cell] == "*":
      board[5][cell] = "R"
      movePlayerHelp() 
    elif board[4][cell] == "*":
      board[4][cell] = "R"
      movePlayerHelp()
    elif board[3][cell] == "*":
      board[3][cell] = "R"
      movePlayerHelp()
    elif board[2][cell] == "*":
      board[2][cell] = "R"
      movePlayerHelp()
    elif board[1][cell] == "*":
      board[1][cell] = "R"
      movePlayerHelp()
    elif board[0][cell] == "*":
      board[0][cell] = "R"
      movePlayerHelp()
    else:
      movePlayer(False)

def moveAI(playersTurn):
  print "AI's move"
  move(playersTurn)

a = ["*", "*", "*", "*", "*", "*", "*"]
b = ["*", "*", "*", "*", "*", "*", "*"]
c = ["*", "*", "*", "*", "*", "*", "*"]
d = ["*", "*", "*", "*", "*", "*", "*"]
e = ["*", "*", "*", "*", "*", "*", "*"]
f = ["*", "*", "*", "*", "*", "*", "*"]

board = [a, b, c, d, e, f]

rowNames = ["a", "b", "c", "d", "e", "f"]

def printBoard(board):
  print "  0 1 2 3 4 5 6"
  numRow = 0
  for row in board:
    print (rowNames[numRow] + " " + row[0] + " " + row[1] + " " + row[2] + " " +
           row[3] + " " + row[4] + " " + row[5] + " " + row[6])
    numRow += 1

init(first)

if first == "n":
  playersTurn = False
else:
  playersTurn = True

move(playersTurn)