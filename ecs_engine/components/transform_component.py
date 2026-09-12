import pygame

from dataclasses import dataclass

from ecs_engine.ecs.component import Component

@dataclass(slots=True)
class TransformComponent(Component):
    local_position: pygame.Vector2