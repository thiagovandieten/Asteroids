import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            pygame.color.Color(255,255,255),
            self.position,
            self.radius,
            2
        )

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)