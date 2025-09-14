import pygame
import asyncio
import sys

from ai_paddle import AI_Paddle
from ball_path_prediction import Ball_Path_Prediction
from paddle import Paddle
from ball import Ball
from player_win_screen import Player_Win_Screen
from scoreboard import ScoreBoard
from settings import Settings
from stats import Stats
from title_screen import Title_Screen


class Pong:
    """ Pong game, contains main event loop and screen rendering methods """
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.settings = Settings()

        self._initialize_game()

    def _initialize_game(self):
        """ Create Paddles and ball objects """
        title_screen = Title_Screen(self)
        title_screen.show()

        # set the timer to update the AI Paddles prediction every 100ms
        pygame.time.set_timer(self.settings.UPDATE_PREDICTION, 150)
        pygame.time.set_timer(self.settings.BALL_START_MOVEMENT, 1000, 1)

        self.ball = Ball(self)

        # used to predict the path the ball will take by AI
        self.path_prediction = Ball_Path_Prediction(self.ball)

        self.player1 = Paddle(self.settings.player_1_default_x,
                              self.settings.paddle_default_y,
                              self.settings.paddle_colour,
                              self)

        self.player2 = AI_Paddle(self.settings.player_2_default_x,
                                 self.settings.paddle_default_y,
                                 self.settings.paddle_colour,
                                 self,
                                self.path_prediction)

        self.stats = Stats()
        self.score_board = ScoreBoard(self)

    async def play_game(self):
        """ The main loop for the pong game"""
        while True:

            for n in range(self.settings.time_slices_count):
                # handle input events
                self._handle_input_events()

                # perform game logic
                self._perform_updates()
                self._check_ball_collisions()

            # render graphics
            self._draw_background()
            self._render_sprites()

            self.score_board.render()

            # flip the back buffer to the display
            pygame.display.flip()

            await asyncio.sleep(0)
            # maintain 60 fps
            self.clock.tick(60)

    def _handle_input_events(self):
        """ process input events from the event queue. """
        for event in pygame.event.get():
            # handle quit events
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and \
                    event.key == pygame.K_ESCAPE:
                sys.exit()

            if event.type == self.settings.BALL_START_MOVEMENT:
                self.ball.start_moving()

            # handle player specific events
            self._check_player1_events(event)
            self._check_player2_events(event)

    def _check_ball_collisions(self):
        """ invoke tests for ball collisions """
        self._test_ball_player1_collision(self.ball, self.player1)
        self._test_ball_player2_collision(self.ball, self.player2)
        self._test_ball_bounds_collisions(self.ball)

    def _test_ball_bounds_collisions(self, ball: Ball):
        """ Tests if the ball has hit the upper or lower boundaries,
        or left the play field on the left or right. """
        # Left play area on left side
        if ball.position.x < -ball.rect.width:
            ball.reset_ball()
            self.stats.player2_score += 1
            self.score_board.update_scores()
            pygame.time.set_timer(self.settings.BALL_START_MOVEMENT, 1000, 1)

            if self.stats.player2_score >= 9:
                Player_Win_Screen(self, "You Lose!!").show()
                self._initialize_game()


        # Left play area on right side
        if ball.position.x > self.screen.get_rect().width + ball.rect.width:
            ball.reset_ball()
            self.stats.player1_score += 1
            self.score_board.update_scores()
            pygame.time.set_timer(self.settings.BALL_START_MOVEMENT, 1000, 1)

            if self.stats.player1_score >= 9:
                Player_Win_Screen(self, "You Win!!").show()
                self._initialize_game()

        # top and bottom boundaries
        if ball.test_for_boundary_collisions():
            ball.bounce_off_boundary()

    def _test_ball_player1_collision(self, ball: Ball, player1: Paddle):
        """ Test if the ball bounces off player one's paddle. """
        # collision with player 1
        if pygame.sprite.collide_rect(ball, player1) and \
                ball.position.x > player1.position.x:
            ball.bounce_off_paddle(player1)

    def _test_ball_player2_collision(self, ball: Ball, player2: Paddle):
        """ Test if the ball bounces off player two's paddle. """
        # collision with player 2
        if pygame.sprite.collide_rect(ball, player2) and \
                ball.position.x < player2.position.x:
            ball.bounce_off_paddle(player2)

    def _draw_background(self):
        """ Draw the background onto the back buffer to clear it """
        pygame.draw.rect(self.screen, self.settings.bg_colour, self.screen.get_rect())
        pygame.draw.rect(self.screen, self.settings.boundary_colour, pygame.Rect(0, 0, self.screen.get_width(), self.settings.top_boundary))
        pygame.draw.rect(self.screen, self.settings.boundary_colour, pygame.Rect(0, self.settings.bottom_boundary, self.screen.get_width(), self.screen.get_height()))
        pygame.draw.rect(self.screen, self.settings.bg_colour, pygame.Rect(20, 20, self.screen.get_width() - 40, self.settings.top_boundary - 40))

    def _render_sprites(self):
        """ Render sprites to screen """
        self.player1.render()
        self.player2.render()
        self.ball.render()

    def _perform_updates(self):
        """ Perform updates on all game objects"""
        self.player1.update()
        self.player2.update()
        self.ball.update(self.settings.time_slices_count)

    def _check_player1_events(self, event):
        """ React to player 1's Input events. """
        # key has been pressed.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player1.start_move_upwards()

            if event.key == pygame.K_DOWN:
                self.player1.start_move_downwards()

        # key has been released.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.player1.stop_move_upwards()

            if event.key == pygame.K_DOWN:
                self.player1.stop_move_downwards()

    def _check_player2_events(self, event):

        # update prediction for ball destination for the AI paddle
        if event.type == self.settings.UPDATE_PREDICTION:
            self.player2.update_prediction()

async def main():
    game = Pong()
    await game.play_game()

asyncio.run(main())