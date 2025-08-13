from turtle import Screen
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
screen.listen()

def start_game():
    # instancias
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    # bindings
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    food.refresh()
    # loop
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.score += 1
            scoreboard.update_scoreboard()

        
        if snake.xcor() > 295 or snake.xcor() < -295 or snake.ycor() > 295 or snake.ycor() < -295:
            game_is_on = False
            scoreboard.lose()

        
        if snake.hit_self():
            game_is_on = False
            scoreboard.lose()

    
    resp = screen.textinput("Game Over", "¿Do you want to play again? (y/n)")
    if resp and resp.lower().startswith("y"):
        screen.clear()
        screen.bgcolor("black")
        screen.tracer(0)
        screen.title("Snake Game")
        screen.listen()
        start_game()
    else:
        screen.bye()

start_game()
