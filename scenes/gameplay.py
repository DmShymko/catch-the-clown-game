import pygame
from entities.clown import Clown
from settings import *

class GamePlayScene:
    def __init__(self, assets, sounds, screen_rect):
        self.font = assets["font"]
        self.bg = assets["background"]
        self.clown = Clown(assets["clown"], screen_rect, CLOWN_STARTING_VELOCITY)

        self.hit = sounds["hit"]
        self.miss = sounds["miss"]

        self.score = 0
        self.lives = PLAYER_STARTING_LIVES

        self.title = self.font.render("Catch the Clown", True, BLUE)
        self.title_rect = self.title.get_rect(topleft=(50,10))

    def reset(self, center):
        self.score = 0
        self.lives = PLAYER_STARTING_LIVES
        self.clown.reset(center, CLOWN_STARTING_VELOCITY)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.clown.rect.collidepoint(event.pos):
                self.hit.play()
                self.score += 1
                self.clown.accelerate(CLOWN_ACCELERATION)
                self.clown.random_direction()
            else:
                self.miss.play()
                self.lives -= 1

    def update(self, bounds):
        self.clown.move()
        self.clown.bounce(bounds)

    def draw(self, screen):
        screen.blit(self.bg, (0,0))
        screen.blit(self.title, self.title_rect)

        score = self.font.render(f"Score: {self.score}", True, YELLOW)
        lives = self.font.render(f"Lives: {self.lives}", True, YELLOW)

        screen.blit(score, (screen.get_width()-250,10))
        screen.blit(lives, (screen.get_width()-250,50))
        screen.blit(self.clown.image, self.clown.rect)
