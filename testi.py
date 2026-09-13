import pygame

from core_abstraction.game import Game
from core_abstraction.entity import Entity

def readyy() -> None:
    print("Entity setup!")

def updati(dt: float) -> None:
    print(f"Delta time: {dt}")

game = Game()
game.setup()

surface = pygame.Surface((100,100))
surface.fill("red")
entity = Entity(surface)
entity.ready = readyy
entity.update = updati

game.add_entity(entity)

game.start()