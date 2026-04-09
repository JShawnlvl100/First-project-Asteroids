import pygame
from constants import *
def draw_start_screen(screen):
    # logic to blit text to the screen
    font = pygame.font.SysFont("Arial", 64)
    title_surface = font.render("ASTEROIDS", True, (255, 255, 255))
    screen.blit(title_surface, (SCREEN_WIDTH/2, SCREEN_WIDTH/2))

def draw_game_over_screen(screen):
    # logic to blit text to the screen
    font = pygame.font.SysFont("Arial", 64)
    game_over_surface = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_surface, (SCREEN_WIDTH/2, SCREEN_WIDTH/2))