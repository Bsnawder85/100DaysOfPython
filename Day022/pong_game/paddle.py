from turtle import Turtle


# Paddles should be (WxH) 20x100 pixels,
# starting with an x-position of 350 and y-position of 0.

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=350, y=0)


