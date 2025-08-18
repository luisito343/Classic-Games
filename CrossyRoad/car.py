import turtle as t
import random
from settings import CAR_SPEED_INIT, WIDTH

class Car:
    def __init__(self, x: int, y: int):
        self.sprite = t.Turtle()
        self.sprite.shape("square")
        self.sprite.color("white")
        self.sprite.penup()
        r, g, b = (random.randint(0, 255) for _ in range(3))
        self.sprite.color(r, g, b)
        self.x = x
        self.y = y
        self.sprite.goto(x, y)
        self.sprite.setheading(180)
        self.step = CAR_SPEED_INIT  # tamaño de paso, ej. 20

    def move(self):
        x = self.sprite.xcor() - self.step
        y = self.sprite.ycor()
        self.sprite.goto(x, y)

    def colision_with(self, player):
        if self.sprite.distance(player.sprite) < 20:
            return True
        return False
    
    def out_of_screen(self):
        half_width = WIDTH // 2
        return self.sprite.xcor() < -half_width - 20

    def respawn_car(self):
        x = WIDTH // 2 + 20  
        posibles_y = list(range(-160, 160, 20))
        y = random.choice(posibles_y)
        self.sprite.goto(x, y)
    
    def __str__(self):
        return f"coords: x = {self.x}, y = {self.y}"
