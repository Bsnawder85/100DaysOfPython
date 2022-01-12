from turtle import Screen
from game_divider import GameDivider
from paddle import Paddle
from ball import Ball
import time

UP = "Up"
DOWN = "Down"
W = "w"
S = "s"

# Build a version of the famous arcade game Pong.
# You need a game area to play on (screen) with a dashed line down the middle
# to separate the two halves of the game area.
# You need two paddles (turtles), one for each player.
# You need a ball object (turtle).
# You need a score object (turtle) for each player that form the number shapes.

screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)
dividing_line = GameDivider(800, 600)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, UP)
screen.onkey(right_paddle.go_down, DOWN)
screen.onkey(left_paddle.go_up, W)
screen.onkey(left_paddle.go_down, S)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

screen.exitonclick()
