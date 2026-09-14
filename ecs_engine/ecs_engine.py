import pygame

from collections.abc import Callable

from ecs_engine.ecs.ecs import ECS
from ecs_engine.ecs.component import Component

from ecs_engine.runtime.window import Window
from ecs_engine.runtime.input import Input
from ecs_engine.runtime.time import Time

from ecs_engine.general.world import World
from ecs_engine.general.layer import Layer
from ecs_engine.general.tags import Tags

from ecs_engine.systems.render_system import render_system
from ecs_engine.systems.synchronize_system import synchronize_system

from ecs_engine.components.render_component import RenderComponent
from ecs_engine.components.transform_component import TransformComponent
from ecs_engine.components.hirachie import Hirachie
from ecs_engine.components.chace_component import ChaceComponent
from ecs_engine.components.transform_dirty_flag import TransformDirtyFlag
from ecs_engine.components.sychnronise_flag import SynchroniseFlag

class ECSEngine:

    def __init__(
        self,
        size: tuple[int, int] = (800, 600),
        title: str = "ECS Engine",
        fps: int = 60,
        background_color: str = "black",
        systems: list[Callable] | None = None,
        component_types: list[type[Component]] | None = None
        ) -> None:
        self.ecs = ECS()

        self.window = Window(size=size, title=title)
        self.input = Input()
        self.time = Time(fps=fps)

        self.layer = Layer()
        self.tags = Tags()

        self.world = World(ecs=self.ecs,
                           window=self.window,
                           input=self.input,
                           time=self.time,
                           layer=self.layer,
                           tags=self.tags)

        self.systems = systems if systems is not None else []

        engine_systems = [render_system, synchronize_system]
        for engine_system in engine_systems:
            self.systems.append(engine_system)

        self.component_types = component_types if component_types is not None else []

        engine_components = [RenderComponent, 
                             TransformComponent, 
                             Hirachie, 
                             ChaceComponent, 
                             TransformDirtyFlag, 
                             SynchroniseFlag]
        for engine_component in engine_components:
            self.component_types.append(engine_component)

        self.running = False

        self.background_color = background_color

    def setup(self) -> None:

        for component in self.component_types:
            self.ecs.add_component_type(component)

        for system in self.systems:
            self.ecs.add_system(system)

    def start(self) -> None:
        self.running = True

        self._setup_entities()

        while self.running:
            self._handle_frame()

        self.window.quit()

    def _setup_entities(self) -> None:
        pass

    def _handle_frame(self) -> None:
        self.input.update()

        self.window.color_background(self.background_color)

        for system in self.systems:
            self.ecs.call_system(system, self.world)

        self.window.render()

        self.time.tick()

        self._handle_events()

    def _handle_events(self) -> None:
        for event in self.input.events:
            if event.type == pygame.QUIT:
                self.running = False

    def create_entity(
        self, 
        surface: pygame.Surface, 
        position: tuple[int, int] = (0, 0),
        layer: int = 1,
        tags: set[str] | None = None
        ) -> int:
        entity = self.ecs.create_entity()

        self.ecs.add_component_to_entity(entity, RenderComponent(surface, pygame.Vector2(position)))

        self.ecs.add_component_to_entity(entity, TransformComponent(pygame.Vector2(position)))

        self.ecs.add_component_to_entity(entity, ChaceComponent(pygame.Vector2(position), pygame.Vector2(position)))

        self.ecs.add_component_to_entity(entity, Hirachie(None, set()))

        self.ecs.add_component_to_entity(entity, TransformDirtyFlag())
        self.ecs.add_component_to_entity(entity, SynchroniseFlag())

        self.layer.register(entity, layer)

        tags = tags if tags is not None else set()
        for tag in tags:
            self.tags.register(entity, tag)

        return entity

    def add_component_to_entity(
        self,
        entity: int,
        component: Component,
    ) -> None:
        self.ecs.add_component_to_entity(entity, component)

    def remove_component_of_entity(
        self,
        entity: int,
        component_type: type[Component],
    ) -> None:
        self.ecs.remove_component_of_entity(entity, component_type)