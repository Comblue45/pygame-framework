from pygame import Vector2

from ecs_engine.ecs.ecs import ECS

from ecs_engine.helpers.world_position import world_position

from ecs_engine.components.chace_component import ChaceComponent
from ecs_engine.components.transform_dirty_flag import TransformDirtyFlag

def screen_position(entity: int, ecs: ECS) -> Vector2:
    if not ecs.entity_has_component(entity, TransformDirtyFlag):
        entity_chace = ecs.get_component_of_entity(entity, ChaceComponent)

        return entity_chace.screen_world_position
    else:
        valid_screen_position = world_position(entity, ecs)

        entity_chace = ecs.get_component_of_entity(entity, ChaceComponent)
        entity_chace.screen_world_position = valid_screen_position

        return valid_screen_position