import pygame

from dataclasses import dataclass

from ecs_engine.ecs.component import Component

@dataclass(slots=True)
class ChaceComponent(Component):
    chace_world_position: pygame.Vector2
    screen_world_position: pygame.Vector2