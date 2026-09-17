from ecs_engine.general.tags import Tags

def add_tag(entity: int, tag: str, tag_system: Tags) -> None:
    tag_system.register(entity, tag)