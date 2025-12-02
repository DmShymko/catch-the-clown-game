import pygame
from core.utils import resource_path

def load_sound(path, volume=1.0):
    sound = pygame.mixer.Sound(resource_path(path))
    sound.set_volume(volume)
    return sound

def play_music(path, volume=0.1):
    pygame.mixer.music.load(resource_path(path))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()
