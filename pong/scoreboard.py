from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-120, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(120, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))
