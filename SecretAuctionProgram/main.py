from replit import clear
from art import logo
import os


print(logo)
print("Welcome to the secret Auction program.")

new_dict = {}


def cls():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):
    high_bid = 0
    winner = ""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > high_bid:
            high_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}")


game_on = True
while game_on:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))

    new_dict[name] = bid

    restart = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if restart == "no":
        cls()
        game_on = False
        find_highest_bidder(new_dict)
    elif restart == 'yes':
        cls()