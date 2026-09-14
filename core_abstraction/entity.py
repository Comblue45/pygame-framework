from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from core_abstraction.components.abstraction_component import AbstractionComponent

if TYPE_CHECKING:
    from core_abstraction.game import Game

class Entity:

    def __init__(self, surface: pygame.Surface, layer: int = 1, position: tuple[int, int] = (0, 0)) -> None:
        self._surface = surface

        self.game = None

        self.id = None

        self._layer = layer

        self._position = position

    def setup(self, game: Game) -> None:
        self.game = game

        self._entity = self.game.create_entity(surface=self._surface, position=self._position, layer=self._layer)

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