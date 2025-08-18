import turtle as t
import time
from settings import WIDTH, HEIGHT, BG_COLOR, TITLE,GRID
from player import Player
from levels import Levels
from Score import Score

def setup_screen():
    screen = t.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor(BG_COLOR)
    screen.tracer(0)
    screen.colormode(255)
    screen.title(TITLE)
    screen.listen()
    return screen

def main():
    screen = setup_screen()
    player = Player(0, -180, "w", "s", "d", "a")
    player.bind_keys(screen)

    levels = Levels(base_cars=2, base_speed=4, max_cars=40)
    score = Score(levels.level)

    interval_ms = 60 

    def tick():
        state = levels.update(player)

        if state == "collision":
            print("💥 Colisión")
            return

        elif state == "level_up":
            print(f"✅ Nivel {levels.level - 1} superado → Nivel {levels.level}")
            score.increment()
            levels.level_up(player)

        screen.update()
        screen.ontimer(tick, interval_ms)

    tick()
    screen.mainloop()

if __name__ == "__main__":
    main()