# Halley Deme
# Last Modified: october 27, 2021
# This program is a guessing game where the player tries to guess a random number between 1 and 100.
import random







def get_number():
    """

    :return: This returns a random number.
    """
    k = random.randint(1, 100)

    return k


def get_guess():
    """

    :return: This runs a while loop to make sure the number is between the given parameters and returns a guess from the user.
    """
    k = 0
    while k > 100 or k <1:
        k = int(input("Please pick a number between 1 and 100."))
    return k



def play(k):
    """

    :param k: The random number.
    :return: This tells the user if their guess is too high or too low. It also adds the total number of tries.
    """

    tries = 0
    while True:
        t = get_guess()
        tries += 1

        if t == k:
            print("You got it in " + str(tries) + " tries")
            return tries

        if t > k:
            print("your guess is too high")
        if k > t:
            print(" your guess is too low")
def main():
    total_guess= 0
    for x in range(3):
        k = get_number()
        total_guess += play(k)
    l = total_guess / 3
    print("your average number of guesses was " + str(l), "Thank you for playing! Have a great day.")



main()