from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(False)
        self.hideturtle()
        self.penup()
        self.goto(-700, 380)
        self.score = 1
        self.lives = 3
        self.screen.tracer(True)
        self.print_score()

    def increase_score(self):
        self.score += 1

    def reduce_lives(self):
        self.lives -= 1

    def print_score(self):
        self.clear()
        self.screen.tracer(False)
        self.pendown()
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)
        self.penup()
        self.goto(680, 380)
        self.pendown()
        self.write(arg=f"lives: {self.lives}", align="center", font=FONT)
        self.penup()
        self.goto(-700, 380)

    def gameover(self):
        self.goto(0, 0)
        self.pendown()
        self.write(arg="Game Over", align="center", font=FONT)
