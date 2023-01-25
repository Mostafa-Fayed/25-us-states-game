from turtle import Turtle


class StatesText(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_answer(self, x, y, state_name):
        self.goto(x, y)
        self.write(state_name)
