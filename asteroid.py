from circleshape import *
from logger import log_event
from constants import *
from particle import Particle
from powers import PowerUp
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.base_velocity = velocity.copy() if velocity is not None else pygame.Vector2(0, 0)
        self.velocity = self.base_velocity.copy()

    def apply_speed_multiplier(self, multiplier):
        self.velocity = self.base_velocity * multiplier
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
        elif self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius

    def split(self):
        self.kill()
        for part in range(20):
            random_angle = random.uniform(0, 360)
            particle_velocity = pygame.Vector2(0, 1).rotate(random_angle)
            speed = random.uniform(50, 150)
            particle_velocity *= speed
            new_particle = Particle(self.position.x, self.position.y, random.uniform(2,5))
            new_particle.velocity = particle_velocity

        if self.radius <= ASTEROID_MIN_RADIUS:
            if random.random() < 0.05:
                new_powerup = PowerUp(self.position.x, self.position.y, POWERUP_RADIUS)
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_velo1 = self.velocity.rotate(new_angle)
        new_velo2 = self.velocity.rotate(new_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        

        Asteroid(self.position.x, self.position.y, new_radius, velocity=new_velo1 * 1.2)
        Asteroid(self.position.x, self.position.y, new_radius, velocity=new_velo2 * 1.2)
        
        
        