# -*- coding: cp1252 -*-

from random import randint
import sys


def guessgame():
    number = randint(0,2)
    number0 = "Foot"
    number1 = "Cockroach"
    number2 = "Nuke"

    while True:

        guess = input("Foot, Nuke or Cockroach? (Quit ends):")
        if guess < 0:
            print("Incorrect selection.")
            sys.exit(0)
        if guess == "Quit":
            print("")
            break
        elif guess == 