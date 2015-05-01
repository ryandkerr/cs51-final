# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

# import external modules
import time
import sys

# import our scripts
from evaluate import *
from ab_pruning import *
from board_functions import *

# declare global variables
global playersTurn
global board
global difficulty

# instantiate empty board
board = [["." for row in range(ROWS)] for column in range(COLUMNS)]

# take input originating from user, exit program if input is "q"
def exit_if(user_input):
  if user_input == "q":
    sys.exit()

# print intro text, ask for first player and difficulty, print starting board,
# call move()
def init():
  global playersTurn
  global difficulty

  print "\nHello! My name is Rondo. Let's play Connect Four!"

  first = raw_input("You'll be yellow (Y). You can enter 'q' at any prompt "
                    "to quit.\nWould you like to go first? (y/n):\n").lower()
  while (first != "y") & (first != "n") & (first != "q"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()

  exit_if(first)

  if first == "n":
    playersTurn = False
  else:
    playersTurn = True

  difficulty = raw_input("\nI'm pretty good at this, so you might want me to "
                         "go easy.\nPlease choose a difficulty from 1 "
                         "(easiest) to 5 (hardest).\nFair warning: when I play"
                         " hard, my turns take a while.\n").lower()
  while difficulty not in ["1","2","3","4","5","q"]:
    difficulty = raw_input("\nSorry, I don't understand! Please"
                           " type '1', '2', '3', '4', or '5'.\n").lower()

  exit_if(difficulty)

  difficulty = int(difficulty)

  print "\nStarting board:"
  printBoard()

  move()


# check for game over, make last move lowercase, reassign playersTurn,
# call moveAI or movePlayer
def move():
  global playersTurn
  global board

  if game_won(board, "R"):
    print "\nGame over! I win!"
    sys.exit()
  elif game_won(board, "Y"):
    print "\nGame over! You win!"
    sys.exit()
  elif full(board):
    print "\nGame over! It's a tie!"
    sys.exit()

  for row in range(ROWS):
    for column in range(COLUMNS):
      if board[column][row] == "R":
        board[column][row] = "r"
      if board[column][row] == "Y":
        board[column][row] = "y"

  if playersTurn:
    playersTurn = False
    movePlayer()
  else:
    playersTurn = True
    moveAI()


# sleep if Rondo too fast, compute Rondo's optimal move, print board,
# call move()
def moveAI():
  global board

  print "\nRondo is thinking...."

  if difficulty < 4:
    time.sleep(1)

  board = go_next(board, minimax_ab(board, difficulty, "R"), "R")

  print "Rondo's move:"
  printBoard()

  move()
  

# take user column input, alter board in memory, print board, call move()
def movePlayer():
  column = raw_input("\nYour turn! Please choose a column (1-7):\n").lower()
  while column not in ["q","1","2","3","4","5","6","7"]:
    column = raw_input("\nSorry, I don't understand! Please type '1', '2',"
                       " '3', '4', '5', '6', or '7'.\n")

  exit_if(column)

  column = int(column) - 1

  for row in range(ROWS):
    if board[column][row] == ".":
      board[column][row] = "Y"
      print "\nYour move:"
      printBoard()
      move()
      break
  else:
    movePlayer()


# print ASCII board to terminal window
def printBoard():
  for column in range(COLUMNS):
    print str(1 + column),
  print ""

  for row in range(ROWS):
    for column in range(COLUMNS):
      print board[column][ROWS - row - 1],
    print 

init()