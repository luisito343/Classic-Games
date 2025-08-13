from Settings import WIDTH, HEIGHT, BG_COLOR, TITLE, FPS
from Player import Player
from Ball import Ball
from Score import Score
import time
import turtle as t


def setup_screen():
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor(BG_COLOR)
    screen.tracer(0)
    screen.title(TITLE)
    screen.listen()
    return screen

def main():
    screen = setup_screen()
    player_left = Player(x=-380, y=0,up_key="w", down_key="s" )
    player_right = Player(x=380, y=0,up_key="Up", down_key="Down" )
    ball = Ball()
    hud = Score()

    screen.listen()
    player_left.bind_keys(screen)
    player_right.bind_keys(screen)

    try:
        while True:
            t.update()
            time.sleep(1/FPS)
            ball.move()

            if ball.hits_top_or_bottom():
                ball.bounce_y()

            if ball.collides_with(player_left) or ball.collides_with(player_right):
                ball.increment_speed()
                ball.bounce_x()

                scorer = ball.out_of_bounds(WIDTH//2)
            
            scorer = ball.out_of_bounds(WIDTH // 2)
            if scorer:
                hud.point_to(scorer)  # "left" o "right"
                ball.reset(direction="left" if scorer == "right" else "right")
    except t.Terminator:
        pass


if __name__ == "__main__":
    main()
