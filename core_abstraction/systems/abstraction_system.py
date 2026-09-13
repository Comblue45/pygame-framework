from ecs_engine.general.world import World

from core_abstraction.components.abstraction_component import AbstractionComponent

def abstraction_system(world: World) -> None:
    abtraction_entities = world.ecs.get_entities_by_component(AbstractionComponent)

    for entity in abtraction_entities:
        abstraction_component = world.ecs.get_component_of_entity(entity, AbstractionComponent)

        refrence = abstraction_component.abstraction_refrence

        refrence.update(world.time.dt)