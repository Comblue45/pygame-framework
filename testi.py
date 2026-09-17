import pygame

from core_abstraction.game import Game
from core_abstraction.entity import Entity

class TestEntity(Entity):

    def __init__(self, color: str = "red", deebug_callbacks: bool = False, *args, **kwargs) -> None:
        surface = pygame.Surface((100,100))
        surface.fill(color)
        super().__init__(surface=surface, tags={"something"}, *args, **kwargs)

        self._deebug_callbacks: bool = deebug_callbacks

        self.speed: int = 300

        self.screen_center: pygame.Vector2 = pygame.Vector2(0, 0)

    def ready(self) -> None:
        if self._deebug_callbacks:
            print(f"Entity ({self.id}): [SETUP]")
        self.screen_center = pygame.Vector2(self.game.window.size) / 2

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

        if self.game.input.keys_down[pygame.K_g]:
            self.position = self.screen_center
            moved_flag = True

        if self._deebug_callbacks:
            if self.game.input.keys_down[pygame.K_1]:
                self.add_tag("anotherthing")
            if self.game.input.keys_down[pygame.K_2]:
                self.add_tag("nothing")
            if self.game.input.keys_down[pygame.K_3]:
                self.tags = {"something",}
        
        if self._deebug_callbacks:
            if moved_flag or self.game.input.keys_pressed[pygame.K_p]:
                print(f"Entity ({self.id}): [POS:{self.position}]")
            elif self.game.input.keys_pressed[pygame.K_t]:
                something = self.game.tags.get_entities_with_tag("something")
                anotherthing = self.game.tags.get_entities_with_tag("anotherthing")
                nothing = self.game.tags.get_entities_with_tag("nothing")
                print(f"Entity (self.id): [SOMETHING:{something}] [ANOTHERTHING:{anotherthing}] [NOTHING:{nothing}]")
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