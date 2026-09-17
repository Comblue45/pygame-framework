class Tags:

    def __init__(self) -> None:
        self.tags: dict[str, set[int]] = {}

    def add_tag(self, tag: str) -> None:
        self.tags[tag] = set()

    def register(self, entity: int, entity_tag: str) -> None:
        if not entity_tag in self.tags.keys():
            self.add_tag(entity_tag)

        self.tags[entity_tag].add(entity)

    def check_out(self, entity: int, entity_tag: str) -> None:
        self.tags[entity_tag].remove(entity)

    def get_entities_with_tag(self, tag: str) -> set[int]:
        if not tag in self.tags.keys():
            self.add_tag(tag)

        return self.tags[tag].copy()

    def get_entities_with_tags(self, tags: set[str]) -> set[int]:
        if not all(tag in self.tags.keys() for tag in tags):
            (self.add_tag(tag) for tag in tags if not tag in self.tags.keys())

        entities = set()

        process_list: list[set[int]] = []
        for tag in tags:
            process_list.append(self.tags[tag])

        entities.update(process_list[0])
        for process_set in process_list:
            entities = entities.intersection(process_set)

        return entities

    def get_tags_of_entity(self, entity: int) -> set[str]:
        tags = set()

        for tag in self.tags.keys():
            if entity in self.tags[tag]:
                tags.add(tag)

        return tags