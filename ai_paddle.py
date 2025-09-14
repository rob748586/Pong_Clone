from paddle import Paddle

class AI_Paddle(Paddle):
    def __init__(self, x, y, colour, pong_game, ball_path_prediction):
        super().__init__(x, y, colour, pong_game)
        self.ball = pong_game.ball
        self.destination_y = y
        self.ball_path_prediction = ball_path_prediction

    def update(self):
        """ Move the paddle towards the predicted ball destination"""
        if self.destination_y > self.position.y + 30:
            self.start_move_downwards()
        elif self.destination_y < self.position.y - 30:
            self.start_move_upwards()
        else:
            self.stop_move_upwards()
            self.stop_move_downwards()

        super().update()

    def update_prediction(self):
        """ update the AI Paddles prediction of the balls destination """
        prediction = self.ball_path_prediction._calculate_next_bounce_destination(self.ball)

        self.destination_y = prediction
