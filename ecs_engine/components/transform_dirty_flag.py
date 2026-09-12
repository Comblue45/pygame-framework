from dataclasses import dataclass

from ecs_engine.ecs.component import Component

@dataclass(slots=True)
class TransformDirtyFlag(Component):
    pass