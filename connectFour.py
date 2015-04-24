# connectFour.py
# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

from time import sleep
from sys import exit

global playersTurn
global board

board = [['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6, ['*'] * 6]

gameOver = False

# to be implemented:
# easy/med/hard modes
# quit

def init():
  global playersTurn
  print "\nHello! My name is Rondo."
  first = raw_input("Let's play Connect Four! You'll be red (R). "
                    "Would you like to go first? (y/n):\n").lower()
  while (first != "y") & (first != "n"):
    first = raw_input("\nSorry, I don't understand! "
                      "Please type 'y' or 'n':\n").lower()
  print '\nStarting board:'
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

def moveAI():
  print "\nRondo is thinking...."
  sleep(2)
  for column in range(7):
    for row in range(6):
      if board[column][row] == "*":
        board[column][row] = "R"
        print "Rondo's move:"
        printBoard()
        move()
        break

def movePlayer():
  column = raw_input("\nYour turn! Please choose a column (0-6):\n")
  if column not in ['0','1','2','3','4','5','6']:
    movePlayer()
  else:
    column = int(column)
    for row in range(6):
      if board[column][row] == "*":
        board[column][row] = "R"
        print "\nYour move:"
        printBoard()
        move()
        break
    else:
      movePlayer()

def printBoard():
  print "0 1 2 3 4 5 6"
  for row in [5,4,3,2,1,0]:
    for column in range(6):
      print board[column][row],
    print board[6][row]

init()