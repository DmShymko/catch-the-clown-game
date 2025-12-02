import pygame
from core.utils import resource_path

def load_image(path):
    return pygame.image.load(resource_path(path)).convert_alpha()

def load_font(path, size):
    return pygame.font.Font(resource_path(path), size)
