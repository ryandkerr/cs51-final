# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

# to be implemented:
# easy/med/hard modes
# consistent ''/""
# abstraction/factoring/etc

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

# instantiate empty board
board = [['.'] * 6, ['.'] * 6, ['.'] * 6,
         ['.'] * 6, ['.'] * 6, ['.'] * 6, ['.'] * 6]

# print intro, ask for first player, print starting board,
# assign to playersTurn, call move()
def init():
  global playersTurn
  print "\nHello! My name is Rondo. Let's play Connect Four!"
  first = raw_input("You'll be yellow (Y). You can enter 'q' at any prompt "
                    "to quit.\nWould you like to go first? (y/n):\n").lower()
  while (first != "y") & (first != "n") & (first != "q"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()
  if first == 'q':
    sys.exit()
  print '\nStarting board:'
  printBoard()
  if first == "n":
    playersTurn = False
  else:
    playersTurn = True
  move()

# check for gameOver, reassign playersTurn, call moveAI or movePlayer
def move():
  global playersTurn
  global board
  for row in range(ROWS):
    for column in range(COLUMNS):
      if board[column][row] == "R":
        board[column][row] = "r"
      if board[column][row] == "Y":
        board[column][row] = "y"
  if game_won(board, "R"):
    print "\nGame over! I win!"
    sys.exit()
  elif game_won(board, "Y"):
    print "\nGame over! You win!"
    sys.exit()
  elif full(board):
    print "\nGame over! It's a tie!"
    sys.exit()
  elif playersTurn:
    playersTurn = False
    movePlayer()
  else:
    playersTurn = True
    moveAI()

# sleep(?), assign R to first available cell, print board, call MOVE
def moveAI():
  global board
  print "\nRondo is thinking...."
  # time.sleep(1)
  board = go_next(board, minimax_ab(board, 3, "R"), "R")
  print "Rondo's move:"
  printBoard()
  move()
  

# take user column input, alter board in memory, print board, call MOVE
def movePlayer():
  column = raw_input("\nYour turn! Please choose a column (1-7):\n").lower()
  if column not in ['q','1','2','3','4','5','6','7']:
    movePlayer()
  elif column == 'q':
    sys.exit()
  else:
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
  print ''
  for row in range(ROWS):
    for column in range(COLUMNS):
      print board[column][ROWS - row - 1],
    print ''

init()