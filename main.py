import pygame
import math

pygame.init()
game_surface = pygame.display.set_mode([500, 500])

running = True


class Colour:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def to_tuple(self) -> tuple[int, int, int]:
        return self.red, self.green, self.blue


class Circle:
    def __init__(self, colour: Colour, radius: float, centre: tuple[int, int], surface: pygame.Surface):
        self.colour = colour
        self.radius = radius
        self.centre = centre
        self.surface = surface

    def draw(self):
        # Use the to_tuple method to get the RGB values
        return pygame.draw.circle(self.surface, self.colour.to_tuple(), self.centre, self.radius)

    def point_intersect(self, position: tuple[int, int]):
        x, y = position
        a, b = self.centre
        equation = (x - a) ** 2 + (y - b) ** 2 - self.radius ** 2
        if equation <= 0:
            return True

    def circle_intersect(self, circle: "Circle"):
        x1, y1 = self.centre
        r1 = self.radius
        x2, y2 = circle.centre
        r2 = circle.radius
        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

        if d == r1 + r2 or d == r2 - r1:  # intersect at one point
            return True
        elif r2 - r1 < d < r1 + r2:  # intersect at two points
            return True
        else:
            return False

    def set_colour(self, colour: Colour):
        self.colour = colour


circle1 = Circle(
    colour=Colour(5, 53, 123),
    radius=70.0,
    centre=(50, 50),
    surface=game_surface
)
circle2 = Circle(
    colour=Colour(5, 53, 123),
    radius=70.0,
    centre=(50, 50),
    surface=game_surface
)

while running:
    game_surface.fill((255, 255, 255))
    circle1.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if circle1.point_intersect(pygame.mouse.get_pos()):
                circle2.set_colour(Colour(23, 124, 54))

pygame.quit()
