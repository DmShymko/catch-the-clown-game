import pygame

class GameOverScene:
    def __init__(self, font, colors, screen_rect):
        blue, yellow = colors

        self.screen_rect = screen_rect

        self.text = font.render("GAME OVER", True, blue, yellow)
        self.text_rect = self.text.get_rect(center=screen_rect.center)

        self.cont = font.render("Click anywhere to continue", True, yellow, blue)
        self.cont_rect = self.cont.get_rect(
            center=(screen_rect.centerx, screen_rect.centery + 64)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True   # сигнал о перезапуске

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.cont, self.cont_rect)
