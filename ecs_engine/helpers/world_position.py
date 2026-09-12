from pygame import Vector2

from ecs_engine.ecs.ecs import ECS

from ecs_engine.components.transform_component import TransformComponent
from ecs_engine.components.hirachie import Hirachie
from ecs_engine.components.chace_component import ChaceComponent
from ecs_engine.components.transform_dirty_flag import TransformDirtyFlag

def world_position(entity: int, ecs: ECS) -> Vector2:
    def chased_position() -> Vector2:
        entity_chace = ecs.get_component_of_entity(entity, ChaceComponent)

        return entity_chace.chace_world_position

    if not ecs.entity_has_component(entity, TransformDirtyFlag):
        return chased_position()
    else:
        parent = ecs.get_component_of_entity(entity, Hirachie).parent

        if parent is None:
            valid_world_position = ecs.get_component_of_entity(entity, TransformComponent).local_position
        else:
            local_position = ecs.get_component_of_entity(entity, TransformComponent).local_position
            valid_world_position = local_position + world_position(parent, ecs)

        entity_chace = ecs.get_component_of_entity(entity, ChaceComponent)
        entity_chace.chace_world_position = valid_world_position

        ecs.remove_component_of_entity(entity, TransformDirtyFlag)

        return valid_world_position