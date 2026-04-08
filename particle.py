import pygame
import random
from circleshape import CircleShape

class Particle(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Add a timer here to track how long the particle lives
        self.lifetime = 0.5 

    def update(self, dt):
        # Move the particle based on its velocity
        self.position += (self.velocity * dt)
        # Reduce the lifetime every frame
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen):
        # Draw the particle as a small circle
        pygame.draw.circle(screen, "white", self.position, self.radius)