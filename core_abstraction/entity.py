from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from core_abstraction.components.abstraction_component import AbstractionComponent

if TYPE_CHECKING:
    from core_abstraction.game import Game

class Entity:

    def __init__(self, surface: pygame.Surface) -> None:
        self._surface = surface

        self.game = None

    def setup(self, game: Game) -> None:
        self.game = game

        self._entity = self.game.create_entity(surface=self._surface)

        self.game.ecs.add_component_to_entity(self._entity, AbstractionComponent(self))

    def ready(self) -> None:
        pass

    def update(self, dt: float) -> None:
        pass