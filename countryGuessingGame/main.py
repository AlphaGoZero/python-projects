import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer = screen.textinput(title=f"{len(guessed_state)}/50 states guessed", prompt="What's another state's name?")\
        .title()
    if answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_missing.csv")
        print(missing_state)
        break

    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        right_state = data[data.state == answer]
        t.goto(int(right_state.x), int(right_state.y))
        t.write(right_state.state.item())
        guessed_state.append(right_state.state.item())

screen.exitonclick()
