import numpy
import pygame


pygame.init()

screen = pygame.display.set_mode((800, 450), pygame.RESIZABLE)

tree_image = pygame.transform.scale(pygame.image.load("./tree.jpg"), (500, 500))
grayscale_image = pygame.surfarray.make_surface(
    numpy.array(
        [
            [
                [(r * 0.298 + g * 0.587 + b * 0.114) for _ in range(3)]
                for r, g, b in color
            ]
            for color in pygame.surfarray.array3d(tree_image)  # type: ignore
        ]
    )
)


def circl():
    circle = pygame.Surface((500, 500))
    # circle.fill((0, 0, 0, 0), None, pygame.BLEND_RGBA_MULT)
    pygame.draw.circle(circle, "white", pygame.mouse.get_pos(), 150)
    circle.blit(tree_image, (0, 0), None, pygame.BLEND_RGBA_MULT)
    return circle


while pygame.QUIT not in map(
    lambda x: x.type, pygame.event.get()
):  # run application while there isn't a 'quit' event
    screen.fill("white")
    screen.blit(grayscale_image, (0, 0))
    screen.blit(circl(), (0, 0), None, pygame.BLEND_RGBA_ADD)
    pygame.display.update()
