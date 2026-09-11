import pygame

class Input:

    def __init__(self) -> None:
        self.update()

    def update(self) -> None:
        self.events = pygame.event.get()

        self.keys_pressed = pygame.key.get_pressed()
        self.keys_down = pygame.key.get_just_pressed()
        self.keys_released = pygame.key.get_just_released()

        self.mouse_pressed = pygame.mouse.get_pressed()
        self.mouse_down = pygame.mouse.get_just_pressed()
        self.mouse_released = pygame.mouse.get_just_released()
        self.mouse_position = pygame.mouse.get_pos()