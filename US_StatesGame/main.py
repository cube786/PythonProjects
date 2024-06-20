import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
correct_ans = data.state.to_list()
correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/ 50 States Correct",
                                    prompt="What's another state").title()
    if answer_state == 'Exit':
        missing_state = []
        for state in correct_ans:
            if state not in correct_guess:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('states_to_learn')
        break
    if answer_state in correct_ans:
        correct_guess.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)