from turtle import Turtle

def create_snake():
    snake = []
    for index in range(3):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(-20 * index, 0)
        snake.append(segment)
    return snake

def move_snake(snake):
    for index in range(len(snake) - 1, 0, -1):
        new_x = snake[index - 1].xcor()
        new_y = snake[index - 1].ycor()
        snake[index].goto(new_x, new_y)
    snake[0].forward(20)

class Snake:
    
    def __init__(self):
        self.segments = create_snake()
        self.head = self.segments[0]

    def move(self):
        move_snake(self.segments)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def position(self):
        return self.head.position()
    
    def xcor(self):
        return self.head.xcor()
    
    def ycor(self):
        return self.head.ycor()
    
    def extend(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
        self.move()
    
    def hit_self(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False