import pygame

from collections.abc import Callable

from ecs_engine.ecs.ecs import ECS
from ecs_engine.ecs.component import Component

from ecs_engine.runtime.window import Window
from ecs_engine.runtime.input import Input
from ecs_engine.runtime.time import Time

from ecs_engine.general.world import World

from ecs_engine.systems.render_system import render_system

from ecs_engine.components.render_component import RenderComponent

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

        self.world = World(ecs=self.ecs,
                           window=self.window,
                           input=self.input,
                           time=self.time)

        self.systems = systems if systems is not None else []
        self.systems.append(render_system)

        self.component_types = component_types if component_types is not None else []
        self.component_types.append(RenderComponent)

        self.running = False

        self.background_color = background_color

    def setup(self) -> None:
        self.ecs.add_system(render_system)

        for component in self.component_types:
            self.ecs.add_component_type(component)

        for system in self.systems:
            self.ecs.add_system(system)

    def start(self) -> None:
        self.running = True

        while self.running:
            self._handle_frame()

        self.window.quit()

    def _handle_frame(self) -> None:
        self.input.update()

        self.window.color_background(self.background_color)

        for system in self.systems:
            self.ecs.call_system(system, self.world)

        self.ecs.call_system(render_system, self.world)

        self.window.render()

        self.time.tick()

        self._handle_events()

    def _handle_events(self) -> None:
        for event in self.input.events:
            if event.type == pygame.QUIT:
                self.running = False

    def create_entity(self) -> int:
        return self.ecs.create_entity()

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