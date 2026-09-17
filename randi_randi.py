import pygame

from random import shuffle

import math

from core_abstraction.game import Game
from core_abstraction.entity import Entity

def updati(dt: float, ) -> None:
    pass
class Spawner(Entity):

    def __init__(self, count: int = 2000, deebug_callbacks: bool = False, *args, **kwargs) -> None:
        super().__init__(surface=pygame.Surface((100,100)), *args, **kwargs)

        self.count = count

        self.colors = ["green", "red", "blue"]

        self._deebug_callbacks = deebug_callbacks

    def ready(self) -> None:
        x = 0
        y = 0

        for amount in range(0, self.count):
            surface = pygame.Surface((10,10))

            shuffle(self.colors)
            surface.fill(self.colors[0])

            entity = Entity(surface=surface, position=(x, y))
            entity.update = updati
            self.game.add_entity(entity)

            #x += 1
            #y += 1

class FPSCounter(Entity):

    def update(self, dt: float) -> None:
        print(self.game.time.clock.get_fps())

game = Game(size=(1000,800))
game.setup()

game.add_entity(Spawner())
game.add_entity(FPSCounter(surface=pygame.Surface((100,100))))

game.start()