import turtle
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        turtle.Screen().tracer(False)
        turtle.Screen().register_shape("player.gif")
        self.hideturtle()
        self.shape("player.gif")
        self.penup()
        self.sety(-350)
        self.showturtle()

    def moveleft(self):
        if self.xcor() > -580:
            self.bk(30)

    def moveright(self):
        if self.xcor() < 580:
            self.fd(30)
