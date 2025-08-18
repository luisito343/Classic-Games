import turtle as t
from settings import FONT

class Score:
    def __init__(self, level):
        self.level = level
        self.writer = t.Turtle(visible=False)
        self.writer.color("white")
        self.writer.penup()
        self.writer.goto(-300, 160)
        self._draw()

    def _draw(self):
        self.writer.clear()
        self.writer.write(f"Level: {self.level}", align="center", font=FONT)
    
    def increment(self, n=1):
        self.level += n
        self._draw()

    def set_level(self, level):
        self.level = level
        self._draw()