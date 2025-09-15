import pygame
import asyncio

class Title_Screen:
    def __init__(self, pong_game):
        self.settings = pong_game.settings
        self.screen = pong_game.screen
        self.clock = pygame.time.Clock()

        # title text
        self.title = pygame.font.SysFont(None, 64,).render("PONG CLONE", True, self.settings.text_colour)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = self.screen.get_rect().centerx
        self.title_rect.centery = 300

        # press any key text
        self.subtitle = pygame.font.SysFont(None, 24, ).render("Press any key to start...", True, self.settings.text_colour)
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.centerx = self.screen.get_rect().centerx
        self.subtitle_rect.top = self.title_rect.bottom + 20


    def render(self):
        pygame.draw.rect(self.screen, self.settings.bg_colour, self.screen.get_rect())
        self.screen.blit(self.title, self.title_rect)

        self.screen.blit(self.subtitle, self.subtitle_rect)



