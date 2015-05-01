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
global ai2_turn
global board

# instantiate empty board
board = [['.'] * 6, ['.'] * 6, ['.'] * 6,
         ['.'] * 6, ['.'] * 6, ['.'] * 6, ['.'] * 6]

# print intro, ask for first player, print starting board,
# assign to ai2_turn, call move()
def init():
  global ai2_turn
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
    ai2_turn = False
  else:
    ai2_turn = True
  move()

# check for gameOver, reassign ai2_turn, call moveAI1 or moveAI2
def move():
  global ai2_turn
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
  elif ai2_turn:
    ai2_turn = False
    moveAI2()
  else:
    ai2_turn = True
    moveAI1()

# sleep(?), assign R to first available cell, print board, call MOVE
def moveAI1():
  global board
  print "\nRondo is thinking...."
  time.sleep(1)
  board = go_next(board, minimax_ab(board, 3), "R")
  print "Rondo's move:"
  printBoard()
  move()
  

# take user column input, alter board in memory, print board, call MOVE
def moveAI2():
  global board
  print "\nCarlisle is thinking...."
  time.sleep(1)
  board = go_next(board, minimax_ab(board, 3), "Y")
  print "Rondo's move:"
  printBoard()
  move()

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