from dataclasses import dataclass, field

import pygame
from entity import Entity, Transforms, Vector2d
from utils import Rectangle 

class Something(Entity):
    def __init__(self):
        self.rect = Rectangle(
            color=pygame.Color("red"),
            transforms=Transforms(size=Vector2d(100, 100), position=Vector2d(10, 10)),
        )
        super().__init__(children=[self.rect])

    def update(
        self, *, delta_time: float, parent: Entity | None, global_transforms: Transforms
    ):
        self.rect.transforms.angle += 100 * delta_time


pygame.init()
screen = pygame.display.set_mode((800, 450), pygame.RESIZABLE)
Something().mainloop(screen)
