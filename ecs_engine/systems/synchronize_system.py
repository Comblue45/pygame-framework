from ecs_engine.general.world import World

from ecs_engine.components.render_component import RenderComponent
from ecs_engine.components.sychnronise_flag import SynchroniseFlag

from ecs_engine.helpers.screen_position import screen_position

def synchronize_system(world: World) -> None:
    ecs = world.ecs

    entities_to_synchronize = world.ecs.get_entities_by_component(SynchroniseFlag)

    for entity in entities_to_synchronize:
        render_component = world.ecs.get_component_of_entity(entity, RenderComponent)

        render_component.screen_position = screen_position(entity, ecs)

        ecs.remove_component_of_entity(entity, SynchroniseFlag)