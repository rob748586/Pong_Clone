from random import choice
from pygame import Vector2
from ball import Ball

class Ball_Path_Prediction(Ball):
    def __init__(self, pong_game):
        super().__init__(pong_game)
        self.settings = pong_game.settings
        self.delay = 2
        self.moving = True

    def _calculate_next_bounce_destination(self, ball):
        """ predicts the path of the ball in subsequent frames until a bounce occurs with over/undershoot error introduced at high speeds """
        self.position = Vector2(ball.position.x, ball.position.y)
        self.direction = Vector2(ball.direction.x, ball.direction.y)

        self.delay -= 1

        if ball.moving:
            while not self.test_for_boundary_collisions() and not self.position.x >= self.settings.player_2_default_x - self.rect.width:
                self.update(6)

            # generate a random overshoot to allow for occasional mistakes
            overshoot = choice(range(3)) + 2

            # apply the overshoot in either positive or negative direction to introduce error for AI player
            return self.position.y + (ball.ball_speed * choice([overshoot, -overshoot]))   # overshoot/undershoot at speed

        else:
            return self.settings.paddle_default_y




