from turtle import Screen
from game_divider import GameDivider


class GameArea(Screen):
    def __init__(self, w, h, title, color):
        super().__init__()
        self.setup(width=w, height=h)
        self.title(title)
        self.bgcolor(color)
        self.tracer(0)
        self.dividing_line = GameDivider(800, 600)




