import pygame
from settings import *
from core.assets import load_image, load_font
from core.sound import load_sound, play_music, stop_music
from scenes.gameplay import GamePlayScene
from scenes.gameover import GameOverScene

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Catch the Clown")
        self.clock = pygame.time.Clock()
        self.rect = self.screen.get_rect()

        self.assets = {
            "background": load_image(BACKGROUND_IMAGE),
            "clown": load_image(CLOWN_IMAGE),
            "font": load_font(FONT_PATH, 32)
        }

        self.sounds = {
            "hit": load_sound(HIT_SOUND, 0.1),
            "miss": load_sound(MISS_SOUND, 0.1)
        }

        self.gameplay = GamePlayScene(self.assets, self.sounds, self.rect)
        self.gameover = GameOverScene(self.assets["font"], (BLUE, YELLOW), self.rect)

        self.state = "GAME"

        play_music(MUSIC)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "GAME":
                self.gameplay.handle_event(event)

            elif self.state == "GAME_OVER":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.gameplay.reset(self.rect.center)
                    play_music(MUSIC)
                    self.state = "GAME"

    def update(self):

        if self.state == "GAME":
            self.gameplay.update(self.rect)

            if self.gameplay.lives <= 0:
                self.state = "GAME_OVER"
                stop_music()

    def draw(self):

        self.gameplay.draw(self.screen)

        if self.state == "GAME_OVER":
            self.gameover.draw(self.screen)
