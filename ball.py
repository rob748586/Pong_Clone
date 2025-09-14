import pygame
from random import choice
from pygame.math import Vector2
from paddle import Paddle
from math import copysign

class Ball:
    """ A class representing the ball """
    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.settings = pong_game.settings

        self.colour = self.settings.ball_colour

        self.reset_ball()

    def reset_ball(self):
        """ Place the ball at the center of play, reset its speed and generate a random direction """
        self.position = Vector2(self.screen.get_rect().width / 2, self.screen.get_rect().height / 2)
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

        temp = choice([-6, -5, -4, -3, 3, 4, 5, 6]) * (1.0 / 8)

        self.moving = False

        self.direction = pygame.math.Vector2(temp, 1-temp).normalize()
        self.ball_speed = self.settings.ball_default_speed

    def bounce_off_paddle(self, paddle : Paddle):
        """ bounce the ball off the paddle,
        updating its direction then speeding up the ball """
        # calculate and normalize the new ball direction
        self.direction = self.calculate_bounce_vector(paddle).normalize()

        # speed up the ball every bounce
        self.speed_up()

    def calculate_bounce_vector(self, paddle: Paddle) -> pygame.Vector2:
        """ Tests the position the ball hits the paddle, and generate a new bounced direction
                that depends on the balls position on Y relative to the paddles centre. """
        output_vector = pygame.Vector2()

        # calculate the difference between the balls centre and the paddle centre
        difference  = self.position - paddle.position

        # assign a new Y value to the direction vector according to height on the paddle.
        if difference.y <  -self.settings.paddle_high_gradient_bounce_distance:
            output_vector.y = -5
        elif difference.y < -self.settings.paddle_mid_gradient_bounce_distance:
            output_vector.y = -4
        elif difference.y < -self.settings.paddle_low_gradient_bounce_distance:
            output_vector.y = -3
        elif difference.y > self.settings.paddle_low_gradient_bounce_distance:
            output_vector.y = 3
        elif difference.y > self.settings.paddle_mid_gradient_bounce_distance:
            output_vector.y = 4
        elif difference.y > self.settings.paddle_high_gradient_bounce_distance:
            output_vector.y = 5
        else:
            output_vector.y = copysign(3, self.direction.y)

        # create a new value for the x direction
        output_vector.x = 8 - abs(self.direction.y)

        # copy the sign of the difference vector to ensure the ball
        # moves away from the paddle on bounce
        output_vector.x = copysign(output_vector.x, difference.x)

        return output_vector

    def speed_up(self):
        """ speed up the ball (invoked when the ball bounces) """
        self.ball_speed *= self.settings.ball_speed_bounce_multiplier
        if self.ball_speed > self.settings.max_ball_speed:
            self.ball_speed = self.settings.max_ball_speed

    def test_for_boundary_collisions(self):
        # bouncing off top boundary
        if self.position.y - self.rect.height / 2 + self.direction.y * self.ball_speed <= self.settings.top_boundary:
            return True

        # bouncing off bottom boundary
        if self.position.y + self.rect.height / 2 + self.direction.y * self.ball_speed >= self.settings.bottom_boundary:
            return True

        return False

    def has_left_game_area(self):
        return self.position.x > self.screen.get_rect().width + self.rect.width or self.position.x < - self.rect.width

    def bounce_off_boundary(self):
        # flip y direction for bounce
        self.direction.y *= -1
        # speed up the ball every bounce
        self.speed_up()

    def render(self):
        """ Render the ball to the back buffer """
        pygame.draw.rect(self.screen, self.colour, self.rect)

    def update(self, slices):
        """ Update the ball position """

        if self.moving:
            self.position += self.direction * self.ball_speed * (1.0 / slices)

        # update the renderable rect to match new position
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def start_moving(self):
        self.moving = True


