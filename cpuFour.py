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
# assign to ai2_turn, call move(diff1, diff2)
def init():
  global ai2_turn
  print "\nHello! My name is Rondo. Let's play Connect Four!"
  first = raw_input("Carlisle will be yellow (Y)."
                    "\nShould he go first? (y/n):\n").lower()
  while (first != "y") & (first != "n") & (first != "q"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()
  if first == 'q':
    sys.exit()
  difficulty1 = raw_input("What difficulty should Rondo be? "
                          " Choose a number 1 (easy) - 5 (hard):\n").lower()
  while (difficulty1 > 5) & (difficulty1 < 1):
    difficulty1 = raw_input("\nSorry, I don't understand! "
                      "Please type a number 1-5:\n").lower()

  difficulty2 = raw_input("What difficulty should Carlisle be? "
                          " Choose a number 1 (easy) - 5 (hard):\n").lower()
  while (difficulty2 > 5) & (difficulty2 < 1):
    difficulty2 = raw_input("\nSorry, I don't understand! "
                      "Please type a number 1-5:\n").lower()
  difficulty1 = int(difficulty1)
  difficulty2 = int(difficulty2)
  print difficulty1
  print difficulty2
  print '\nStarting board:'
  printBoard()
  if first == "n":
    ai2_turn = False
  else:
    ai2_turn = True
  move(difficulty1, difficulty2)

# check for gameOver, reassign ai2_turn, call moveAI1 or moveAI2
def move(diff1, diff2):
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
    moveAI2(diff1, diff2)
  else:
    ai2_turn = True
    moveAI1(diff1, diff2)

# sleep(?), assign R to first available cell, print board, call MOVE
def moveAI1(diff1, diff2):
  global board
  print "\nRondo is thinking...."
  time.sleep(1)
  board = go_next(board, minimax_ab(board, diff1, "R"), "R")
  print "Rondo's move:"
  printBoard()
  move(diff1, diff2)
  

# take user column input, alter board in memory, print board, call MOVE
def moveAI2(diff1, diff2):
  global board
  print "\nCarlisle is thinking...."
  time.sleep(1)
  board = go_next(board, minimax_ab(board, diff2, "Y"), "Y")
  print "Carlisle's move:"
  printBoard()
  move(diff1, diff2)

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