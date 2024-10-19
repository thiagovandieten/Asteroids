import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
    
    def check_collision(self, cShape):
        distance = self.position.distance_to(cShape.position)
        return True if distance < self.radius + cShape.radius else False
        
    def draw(self, screen):
        # children must override this method
        pass

    def update(self, dt):
        # children must override this method
        pass