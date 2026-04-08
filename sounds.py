import pygame

try:
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except pygame.error:
    print("Warning: No audio device found. Game will run in silent mode.")
    AUDIO_AVAILABLE = False

class SoundManager:
    def __init__(self):
        # Load sounds into a dictionary or attributes
        self.warp = pygame.mixer.Sound("assets/playerwarp.wav")
        self.shoot = pygame.mixer.Sound("assets/playershoot.wav")
        self.powerup = pygame.mixer.Sound("assets/powerUp.wav")
        self.explosion = pygame.mixer.Sound("assets/asteroidexplosion.wav")
        
        # Set individual volumes
        self.warp.set_volume(0.4)
        self.shoot.set_volume(0.2)
        self.explosion.set_volume(0.4)

# Create a single instance to be used globally
sounds = SoundManager()