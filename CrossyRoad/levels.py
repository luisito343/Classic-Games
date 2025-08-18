import random
from car import Car

STEP = 20

class Levels:
    def __init__(self, base_cars=2, base_speed=4, max_cars=30):
        self.level = 1
        self.max_cars = max_cars
        self.base_cars = base_cars
        self.base_speed = base_speed
        self.cars = []
        self._build_initial_fleet()

    def _build_initial_fleet(self):
        need = self._cars_for_level(self.level)
        self._ensure_cars(need)

    def _cars_for_level(self, lvl:int) -> int:
        return min(self.base_cars + (lvl - 1), self.max_cars)

    def _ensure_cars(self, target_count:int):
        """Asegura que haya exactamente target_count autos en la flota."""
        current = len(self.cars)
        if current < target_count:
            # Agregar autos nuevos, con Y aleatoria, entrando por la derecha
            posibles_y = list(range(-160,160, 20))
            posibles_x = list(range(-360, 360, 20))
            for _ in range(target_count - current):
                y = random.choice(posibles_y)
                x = random.choice(posibles_x)
                car = Car(x, y)
                
                self.cars.append(car)
        elif current > target_count:
            self.cars = self.cars[:target_count]

    def level_up(self, player):
        self.level += 1
        player.reset_position()  
        
        target = self._cars_for_level(self.level)
        self._ensure_cars(target)

    def update(self, player):
        for car in self.cars:
            car.move()
            if car.out_of_screen():
                car.respawn_car()

            if car.colision_with(player):
                return "collision"

        if player.is_on_top():
            return "level_up"

        return None
