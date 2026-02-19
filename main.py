# Import dependencies
import random
import sys
# Make a list of numbers on dice
dice = [1, 2, 3, 4, 5, 6]
# Make another list for rolling two dice
dice_2 = [1, 2, 3, 4, 5, 6]

# Ask user if they want to roll one die or two
xy = input("Do you want to: (1. Roll one die) or (2. Roll two dice): ")

# If user says one, start outer while loop - to be used for rolling again
if xy == "1":
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

# If user wants to roll two dice, start outer while loop - to be used for rolling again
elif xy == "2":
    running = True
    while running:
        # Start inner while loop
        rolling = True
        while rolling:
            # Choose two random numbers
            number = random.choice(dice)
            number_2 = random.choice(dice_2)
            # Print the two numbers chosen
            print(f"You rolled a {number} and a {number_2}.")
            # Ask if the user wants to roll again
            again = input("Roll again? ('y'/'n'): ")
            # If user does, restart the loop. The outer while loop helps to do this.
            if again == "y":
                break
            # If the user does not want to roll again, exit the program.
            elif again == "n":
                print("Exiting...")
                sys.exit(0)

# If the user does not type 1 or 2 then exit the system and tell them to run the code again.
else:
    print("Please choose 1 or 2. Run the code again.")
    print("Exiting...")
    sys.exit(0)
