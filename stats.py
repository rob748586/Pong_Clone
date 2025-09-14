class Stats:
    """ Stores the scores for player 1 and 2 """
    def __init__(self):
        self.reset_scores()

    def reset_scores(self):
        """ Reset scores """
        self.player1_score = 0
        self.player2_score = 0