from turtle import Turtle, Screen
import pandas as pd
import states

# Declaring Objects
screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
us_map = Turtle(shape="blank_states_img.gif")
df = pd.read_csv("50_states.csv")
states_list = df.state.tolist()
x_coordinates = df.x.tolist()
y_coordinates = df.y.tolist()

state = states.StatesText()

guessed_states = []


while len(guessed_states) <= 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 states guessed", prompt="What's another state's name?").title()
    if user_answer == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        df = pd.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break

    if user_answer in states_list:
        if user_answer not in guessed_states:
            answer = user_answer
            answer_index = states_list.index(user_answer)
            state.write_answer(x_coordinates[answer_index], y_coordinates[answer_index], answer)
            guessed_states.append(answer)

    else:
        continue

