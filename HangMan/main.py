from art import logo, stages
from words import word_list
import random


chosen_word = random.choice(word_list)
display = []
lives = 6
print(chosen_word)
for _ in range(len(chosen_word)):
    display += '_'
game_on = True
while game_on:
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"{guess} is already guessed ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            game_on = False

    print(' '.join(display))

    if '_' not in display:
        print("You won")
        game_on = False

    print(stages[lives])