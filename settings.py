import pygame

class Settings:
    """ Default settings for various classes in Pong clone. """
    def __init__(self):
        """ Initialise default values. """
        # game states
        self.SHOW_TITLE_SCREEN = 0,
        self.GAME_SCREEN = 1,
        self.WIN_LOSE_SCREEN = 2

        # bg defaults
        self.bg_colour = (0, 0, 0)
        self.boundary_colour = (55, 255, 55)
        self.text_colour = (55, 255, 55)

        # paddle defaults
        self.player_1_default_x = 100
        self.player_1_colour = (255, 55, 55)

        self.player_2_default_x = 1180
        self.player_2_colour = (55, 55, 255)

        self.paddle_speed = 12.0
        self.paddle_width = 24
        self.paddle_height = 150
        self.paddle_default_y = 410
        self.paddle_high_gradient_bounce_distance = 60
        self.paddle_mid_gradient_bounce_distance = 45
        self.paddle_low_gradient_bounce_distance = 30
        self.paddle_colour = (55, 255, 55)

        # number of time slices used to stagger
        # movement to aid collision detection at speed.
        self.time_slices_count = 25
        self.UPDATE_PREDICTION = pygame.USEREVENT + 1
        self.BALL_START_MOVEMENT = self.UPDATE_PREDICTION + 1

        # scoreboard defaults
        self.scoreboard_text_centrey = 53

        # ball defaults
        self.ball_colour = (55, 255, 55)
        self.ball_default_speed = 6
        self.ball_speed = self.ball_default_speed
        self.ball_speed_bounce_multiplier = 1.1
        self.max_ball_speed = 30

        # the y values of the play boundaries the ball should bounce off
        self.top_boundary = 100
        self.bottom_boundary = 700
