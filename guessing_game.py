# Number Guessing Game
# The computer picks a random number, you try to guess it!

import random  # This gives us access to random number functions

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10...")
print("Can you guess it?")

# Get the player's guess
guess = input("Enter your guess: ")  # input() waits for the user to type something
guess = int(guess)  # Convert the text input to a number

# Check if they got it right
if guess == secret_number:
    print("Correct! You got it!")
elif guess < secret_number:
    print(f"Too low! The number was {secret_number}")
else:
    print(f"Too high! The number was {secret_number}")
