import random

print("Welcome to the dice game!")

while True:

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)

    print("Dice 1:", dice1)

    print("Dice 2:", dice2)

    print("Dice 3:", dice3)

    print("Total:", dice1 + dice2 + dice3)

    print("Do you want to play again? (y/n)")

    answer = input()

    if answer == "y":

        continue

    elif answer == "n":

        print("Thanks for playing!")

        break

    else:

        print("Please enter a valid answer.")

        continue
