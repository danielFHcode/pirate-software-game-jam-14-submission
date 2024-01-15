import pygame
from entity import Entity, Transforms
from dataclasses import dataclass, field

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
        surface = pygame.Surface((global_transforms.size.x, global_transforms.size.y))
        surface.fill(self.color)
        screen.blit(
            pygame.transform.rotozoom(surface, global_transforms.angle, 1),
            (
                global_transforms.position.x + global_transforms.center.x,
                global_transforms.position.y + global_transforms.center.x,
            ),
        )