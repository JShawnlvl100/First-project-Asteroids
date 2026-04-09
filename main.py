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
from sounds import sounds
from screens import *

def main():
    pygame.init()
    state = "START"
    is_paused = False
    high_score = load_high_score()
    score = 0
    font = pygame.font.SysFont("Arial", 36)
    pause_text = font.render(f"PAUSED", True, (255, 255, 255))
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
            if state == "START":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    for sprite in updatable:
                        sprite.kill()
                    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    asteroidfield = AsteroidField()
                    score = 0
                    state = "PLAYING"
            elif state == "PLAYING":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        is_paused = not is_paused
            elif state == "GAME_OVER":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # 'R' to Restart
                        state = "START"
                    elif event.key == pygame.K_q: # 'Q' to Quit
                        return
        dt_ms = clock.tick(60)
        dt = dt_ms / 1000
        if score > high_score:
            high_score = score
        screen.fill("black")
        if state == "START":
            draw_start_screen(screen)
        elif state == "PLAYING":
            score_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))
            screen.blit(score_surface, (10, 10))
            score_surface2 = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_surface2, (1060, 10))
            for draw in drawable:
                draw.draw(screen)
            if not is_paused:
                updatable.update(dt)
                for asteroid in asteroids:
                    for shot in shots:
                        if asteroid.collides_with(shot) == True:
                            log_event("asteroid_shot")
                            score += 20
                            asteroid.split()
                            sounds.explosion.play()
                            shot.kill()
                for powerup in powerups:
                    if powerup.collides_with(player):
                        sounds.powerup.play()
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
                            state = "GAME_OVER"
            else:
                text_rect = pause_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                screen.blit(pause_text, text_rect)
            

        elif state == "GAME_OVER":
            draw_game_over_screen(screen)

        pygame.display.flip()
if __name__ == "__main__":
    main()
