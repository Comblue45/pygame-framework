from pygame import Vector2

from ecs_engine.ecs.ecs import ECS

from ecs_engine.components.transform_component import TransformComponent
from ecs_engine.components.hirachie import Hirachie
from ecs_engine.components.transform_dirty_flag import TransformDirtyFlag
from ecs_engine.components.sychnronise_flag import SynchroniseFlag

def move(entity: int, move_by: Vector2, ecs: ECS) -> None:
    transform_component = ecs.get_component_of_entity(entity, TransformComponent)
    transform_component.local_position += move_by

    hirachie_component = ecs.get_component_of_entity(entity, Hirachie)
    for child in hirachie_component.children:
        ecs.add_component_to_entity(child, TransformDirtyFlag())
        ecs.add_component_to_entity(child, SynchroniseFlag())

    ecs.add_component_to_entity(entity, TransformDirtyFlag())
    ecs.add_component_to_entity(entity, SynchroniseFlag())