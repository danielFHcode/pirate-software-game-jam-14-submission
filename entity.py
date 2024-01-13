from dataclasses import dataclass, field
import time
from typing import Optional
import pygame


@dataclass
class Vector2d:
    x: float
    y: float

    def __add__(self, other: "Vector2d | float | int") -> "Vector2d":
        if isinstance(other, (float, int)):
            return self + Vector2d(other, other)
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2d | float | int") -> "Vector2d":
        if isinstance(other, (float, int)):
            return self - Vector2d(other, other)
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector2d | float | int") -> "Vector2d":
        if isinstance(other, (float, int)):
            return self * Vector2d(other, other)
        return Vector2d(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: "Vector2d | float | int") -> "Vector2d":
        if isinstance(other, (float, int)):
            return self / Vector2d(other, other)
        return Vector2d(self.x / other.x, self.y / other.y)


@dataclass
class Transforms:
    position: Vector2d = field(default_factory=lambda: Vector2d(0, 0))
    center: Vector2d = field(default_factory=lambda: Vector2d(0, 0))
    size: Vector2d = field(default_factory=lambda: Vector2d(1, 1))
    angle: float = field(default_factory=lambda: 0)

    def __add__(self, other: "Transforms"):
        return Transforms(
            self.position + other.position,
            self.center + other.center,
            self.size * other.size,
            self.angle + other.angle,
        )

    def __sub__(self, other: "Transforms"):
        return Transforms(
            self.position - other.position,
            self.center - other.center,
            self.size / other.size,
            self.angle - other.angle,
        )


@dataclass
class Entity:
    transforms: Transforms = field(default_factory=lambda: Transforms())
    children: list["Entity"] = field(default_factory=lambda: [])

    def update(
        self,
        *,  # allow only named arguments
        delta_time: float,
        parent: Optional["Entity"],
        global_transforms: Transforms,
    ):
        ...

    def draw(
        self,
        *,  # allow only named arguments
        screen: pygame.Surface,
        parent: Optional["Entity"],
        global_transforms: Transforms,
    ):
        ...

    def __tick(
        self,
        delta_time: float,
        screen: pygame.Surface,
        parent: Optional["Entity"] = None,
        parent_transforms: Optional[Transforms] = None,
    ):
        global_transforms = (
            parent_transforms + self.transforms
            if parent_transforms
            else self.transforms
        )
        self.update(
            delta_time=delta_time,
            parent=parent,
            global_transforms=global_transforms,
        )
        self.draw(
            screen=screen,
            parent=parent,
            global_transforms=global_transforms,
        )
        for child in self.children:
            child.__tick(delta_time, screen, self, global_transforms)

    def tick(
        self,
        delta_time: float,
        screen: pygame.Surface,
        background_color: pygame.Color = pygame.Color("white"),
    ):
        screen.fill(background_color)
        self.__tick(delta_time, screen)
        pygame.display.flip()

    def mainloop(
        self,
        screen: pygame.Surface,
        background_color: pygame.Color = pygame.Color("white"),
    ):
        last_time_stamp = time.perf_counter()
        while pygame.QUIT not in map(lambda e: e.type, pygame.event.get()):
            time_stamp = time.perf_counter()
            delta_time = time_stamp - last_time_stamp
            self.tick(delta_time, screen, background_color)
            last_time_stamp = time_stamp
