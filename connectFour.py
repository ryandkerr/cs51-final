# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

global playersTurn
global board

board = [['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6]

gameOver = False

#easy/med/hard modes

def init():
  global playersTurn
  first = raw_input("Let's play Connect Four! "
                    "Would you like to go first? (y/n):\n")
  if (first != "y") & (first != "n"):
    first = raw_input("Sorry, I don't understand! Please type 'y' or 'n':\n")
    if (first != "y") and (first != "n"):
      init(first)
  print "Okay, you'll be red (R).\n"
  printBoard()
  if first == "n":
    playersTurn = False
  else:
    playersTurn = True
  move()

def move():
  global playersTurn
  if gameOver:
    print "Game over! Somebody wins!"
  elif playersTurn:
    playersTurn = False
    movePlayer()
  else:
    playersTurn = True
    moveAI()

def movePlayerHelp():
  printBoard()
  move()

def movePlayer():
  column = raw_input("Please choose a column (0-6):\n")
  if column not in ['0','1','2','3','4','5','6']:
    movePlayer()
  else:
    column = int(column)
    for row in [0,1,2,3,4,5]:
      if board[column][row] == "*":
        board[column][row] = "R"
        movePlayerHelp()
        break
    else:
      movePlayer()

def moveAI():
  print "AI's move"
  move()

def printBoard():
  print "0 1 2 3 4 5 6"
  for row in [5,4,3,2,1,0]:
    for column in range(6):
      print board[column][row],
    print board[6][row]

init()