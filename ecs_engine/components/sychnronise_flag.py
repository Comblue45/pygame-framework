from dataclasses import dataclass

from ecs_engine.ecs.component import Component

@dataclass(slots=True)
class SynchroniseFlag(Component):
    pass