# Connect Four MiniMax AI
# CS 51 Final Project
# Evan Sandhoefner, Ryan Kerr, Milan Ravenell, Matthew Tesfalul
# run by typing "python connectfour.py" at command line

first = raw_input("Let's play Connect Four! "
                    "Would you like to go first? (y/n)\n")

def init(first):
  if (first != "y") & (first != "n"):
    first = raw_input("Sorry, I don't understand! Please type 'y' or 'n'\n")
    if (first != "y") and (first != "n"):
      init(first)

init(first)