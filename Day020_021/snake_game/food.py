from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle, instead of 20x20
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        self.refresh()

    def refresh(self):
        # place food at a random spot in the game area
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

