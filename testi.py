import pygame

from core_abstraction.game import Game
from core_abstraction.entity import Entity

class TestEntity(Entity):

    def __init__(self, color: str = "red", deebug_callbacks: bool = False, *args, **kwargs) -> None:
        surface = pygame.Surface((100,100))
        surface.fill(color)
        super().__init__(surface=surface, *args, **kwargs)

        self._deebug_callbacks = deebug_callbacks

        self.speed = 300

    def ready(self) -> None:
        if self._deebug_callbacks:
            print(f"Entity ({self.id}): [SETUP]")

    def update(self, dt: float) -> None:
        moved_flag = False
        if self.game.input.keys_pressed[pygame.K_w]:
            self.y -= self.speed * dt
            moved_flag = True
        if self.game.input.keys_pressed[pygame.K_s]:
            self.y += self.speed * dt
            moved_flag = True
        if self.game.input.keys_pressed[pygame.K_d]:
            self.x += self.speed * dt
            moved_flag = True
        if self.game.input.keys_pressed[pygame.K_a]:
            self.x -= self.speed * dt
            moved_flag = True

        if self._deebug_callbacks:
            if moved_flag or self.game.input.keys_pressed[pygame.K_p]:
                print(f"Entity ({self.id}): [POS:{self.position}]")
            else:
                print(f"Entity ({self.id}): [DT:{dt}]")

            if self.game.input.keys_down[pygame.K_l]: # type: ignore
                print(f"Entity ({self.id}): [LAYER:{self.layer}]")
                self.layer = 2

game = Game(size=(1000,800))
game.setup()

entity = TestEntity(deebug_callbacks=True)
game.add_entity(entity)

entity_2 = TestEntity(color="green", layer=1, position=(50,50))
game.add_entity(entity_2)

game.start()