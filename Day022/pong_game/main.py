from turtle import Screen
from game_divider import GameDivider
from paddle import Paddle

UP = "up"
DOWN = "down"

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

player1 = Paddle()

screen.update()  # show screen and game objects after placing them.

screen.listen()


screen.exitonclick()
