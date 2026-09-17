from ecs_engine.general.tags import Tags

def remove_tag(entity: int, tag: str, tag_system: Tags) -> None:
    tag_system.check_out(entity, tag)