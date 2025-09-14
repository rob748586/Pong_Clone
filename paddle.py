import pygame

class Paddle:
    """ Describes a paddle in Pong, and allows the paddle to be rendered to a screen. """
    def __init__(self, x, y, colour, pong_game):
        self.pong_game = pong_game
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.colour = colour

        # initialize paddle as not moving
        self.movement_delta = 0

        # create and center the paddle
        self.rect = pygame.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.centerx, self.rect.centery = x, y

        # set position vector to match the center of the paddle
        self.position = pygame.Vector2(self.rect.centerx, self.rect.centery)

    def update(self):
        """ Perform movement updates for paddle. """
        # check if paddle is moving upwards.
        if self.movement_delta < 0:
            if (self.position.y - self.settings.paddle_speed - self.settings.paddle_height / 2
                    >= self.settings.top_boundary):
                # update y then move paddle sprite to match new position
                self.position.y -= self.settings.paddle_speed * (1.0 / self.settings.time_slices_count)
                self.rect.centery = self.position.y

        # check if paddle is moving downwards.
        if self.movement_delta > 0:
            if (self.position.y + self.settings.paddle_speed + self.settings.paddle_height / 2
                    <= self.settings.bottom_boundary):
                # update y then move paddle sprite to match new position
                self.position.y += self.settings.paddle_speed * (1.0 / self.settings.time_slices_count)
                self.rect.centery = self.position.y

    def start_move_upwards(self):
        """ Set movement delta to -1 indicating that the paddle is moving upwards. """
        self.movement_delta = -1

    def start_move_downwards(self):
        """ Set movement delta to 1 indicating that the paddle is moving downwards. """
        self.movement_delta = 1

    def stop_move_upwards(self):
        """ If the paddle is moving upwards set the movement delta to 0 sto stop movement. """
        # check if paddle is moving upwards.
        if self.movement_delta == -1:
            self.movement_delta = 0

    def stop_move_downwards(self):
        """ If the paddle is moving downwards set the movement delta to 0 sto stop movement. """
        # check if paddle is moving downwards.
        if self.movement_delta == 1:
            self.movement_delta = 0

    def render(self):
        """ Render the paddle to the screen. """
        pygame.draw.rect(self.screen, self.colour, self.rect)
