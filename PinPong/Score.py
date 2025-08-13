import turtle as t
from Settings import FONT

class Score:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.writer = t.Turtle(visible=False)
        self.writer.color("white")
        self.writer.penup()
        self.writer.goto(0, 150)
        self._draw()

    def _draw(self):
        self.writer.clear()
        self.writer.write(f"{self.left}   |   {self.right}", align="center", font=FONT)

    def point_to(self, who: str):
        if who == "left":
            self.left += 1
        else:
            self.right += 1
        self._draw()