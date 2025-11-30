import pygame

def load_image(path):
    return pygame.image.load(path).convert_alpha()

def load_font(path, size):
    return pygame.font.Font(path, size)
