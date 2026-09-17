from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from core_abstraction.components.abstraction_component import AbstractionComponent

from ecs_engine.helpers.set_position import set_position
from ecs_engine.helpers.world_position import world_position
from ecs_engine.helpers.screen_position import screen_position

from ecs_engine.helpers.add_tag import add_tag
from ecs_engine.helpers.remove_tag import remove_tag
from ecs_engine.helpers.clear_tags import clear_tags

if TYPE_CHECKING:
    from core_abstraction.game import Game

class Entity:

    def __init__(
        self, 
        surface: pygame.Surface, 
        layer: int = 1, 
        tags: set[str] | None = None,
        position: tuple[float, float] = (0.0, 0.0),
        copy_position_on_assignment: bool = True
        ) -> None:
        self._surface = surface

        # self.game = None

        self.id: int = -1

        self._layer: int = layer

        self._tags: set[str] = tags if tags is not None else set()

        self._position: pygame.Vector2 = pygame.Vector2(position)

        self.copy_position_on_assignment: bool = copy_position_on_assignment

    def setup(self, game: Game) -> None:
        self.game = game

        self._entity = self.game.create_entity(surface=self._surface, position=(self._position.x, self._position.y), layer=self._layer)

        self.id = self._entity

        self.game.ecs.add_component_to_entity(self._entity, AbstractionComponent(self))

        for tag in self._tags:
            self.add_tag(tag)

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
        return self._position.copy()

    @position.setter
    def position(self, new_position: pygame.Vector2) -> None:
        if self.copy_position_on_assignment:
            new_position = new_position.copy()

        set_position(self._entity, (new_position.x, new_position.y), self.game.ecs)
        self._position = new_position

    @property
    def tags(self) -> set[str]:
        return self._tags

    @tags.setter
    def tags(self, new_tags: set[str]):
        self.tags.clear()
        clear_tags(self._entity, self.game.tags)
        for tag in new_tags:
            self.add_tag(tag)

    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)
        add_tag(self._entity, tag, self.game.tags)

    def remove_tag(self, tag: str) -> None:
        self.tags.remove(tag)
        remove_tag(self._entity, tag, self.game.tags)

    def world_position(self) -> pygame.Vector2:
        return world_position(self._entity, self.game.ecs)

    def screen_position(self) -> pygame.Vector2:
        return screen_position(self._entity, self.game.ecs)