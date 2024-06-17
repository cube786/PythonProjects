from turtle import Turtle, Screen
import random

game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color Turtle will win the race? ")
colors = ['red', 'yellow', 'green', 'blue', 'orange', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle('turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-230, y_pos[turtle_index])
    all_turtle.append(tim)

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner")
        else:
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)













screen.exitonclick()