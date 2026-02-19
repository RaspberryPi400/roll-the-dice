# Import dependencies
import random
import sys
# Make a list of numbers on dice
dice = [1, 2, 3, 4, 5, 6]

# Start outer while loop - to be used for rolling again
running = True
while running:
    # Start inner while loop
    rolling = True
    while rolling:
        # Choose a random number on a die
        number = random.choice(dice)
        # Print the chosen number
        print(f"You rolled a {number}.")
        # Ask if the user wants to roll again
        again = input("Roll again? ('y'/'n'): ")
        # If the user wants to roll again, restart the inner while loop and choose the random number again.
        if again == "y":
            break
        # If the user does not want to roll again, exit the program.
        elif again == "n":
            print("Exiting...")
            sys.exit(0)