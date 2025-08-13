import random
import turtle as t
from Settings import  HEIGHT, BALL_SPEED_INIT, BALL_SPEED_MAX, BALL_SPEED_STEP

class Ball:
    def __init__(self):
        self.sprite = t.Turtle("circle")
        self.sprite.color("white")
        self.sprite.penup()
        self.speed_mag = BALL_SPEED_INIT
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-0.6, 0.6])

    def move(self):
        x = self.sprite.xcor() + self.dx * self.speed_mag
        y = self.sprite.ycor() + self.dy * self.speed_mag
        self.sprite.goto(x, y)

    def hits_top_or_bottom(self) -> bool:
        return abs(self.sprite.ycor()) > (HEIGHT // 2 - 10)

    def bounce_y(self):
        self.dy *= -1

    def collides_with(self, player) -> bool:
        """Caja simple: distancia en X corta y en Y dentro del alto de la paleta."""
        bx, by = self.sprite.xcor(), self.sprite.ycor()
        px, py = player.sprite.xcor(), player.sprite.ycor()
        # Ajustes finos para el ancho/alto reales
        close_x = abs(bx - px) < 20
        within_y = abs(by - py) < 60
        if close_x and within_y:
            return True
        return False

    def bounce_x(self):
        self.dx *= -1

    def out_of_bounds(self, half_width: int) -> str | None:
        x = self.sprite.xcor()
        if x > half_width:
            return "left"
        if x < -half_width:
            return "right"
        return None
    
    def increment_speed(self):
        if self.speed_mag < BALL_SPEED_MAX:
            self.speed_mag += BALL_SPEED_STEP

    def reset(self, direction: str):
        self.sprite.goto(0, 0)
        self.speed_mag = BALL_SPEED_INIT
        self.dx = 1 if direction == "right" else -1
        self.dy = random.choice([-0.6, 0.6])