from core_abstraction.systems.abstraction_system import abstraction_system

from core_abstraction.components.abstraction_component import AbstractionComponent

from ecs_engine.ecs_engine import ECSEngine

from core_abstraction.entity import Entity

class Game(ECSEngine):

    def __init__(self, size: tuple[int, int] = (800, 600), title: str = "ECS Engine", fps: int = 60, background_color: str = "black", ) -> None:
        super().__init__(size, title, fps, background_color, [abstraction_system], [AbstractionComponent])

    def add_entity(self, entity: Entity) -> None:
        entity.setup(self)

        if self.running:
            entity.ready()

    def _setup_entities(self) -> None:
        super()._setup_entities()
        abtraction_entities = self.ecs.get_entities_by_component(AbstractionComponent)

        for entity in abtraction_entities:
            abstraction_component = self.ecs.get_component_of_entity(entity, AbstractionComponent)

            refrence = abstraction_component.abstraction_refrence

            refrence.ready()