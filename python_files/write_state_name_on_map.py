from turtle import Turtle, Screen


class StateOnMap(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


    def show_state_name(self, name, x, y):
        self.goto(x, y)
        self.write(name)
