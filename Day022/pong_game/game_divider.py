from turtle import Turtle
import math


class GameDivider(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(8)
        self.penup()
        self.goto(0, math.floor(screen_height / 2))
        self.setheading(270)
        self.pendown()
        self.forward(screen_height)

