from typing import Iterable

class Layer:

    def __init__(self, layers: int = 1) -> None:
        self.layers: dict[int, set[int]] = {}

        for layer in range(0, layers):
            self.add_layer(layer)

    def add_layer(self, layer: int) -> None:
        self.layers[layer] = set()

    def register(self, entity: int, entity_layer: int) -> None:
        if not entity_layer in self.layers.keys():
            self.add_layer(entity_layer)

        self.layers[entity_layer].add(entity)

    def check_out(self, entity: int, entity_layer: int) -> None:
        if not entity in self.layers[entity_layer]:
            for layer in self.layers.keys():
                if entity in self.layers[layer]:
                    entity_layer = layer
                    break

        self.layers[entity_layer].remove(entity)

    def get_rendering_order_iterable(self) -> Iterable:
        rendering_order: list[int] = []

        for layer in sorted(self.layers.keys(), reverse=True):
            rendering_order = rendering_order + list(self.layers[layer])

        return rendering_order