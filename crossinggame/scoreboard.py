from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-265, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)
        self.goto(-265, 225)
        self.write(f"score:{self.score}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1

    def win(self):
        self.clear()
        self.score += 1
        self.level += 1
        self.goto(-265, 250)
        self.write(f"Level {self.level}", align="left", font=FONT)
        self.goto(-265, 225)
        self.write(f"score:{self.score}", align="left", font=FONT)

    def lose(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 36, "normal"))
