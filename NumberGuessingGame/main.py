import random
from art import logo

number = random.randint(1, 100)

EASY_MODE = 10
HARD_MODE = 5


def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_MODE
    elif level == 'hard':
        return HARD_MODE


def check_answer(guess, number, turns):
    if guess < number:
        print("Too low")
        return turns - 1
    elif guess > number:
        print("Too high")
        return turns - 1
    elif guess == number:
        print(f"You got it! The answer was {number}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"The correct answer is {number}")

    attempts = difficulty_level()

    guess = 0
    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again.")


game()