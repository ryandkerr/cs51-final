# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

# to be implemented:
# easy/med/hard modes

# import external modules
from time import sleep
from sys import exit

# import our scripts
from evaluate import *
from prototype import *
from board_functions import *

# declare global variables
global playersTurn
global board

# instantiate empty board
board = [['*'] * 6, ['*'] * 6, ['*'] * 6,
         ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6]

# print intro, ask for first player, print starting board,
# assign to playersTurn, call MOVE
def init():
  global playersTurn
  print "\nHello! My name is Rondo. Let's play Connect Four!"
  first = raw_input("You'll be yellow (Y). You can enter 'q' at any prompt "
                    "to quit.\nWould you like to go first? (y/n):\n").lower()
  while (first != "y") & (first != "n") & (first != "q"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()
  if first == "q":
    exit()
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
  if game_won(board, "R"):
    print "\nGame over! I win!"
    exit()
  elif game_won(board, "Y"):
    print "\nGame over! You win!"
    exit()
  elif full(board):
    print "\nGame over! It's a tie!"
    exit()
  elif playersTurn:
    playersTurn = False
    movePlayer()
  else:
    playersTurn = True
    moveAI()

# sleep, assign R to first available cell, print board, call MOVE
def moveAI():
  global board
  print "\nRondo is thinking...."
  sleep(1)
  for column in range(7):
    for row in range(6):
      if board[column][row] == "*":
        board[column][row] = "B"
        print "Rondo's move:"
        printBoard()
        move()
        break
  # we want it to be like below, but needs more debugging
  """board = go_next(board, 2, "R")
  print "Rondo's move:"
  printBoard()
  move()"""

# take user column input, alter board in memory, print board, call MOVE
def movePlayer():
  column = raw_input("\nYour turn! Please choose a column (0-6):\n").lower()
  if column not in ['q','0','1','2','3','4','5','6']:
    movePlayer()
  elif column == 'q':
    exit()
  else:
    column = int(column)
    for row in range(6):
      if board[column][row] == "*":
        board[column][row] = "Y"
        print "\nYour move:"
        printBoard()
        move()
        break
    else:
      movePlayer()

# print ASCII board to terminal window
def printBoard():
  print "0 1 2 3 4 5 6"
  for row in [5,4,3,2,1,0]:
    for column in range(6):
      print board[column][row],
    print board[6][row]

init()