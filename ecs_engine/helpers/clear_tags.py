from ecs_engine.general.tags import Tags

def clear_tags(entity: int, tag_system: Tags) -> None:
    for tag in tag_system.get_tags_of_entity(entity):
        tag_system.check_out(entity, tag)