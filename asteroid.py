from circleshape import *
from logger import log_event
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_velo1 = self.velocity.rotate(new_angle)
        new_velo2 = self.velocity.rotate(new_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        baby_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        baby_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        baby_asteroid1.velocity = new_velo1 * 1.2
        baby_asteroid2.velocity = new_velo2 * 1.2