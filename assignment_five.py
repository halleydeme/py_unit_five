# Halley Deme
# Last Modified: october 27, 2021
# This program is a guessing game where the player tries to guess a random number between 1 and 100.
import random


def get_number():

    k = random.randint(1, 100)

    return k


def get_guess():
    r = 0
    while r<100:
        k = input("Please pick a number between 1 and 100.")
        print(k)


   # for x in range(r < 100 and r > 1):
       # r = int(input("Please guess a number between 1 and 100."))
        #if r < 1 or r > 100:
            #print("Please pick a number between 1 and 100.")


def main():
    get_number()
    get_guess()

main()