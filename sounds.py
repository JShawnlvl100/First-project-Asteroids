import pygame
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:
    pygame.mixer.init()
    AUDIO_AVAILABLE = True
except pygame.error:
    print("Warning: No audio device found. Game will run in silent mode.")
    AUDIO_AVAILABLE = False

class SoundManager:
    def __init__(self):
        # Load sounds into a dictionary or attributes
        self.warp = pygame.mixer.Sound(resource_path("assets/playerwarp.wav"))
        self.shoot = pygame.mixer.Sound(resource_path("assets/playershoot.wav"))
        self.powerup = pygame.mixer.Sound(resource_path("assets/powerUp.wav"))
        self.explosion = pygame.mixer.Sound(resource_path("assets/asteroidexplosion.wav"))
        
        # Set individual volumes
        self.warp.set_volume(0.4)
        self.shoot.set_volume(0.2)
        self.explosion.set_volume(0.4)

# Create a single instance to be used globally
sounds = SoundManager()