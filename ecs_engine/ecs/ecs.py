from collections.abc import Callable
from typing import TypeVar, cast

from ecs_engine.ecs.component import Component

ComponentType = TypeVar("ComponentType", bound=Component)

class ECS:

    def __init__(self) -> None:
        self._current_id = 0
        self._components: dict[type[Component], dict[int, Component]] = {}
        self._systems = set()

    def create_entity(self) -> int:
        self._current_id += 1
        return self._current_id

    def get_all_entites(self) -> tuple[int, ...]:
        return tuple(range(0, self._current_id))

    def add_component_type(self, component_type: type[Component]) -> None:
        self._components[component_type] = {}

    def add_component_to_entity(
        self,
        entity: int,
        component: Component,
    ) -> None:
        self._components[type(component)][entity] = component

    def get_entities_by_components(
        self,
        component_types: list[type[Component]],
    ) -> set[int]:
        if len(component_types) == 0:
            raise ValueError("length of components must be bigger than 0")
        entities = [self._components[component].keys() for component in component_types]
        entities = set.intersection(*map(set, entities))
        return entities

    def get_entities_by_component(
        self,
        component_type: type[ComponentType],
    ) -> set[int]:
        return set(self._components[component_type].keys())

    def get_component_of_entity(
        self,
        entity: int,
        component_type: type[ComponentType],
    ) -> ComponentType:
        component = self._components[component_type][entity]
        return cast(ComponentType, component)

    def remove_component_type(self, component_type: type[Component]) -> None:
        del self._components[component_type]

    def remove_component_of_entity(
        self,
        entity: int,
        component_type: type[Component],
    ) -> None:
        del self._components[component_type][entity]

    def entity_has_component(
        self,
        entity: int,
        component_type: type[Component]
    ) -> bool:
        return entity in self._components[component_type].keys()

    def add_system(self, system: Callable) -> None:
        self._systems.add(system)

    def remove_system(self, system: Callable) -> None:
        self._systems.remove(system)

    def call_system(self, system: Callable, *args, **kwargs) -> None:
        if not system in self._systems:
            self._systems.add(system)
        system(*args, **kwargs)