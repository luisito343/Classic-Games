from Settings import HEIGHT, PADDLE_SPEED, PADDLE_SIZE
import turtle as t

class Player:
    def __init__(self, x: int, y: int, up_key: str, down_key: str):
        self.up_key = up_key
        self.down_key = down_key
        self.sprite = t.Turtle("square")
        self.sprite.color("white")
        self.sprite.penup()
        self.sprite.goto(x,y)
        self.sprite.shapesize(stretch_wid= PADDLE_SIZE[0], stretch_len=PADDLE_SIZE[1])

    def move_up(self):
        new_y = self.sprite.ycor() + PADDLE_SPEED
        self.sprite.sety(self._clamp(new_y))

    def move_down(self):
        new_y = self.sprite.ycor() - PADDLE_SPEED
        self.sprite.sety(self._clamp(new_y))

    def _clamp(self, y: float) -> float:
        half = HEIGHT // 2 - 20 
        return max(-half, min(half, y))

    def bind_keys(self, screen: t.Screen):
        screen.onkeypress(self.move_up, self.up_key)
        screen.onkeypress(self.move_down, self.down_key)