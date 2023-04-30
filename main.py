import time
from turtle import *
from bullet import *
from player import *
from enemy import *
from scoreboard import *

# screen initialisation
screen = Screen()
screen.bgpic("background.png")
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
screen.title("Marine invaders")

# object initialisation from classes
player = Player()
bullet = Bullet()
enemy = Enemy()
scoreboard = Scoreboard()
enemy.generate_enemies()

# Event handling
screen.listen()
screen.onkeypress(player.moveleft, "Left")
screen.onkeypress(player.moveright, "Right")
screen.onkeypress(lambda: bullet.generate_bullets(player.xcor()), "space")
screen.onkeypress(screen.bye, "Escape")

# Game loop
game_on = True
while game_on:
    time.sleep(0.03)
    screen.update()
    bullet.launch()
    enemy.launch_bombs(playerpos=player)
    enemy.move_enemies()

# Progress to next level by detecting if enemies list is empty
    if len(enemy.enemies) == 0:
        scoreboard.increase_score()
        # enemy.increase_step()
        scoreboard.print_score()
        enemy.generate_enemies()

# detect if player was hit with bombs
    for bomb in enemy.bombs:
        if bomb.distance(player) < 30:
            bomb.hideturtle()
            bomb.goto(1000, 1000)
            enemy.bombs.remove(bomb)
            scoreboard.reduce_lives()
            scoreboard.print_score()

# Detect if lives reduced to zero to end game & reset values
    if scoreboard.lives <= 0:
        scoreboard.gameover()
        game_on = False
        scoreboard.lives = 3
        scoreboard.score = 1
        enemy.enemies.clear()
        enemy.bombs.clear()
        bullet.bullets.clear()

screen.exitonclick()



