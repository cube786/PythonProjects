import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

new_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("invalid choice , you lose")
else:
    print(new_list[user_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer chose:\n{new_list[computer_choice]}")
    if user_choice == computer_choice:
        print("it's a draw")
    elif computer_choice > user_choice:
        print("You lose")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice == 2 and user_choice == 0:
        print("You win")
    elif user_choice > computer_choice:
        print("You win")





