import pygame

class Player_Win_Screen:
    def __init__(self, pong_game, message):
        self.settings = pong_game.settings
        self.screen = pong_game.screen

        # title text
        self.title = pygame.font.SysFont(None, 64,).render(f"{message}", True, self.settings.text_colour)
        self.title_rect = self.title.get_rect()
        self.title_rect.centerx = self.screen.get_rect().centerx
        self.title_rect.centery = 300

        # press any key text
        self.subtitle = pygame.font.SysFont(None, 24, ).render("Press any key to return to the title screen...", True, self.settings.text_colour)
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.centerx = self.screen.get_rect().centerx
        self.subtitle_rect.top = self.title_rect.bottom + 20

    def show(self):
        waiting_for_input = True

        while waiting_for_input:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    waiting_for_input = False

            self.render()

            # flip the back buffer to the display
            pygame.display.flip()

    def render(self):
        pygame.draw.rect(self.screen, self.settings.bg_colour, self.screen.get_rect())
        self.screen.blit(self.title, self.title_rect)

        self.screen.blit(self.subtitle, self.subtitle_rect)



