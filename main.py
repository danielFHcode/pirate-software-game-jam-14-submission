from dataclasses import dataclass

import pygame
from entity import Entity


@dataclass
class Rectangle(Entity):
    color: pygame.Color
    x: float
    y: float
    width: float
    height: float

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(
            screen, self.color, pygame.Rect((self.x, self.y), (self.width, self.height))
        )
        return super().draw(screen)
