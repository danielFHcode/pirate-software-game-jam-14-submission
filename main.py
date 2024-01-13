from dataclasses import dataclass, field

import pygame
from entity import Entity, Transforms, Vector2d


@dataclass
class Rectangle(Entity):
    color: pygame.Color = field(default_factory=lambda: pygame.Color(0, 0, 0, 0))

    def draw(
        self,
        *,
        screen: pygame.Surface,
        parent: Entity | None,
        global_transforms: Transforms
    ):
        # pygame.draw.rect(
        #     screen,
        #     self.color,
        #     pygame.Rect(
        #         (
        #             self.transforms.position.x + self.transforms.center.x,
        #             self.transforms.position.y + self.transforms.center.x,
        #         ),
        #         (self.transforms.size.x, self.transforms.size.y),
        #     ),
        # )
        surface = pygame.Surface((global_transforms.size.x, global_transforms.size.y))
        surface.fill(self.color)
        screen.blit(
            pygame.transform.rotozoom(surface, global_transforms.angle, 1),
            (
                global_transforms.position.x + global_transforms.center.x,
                # - global_transforms.size.x / 2,
                global_transforms.position.y + global_transforms.center.x,
                # - global_transforms.size.y / 2,
            ),
        )


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
