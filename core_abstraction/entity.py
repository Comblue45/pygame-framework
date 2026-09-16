from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from core_abstraction.components.abstraction_component import AbstractionComponent

from ecs_engine.helpers.set_position import set_position
from ecs_engine.helpers.world_position import world_position
from ecs_engine.helpers.screen_position import screen_position

if TYPE_CHECKING:
    from core_abstraction.game import Game

class Entity:

    def __init__(self, surface: pygame.Surface, layer: int = 1, position: tuple[float, float] = (0.0, 0.0)) -> None:
        self._surface = surface

        # self.game = None

        self.id = None

        self._layer = layer

        self._position: pygame.Vector2 = pygame.Vector2(position)

    def setup(self, game: Game) -> None:
        self.game = game

        self._entity = self.game.create_entity(surface=self._surface, position=(self._position.x, self._position.y), layer=self._layer)

        self.id = self._entity

        self.game.ecs.add_component_to_entity(self._entity, AbstractionComponent(self))

    def ready(self) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    @property
    def layer(self) -> int:
        return self._layer

    @layer.setter
    def layer(self, new_layer: int) -> None:
        if not self.game:
            return # Raise error or warning here

        if new_layer == self._layer:
            return

        self.game.layer.check_out(self._entity, self._layer)

        self._layer = new_layer
        self.game.layer.register(self._entity, new_layer)

    @property
    def x(self) -> float:
        return self._position.x

    @x.setter
    def x(self, new_x: float) -> None:
        set_position(self._entity, (new_x, self._position.y), self.game.ecs)
        self._position.x = new_x

    @property
    def y(self) -> float:
        return self._position.y

    @y.setter
    def y(self, new_y: float) -> None:
        set_position(self._entity, (self._position.x, new_y), self.game.ecs)
        self._position.y = new_y

    @property
    def position(self) -> pygame.Vector2:
        return self._position

    def world_position(self) -> pygame.Vector2:
        return world_position(self._entity, self.game.ecs)

    def screen_position(self) -> pygame.Vector2:
        return screen_position(self._entity, self.game.ecs)