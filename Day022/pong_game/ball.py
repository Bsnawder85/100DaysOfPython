from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pos = 0
        self.y_pos = 0
        self.goto(x=self.x_pos, y=self.y_pos)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

