import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            pygame.color.Color(255,255,255),
            self.position,
            self.radius
            )
    
    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        random_angle = random.uniform(20,50)
        a  = pygame.Vector2(self.velocity).rotate(random_angle)
        b  = pygame.Vector2(self.velocity).rotate(-random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
        new_asteroid.velocity = a * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        new_asteroid_2.velocity = b * 1.2
