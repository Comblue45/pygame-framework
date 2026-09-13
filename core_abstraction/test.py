# Engine (don't know if I could even consider this one) in an extremly early state

import pygame

from ecs_engine.ecs_engine import ECSEngine
from ecs_engine.general.world import World
from ecs_engine.components.render_component import RenderComponent
from ecs_engine.components.hirachie import Hirachie
from ecs_engine.ecs.component import Component, dataclass
from ecs_engine.helpers.move import move
from ecs_engine.helpers.connect import connect
from ecs_engine.helpers.disconnect import disconnect

@dataclass(slots=True)
class Moveable(Component):
    pass

def moveable_system(world: World):
    movable_entities = world.ecs.get_entities_by_components([Moveable, RenderComponent])

    if world.input.keys_down[pygame.K_g]:
        movable_entities = world.ecs.get_entities_by_components([Moveable, RenderComponent])

        for movable_entity in movable_entities:
            move(movable_entity, pygame.Vector2(50.0, 50.0), world.ecs)

    if world.input.keys_pressed[pygame.K_w]:
        for movable_entity in movable_entities:
            move(movable_entity, pygame.Vector2(0.0, -300.0) * world.time.dt, world.ecs)
    if world.input.keys_pressed[pygame.K_s]:
        for movable_entity in movable_entities:
            move(movable_entity, pygame.Vector2(0.0, 300.0) * world.time.dt, world.ecs)
    if world.input.keys_pressed[pygame.K_a]:
        for movable_entity in movable_entities:
            move(movable_entity, pygame.Vector2(-300.0, 0.0) * world.time.dt, world.ecs)
    if world.input.keys_pressed[pygame.K_d]:
        for movable_entity in movable_entities:
            move(movable_entity, pygame.Vector2(300.0, 0.0) * world.time.dt, world.ecs)

    # print(world.time.clock.get_fps())

def test_hirachie_system(world: World):
    hirachie_entities = world.ecs.get_entities_by_component(Hirachie)

    if world.input.keys_down[pygame.K_x]:
        for entity in hirachie_entities:
            hirachie_component = world.ecs.get_component_of_entity(entity, Hirachie)

            if hirachie_component.parent is not None:
                disconnect(hirachie_component.parent, entity, world.ecs)

def test_tag_system(world: World):
    tags = world.tags

    entities = tags.get_entities_with_tag("entity")
    test = tags.get_entities_with_tag("test")
    test_2 = tags.get_entities_with_tag("test2")
    bullshit = tags.get_entities_with_tags({"entity", "bullshit"})

    print(f"Entity: {entities}; test: {test}; test_2: {test_2}; bullshit: {bullshit}")

game = ECSEngine(systems=[moveable_system, test_hirachie_system, test_tag_system], component_types=[Moveable])

game.setup()

surface = pygame.Surface((100,100))
surface.fill("green")
test_entity = game.create_entity(surface=surface, position=(50, 50), tags={"entity", "test", "bullshit"})
game.add_component_to_entity(test_entity, Moveable())

surface = pygame.Surface((100,100))
surface.fill("red")
test_entity_2 = game.create_entity(surface=surface, position=(50, 50), layer=2, tags={"entity", "test2", "bullshit"})

connect(test_entity, test_entity_2, game.ecs)

game.start()