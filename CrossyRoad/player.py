import turtle as t
from settings import HEIGHT, WIDTH, PLAYER_SPEED

class Player:
    def __init__(self, x: int, y: int, up_key: str, down_key: str, rig_key: str, lef_key: str):
        self.up_key = up_key
        self.down_key = down_key
        self.rig_key = rig_key
        self.lef_key = lef_key
        self.sprite = t.Turtle()
        self.sprite.shape("turtle")
        self.sprite.color("white")
        self.sprite.penup()
        self.sprite.goto(x,y)
        self.sprite.setheading(90)

    def move_up(self):
        new_y = self.sprite.ycor() + PLAYER_SPEED
        self.sprite.sety(self._clamp(new_y))
        

    def move_down(self):
        new_y = self.sprite.ycor() - PLAYER_SPEED
        self.sprite.sety(self._clamp(new_y))

    def move_right(self):
        new_x = self.sprite.xcor() + PLAYER_SPEED
        self.sprite.setx(self._clamp_w(new_x))

    def move_left(self):
        new_x = self.sprite.xcor() - PLAYER_SPEED
        self.sprite.setx(self._clamp_w(new_x))

    def is_on_top(self):
        if self.sprite.ycor() >= HEIGHT // 2 - 20:
            return True
        return False
    
    def reset_position(self):
        self.sprite.goto(0,-180)

    def _clamp(self, y: float) -> float:
        half = HEIGHT // 2 - 20 
        return max(-half, min(half, y))
    
    def _clamp_w(self, x: float) -> float:
        half = WIDTH // 2 - 20 
        return max(-half, min(half, x))

    def bind_keys(self, screen: t.Screen):
        screen.onkeypress(self.move_up, self.up_key)
        screen.onkeypress(self.move_down, self.down_key)
        screen.onkeypress(self.move_right, self.rig_key)
        screen.onkeypress(self.move_left, self.lef_key)