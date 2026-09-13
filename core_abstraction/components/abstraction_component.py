from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core_abstraction.entity import Entity

from ecs_engine.ecs.component import Component, dataclass

@dataclass(slots=True)
class AbstractionComponent(Component):
    abstraction_refrence: Entity