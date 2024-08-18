import random
from art import logo
import os

# Constants for the number of attempts based on difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """
    Checks the player's guess against the actual answer.

    Parameters:
    guess (int): The player's guess.
    answer (int): The actual number to be guessed.
    turns (int): The number of attempts remaining.

    Returns:
    int: Updated number of attempts remaining.
    """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    """
    Sets the difficulty level based on user input.

    Returns:
    int: The number of attempts based on the chosen difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    

def game():
    """
    Main function to run the Number Guessing Game.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    # Set the number of attempts based on difficulty
    turns = set_difficulty()
    guess = 0

    # Loop until the player guesses the correct number or runs out of attempts
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Main loop to start a new game
while input("Do you want to play the guessing game? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    game()
