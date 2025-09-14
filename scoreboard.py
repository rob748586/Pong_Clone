import pygame

class ScoreBoard:
    """ The score board renderable """
    def __init__(self, pong_game):
        self.stats = pong_game.stats
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.update_scores()

        self.heading_image = pygame.font.SysFont(None, 64).render(f"PONG CLONE", True,
                                                                 self.settings.text_colour)
        self.heading_image_rect = self.heading_image.get_rect()
        self.heading_image_rect.centerx = self.screen.get_rect().width / 2
        self.heading_image_rect.centery = self.settings.scoreboard_text_centrey

    def update_scores(self):
        """ Update the images that are used to display the scores. """
        self.score1_image = pygame.font.SysFont(None, 64).render(f"{self.stats.player1_score}", True, self.settings.text_colour)
        self.score1_rect = self.score1_image.get_rect()
        self.score1_rect.centerx = 70
        self.score1_rect.centery = self.settings.scoreboard_text_centrey

        self.score2_image = pygame.font.SysFont(None, 64).render(f"{self.stats.player2_score}", True, self.settings.text_colour)
        self.score2_rect = self.score1_image.get_rect()
        self.score2_rect.centerx = self.screen.get_rect().width - 70
        self.score2_rect.centery = self.settings.scoreboard_text_centrey

    def render(self):
        """ Render the two score images to the screen. """
        if (self.score1_image == None or self.score2_image == None):
            self.update_scores()

        self.screen.blit(self.score1_image, self.score1_rect)
        self.screen.blit(self.score2_image, self.score2_rect)
        self.screen.blit(self.heading_image, self.heading_image_rect)
