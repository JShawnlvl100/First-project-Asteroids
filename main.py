import pygame
import sys
from score import *
from constants import * 
from logger import log_state
from logger import log_event
from player import *
from asteroid import *
from asteroidfield import *
from particle import *
from powers import *

def main():
    pygame.init()
    high_score = load_high_score()
    score = 0
    font = pygame.font.SysFont("Arial", 36)
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    PowerUp.containers = (drawable, updatable, powerups)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Particle.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    clock = pygame.time.Clock()
    dt = 0
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000
        updatable.update(dt)
        if score > high_score:
            high_score = score
        screen.fill("black")
        score_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        score_surface2 = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface2, (1060, 10))
        for draw in drawable:
            draw.draw(screen)
        for powerup in powerups:
            if powerup.collides_with(player):
                player.has_shield = True
                powerup.kill()
                print("shield activated!")
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.invulnerable_timer > 0:
                    continue
                log_event("player_hit")
                if player.has_shield:
                    player.has_shield = False
                    player.invulnerable_timer = 1
                    asteroid.split()
                else:
                    if score >= high_score:
                        save_high_score(score)
                    print("Game over!")
                    sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    score += 20
                    asteroid.split()
                    shot.kill()
        
        pygame.display.flip()
if __name__ == "__main__":
    main()
