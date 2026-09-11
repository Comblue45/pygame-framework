from dataclasses import dataclass

from ecs_engine.ecs.ecs import ECS

from ecs_engine.runtime.window import Window
from ecs_engine.runtime.input import Input
from ecs_engine.runtime.time import Time

@dataclass(slots=True)
class World:
    ecs: ECS

    window: Window
    input: Input
    time: Time