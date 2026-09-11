import pygame

from dataclasses import dataclass

from ecs_engine.ecs.component import Component

@dataclass(slots=True)
class RenderComponent(Component):
    surface: pygame.Surface
    screen_position: pygame.Vector2