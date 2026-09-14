import pygame

from core_abstraction.game import Game
from core_abstraction.entity import Entity

class TestEntity(Entity):

    def __init__(self, color: str = "red", deebug_callbacks: bool = False, *args, **kwargs) -> None:
        surface = pygame.Surface((100,100))
        surface.fill(color)
        super().__init__(surface=surface, *args, **kwargs)

        self._deebug_callbacks = deebug_callbacks

    def ready(self) -> None:
        if self._deebug_callbacks:
            print(f"Entity ({self.id}): [SETUP]")

    def update(self, dt: float) -> None:
        if self._deebug_callbacks:
            print(f"Entity ({self.id}): [DT:{dt}]")

            if self.game.input.keys_down[pygame.K_l]: # type: ignore
                print(f"Entity ({self.id}): [LAYER:{self.layer}]")
                self.layer = 2

game = Game()
game.setup()

entity = TestEntity(deebug_callbacks=True)
game.add_entity(entity)

entity_2 = TestEntity(color="green", layer=1, position=(50,50))
game.add_entity(entity_2)

game.start()