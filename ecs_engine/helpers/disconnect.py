from ecs_engine.ecs.ecs import ECS

from ecs_engine.components.hirachie import Hirachie
from ecs_engine.components.transform_dirty_flag import TransformDirtyFlag
from ecs_engine.components.sychnronise_flag import SynchroniseFlag

def disconnect(parent: int, child: int, ecs: ECS) -> None:
    parent_hirachie = ecs.get_component_of_entity(parent, Hirachie)
    parent_hirachie.children.remove(child)

    child_hirachie = ecs.get_component_of_entity(child, Hirachie)
    child_hirachie.parent = None

    ecs.add_component_to_entity(child, TransformDirtyFlag())
    ecs.add_component_to_entity(child, SynchroniseFlag())