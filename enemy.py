import random
import turtle
from turtle import Turtle


class Enemy:
    enemies = []

    def __init__(self):
        self.step = 5
        turtle.Screen().register_shape("enemy.gif")
        turtle.Screen().register_shape("bombs.gif")
        turtle.Screen().register_shape("enemy2.gif")
        self.shape = "enemy.gif"
        self.bombs = []

    def increase_step(self):
        self.step += 1

    def generate_enemies(self, enemies=enemies):
        self.x = 700
        self.y = 360
        turtle.Screen().tracer(False)
        for i in range(0, 20):
            enemy = Turtle(visible=False)
            enemy.shape(self.shape)
            enemy.penup()
            enemy.goto(self.x, self.y)
            self.x -= 80
            if self.x == 300:
                self.x = 700
                self.y -= 40
            enemy.showturtle()
            enemies.append(enemy)

    def move_enemies(self, enemies=enemies):
        for enemy in enemies:
            if enemy.xcor() <= -700:
                self.shape = "enemy2.gif"
                self.step = -5
                enemies.reverse()
            elif enemy.xcor() >= 700:
                self.shape = "enemy.gif"
                self.step = 5
                enemies.reverse()
        for enemy in enemies:
            enemy.shape(self.shape)
            enemy.backward(self.step)
            chance = random.randint(1, 300)
            if chance == 1:
                self.generate_bombs(enemyx=enemy.xcor(), enemyy=enemy.ycor())

    def generate_bombs(self, enemyx, enemyy):
        bomb = Turtle(visible=False)
        turtle.Screen().tracer(False)
        bomb.penup()
        bomb.setx(enemyx)
        bomb.sety(enemyy)
        bomb.showturtle()
        bomb.shape("bombs.gif")
        self.bombs.append(bomb)

    def launch_bombs(self, playerpos, enemies=enemies):
        if len(self.bombs) != 0:
            for bomb in self.bombs:
                bomb.goto(x=bomb.xcor(), y=bomb.ycor() - 20)
                if bomb.ycor() < -370:
                    bomb.goto(x=1000, y=1000)
                    self.bombs.remove(bomb)



