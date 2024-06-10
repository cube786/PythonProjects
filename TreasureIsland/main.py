print("\n"
      "*******************************************************************************\n"
      "          |                   |                  |                     |\n"
      " _________|________________.=\"\"_;=.______________|_____________________|_______\n"
      "|                   |  ,-\"_,=\"\"     `\"=.|                  |\n"
      "|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n"
      "          |                `\"=._o`\"=._      _`\"=._                     |\n"
      " _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n"
      "|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n"
      "|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n"
      "          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n"
      " _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______\n"
      "|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n"
      "|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n"
      "____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____\n"
      "/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_\n"
      "____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n"
      "/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n"
      "____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____\n"
      "/______/______/______/______/______/______/______/______/______/______/[TomekK]\n"
      "*******************************************************************************\n")

print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")

choice1 = input("You have reached a crossroads.Do you want to go left or right?: ").lower()

if choice1 == 'left':
    choice2 = input("You have reached a lake.Do you want to swim across or wait for a boat? swim/wait: ").lower()
    if choice2 == 'wait':
        choice3 = input(
            "You have arrived at a house. there are three doors to open the house. so Red , Yellow or Blue?: ").lower()
        if choice3 == 'yellow':
            print("You found the treasure. You won!")
        elif choice3 == "red":
            print("It's a room full of fire.Game over")
        elif choice3 == 'blue':
            print("You enter a room full of beasts. GameOver")
        else:
            print('You chose a door that doesnt exist.Game over')
    else:
        print("You got attacked by a angry trout.Game Over")
else:
    print("Game Over")