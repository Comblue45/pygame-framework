# Engine (don't know if I could even consider this one) in an extremly early state

import pygame

from ecs_engine.ecs_engine import ECSEngine
from ecs_engine.general.world import World
from ecs_engine.components.render_component import RenderComponent
from ecs_engine.ecs.component import Component, dataclass

@dataclass(slots=True)
class Moveable(Component):
    pass

def moveable_system(world: World):
    movable_entities = world.ecs.get_entities_by_components([Moveable, RenderComponent])

    if world.input.keys_pressed[pygame.K_g]:
        movable_entities = world.ecs.get_entities_by_components([Moveable, RenderComponent])

        for movable_entity in movable_entities:
            rendering_component = world.ecs.get_component_of_entity(movable_entity, RenderComponent)
            rendering_component.screen_position += (50.0, 50.0)
            world.ecs.remove_component_of_entity(movable_entity, Moveable)

game = ECSEngine(systems=[moveable_system], component_types=[Moveable])

game.setup()

test_entity = game.create_entity()
surface = pygame.Surface((100,100))
surface.fill("green")
game.add_component_to_entity(test_entity, RenderComponent(surface, pygame.Vector2(50,50)))
game.add_component_to_entity(test_entity, Moveable())

game.start()