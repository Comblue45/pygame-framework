import pygame

class Window:
    
    def __init__(
        self,
        size: tuple[int, int] = (800, 800),
        title: str = "Pygame Window"
        ) -> None:
        self._size = size
        self._title = title

        pygame.init()
        self.screen = pygame.display.set_mode(self._size)
        pygame.display.set_caption(self._title)
        self.clock = pygame.time.Clock()

    def blit(self, surface: pygame.Surface, position: tuple[int, int]|pygame.Vector2) -> None:
        self.screen.blit(surface, position)
    def color_background(self, color: str) -> None:
        self.screen.fill(color)
    def render(self) -> None:
        pygame.display.flip()

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if self._title == title:
            return

        self._title = title
        pygame.display.set_caption(self._title)

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]) -> None:
        if self._size == size:
            return

        self._size = size
        self.screen = pygame.display.set_mode(self._size)

    def quit(self) -> None:
        pygame.quit