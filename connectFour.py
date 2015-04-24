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
  sleep(1.5)
  for column in range(7):
    for row in range(6):
      if board[column][row] == "*":
        board[column][row] = "R"
        print "Rondo's move:"
        printBoard()
        move()
        break

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

def printBoard():
  print "0 1 2 3 4 5 6"
  for row in [5,4,3,2,1,0]:
    for column in range(6):
      print board[column][row],
    print board[6][row]

init()