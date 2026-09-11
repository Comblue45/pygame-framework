import pygame

class Time:

    def __init__(self, fps: int = 60) -> None:
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        self.running_time = 0.0

    def tick(self) -> float:
        self.dt = self.clock.tick(self.fps) / 1000
        self.running_time += self.dt
        return self.dt