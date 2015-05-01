# cpuFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python cpufour.py" at command line

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
board = [["." for y in range(ROWS)] for x in range(COLUMNS)]

# takes input originating from user, exits program if input is "q"
def quit_if(user_input):
  if user_input == "q":
    sys.exit()

# print intro, ask for first player, ask cpu difficulty, print starting board,
# assign to ai2_turn, call move(diff1, diff2)
def init():
  global ai2_turn
  print ("\nHello! My name is Rondo. I'm about to play Connect Four with my"
         " friend Carlisle.")
  first = raw_input("Carlisle will be yellow (Y)."
                    "\nShould he go first? (y/n):\n").lower()
  while (first != "y") & (first != "n") & (first != "q"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()
  quit_if(first)
  difficulty1 = raw_input("What difficulty should Rondo be? "
                          " Choose a number 1 (easy) - 5 (hard):\n").lower()
  while difficulty1 not in ["1","2","3","4","5","q"]:
    difficulty1 = raw_input("\nSorry, I don't understand! "
                      "Please type a number 1-5:\n").lower()

  difficulty2 = raw_input("What difficulty should Carlisle be? "
                          " Choose a number 1 (easy) - 5 (hard):\n").lower()
  quit_if(difficulty1)
  while difficulty2 not in ["1","2","3","4","5","q"]:
    difficulty2 = raw_input("\nSorry, I don't understand! "
                      "Please type a number 1-5:\n").lower()
  quit_if(difficulty2)
  difficulty1 = int(difficulty1)
  difficulty2 = int(difficulty2)
  print '\nStarting board:'
  printBoard()
  if first == "n":
    ai2_turn = False
  else:
    ai2_turn = True
  move(difficulty1, difficulty2)

# check for game over, change last move to lowercase,
# reassign ai2_turn, call moveAI1 or moveAI2
def move(diff1, diff2):
  global ai2_turn
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
  if ai2_turn:
    ai2_turn = False
    moveAI2(diff1, diff2)
  else:
    ai2_turn = True
    moveAI1(diff1, diff2)

# sleep if AI too fast, compute optimal move & modify board in memory,
# print board, call move()
def moveAI1(diff1, diff2):
  global board
  print "\nRondo is thinking...."
  if diff1 < 4:
    time.sleep(1)
  board = go_next(board, minimax_ab(board, diff1, "R"), "R")
  print "Rondo's move:"
  printBoard()
  move(diff1, diff2)
  

# sleep if AI too fast, compute optimal move & modify board in memory,
# print board, call move()
def moveAI2(diff1, diff2):
  global board
  print "\nCarlisle is thinking...."
  if diff2 < 4:
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