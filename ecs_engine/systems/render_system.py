from ecs_engine.general.world import World

from ecs_engine.components.render_component import RenderComponent

def render_system(world: World) -> None:
    ecs = world.ecs

    entities_to_render = world.layer.get_rendering_order_iterable()

    for entity in entities_to_render:
        render_component = ecs.get_component_of_entity(entity, RenderComponent)
        world.window.blit(render_component.surface, render_component.screen_position)