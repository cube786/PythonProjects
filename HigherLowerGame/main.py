from game_data import data
from art import logo, vs
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account_data):
    acc_name = account_data['name']
    acc_description = account_data['description']
    acc_country = account_data['country']
    return f"{acc_name}, a{acc_description}, from{acc_country}."


def compare(guess,a_count,b_count):
    if a_count > b_count:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_on = True
second_choice = random.choice(data)
while game_on:

    first_choice = second_choice
    second_choice = random.choice(data)
    while first_choice == second_choice:
        second_choice = random.choice(data)
    a_follower_count = first_choice['follower_count']
    b_follower_count = second_choice['follower_count']

    print(f"Compare A: {format_data(first_choice)}")
    print(vs)
    print(f"Against B: {format_data(second_choice)}")

    ask = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_guess = compare(ask, a_follower_count, b_follower_count)
    cls()
    print(logo)
    if is_guess:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_on = False
        print(f"You're wrong. Final score: {score} ")