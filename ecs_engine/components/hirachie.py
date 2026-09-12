from ecs_engine.ecs.component import Component, dataclass

@dataclass(slots=True)
class Hirachie(Component):
    parent: int | None
    children: set[int]