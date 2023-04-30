import turtle
from turtle import Turtle
from enemy import Enemy


class Bullet:
    def __init__(self):
        self.bullets = []
        turtle.Screen().register_shape("missile.gif")

    def generate_bullets(self, player_pos):
        if len(self.bullets) <= 3:
            new_bullet = Turtle(visible=False)
            turtle.Screen().tracer(False)
            new_bullet.penup()
            new_bullet.setx(player_pos)
            new_bullet.sety(-330)
            new_bullet.showturtle()
            new_bullet.shape("missile.gif")
            self.bullets.append(new_bullet)

    def launch(self):
        if len(self.bullets) != 0:
            for bullet in self.bullets:
                bullet.goto(x=bullet.xcor(), y=bullet.ycor() + 20)
                for enemy in Enemy.enemies:
                    if bullet.distance(enemy) < 30:
                        enemy.goto(1000, 1000)
                        bullet.goto(1000,1000)
                        Enemy.enemies.remove(enemy)
                if bullet.ycor() > 460:
                    self.bullets.remove(bullet)
