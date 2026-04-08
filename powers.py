import pygame
from circleshape import CircleShape

class PowerUp(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.powerup_duration = 0
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius, 2)
        text_surface = self.font.render("S", True, (0, 255, 0))
        #Calculate the center to keep the "S" inside the circle
        #subtract half the text's width/height from the circle's center
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y))

        # 4. Blit (draw) the text onto the screen
        screen.blit(text_surface, text_rect)
        
