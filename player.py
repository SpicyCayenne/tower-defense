"""Class for storing all the player's info"""
class Player:
    """Class for storing all the player's info"""
    def __init__(self, score, lives):
        self.score = score
        self.lives = lives

    def update_score(self, amount):
        """Updates the current score by the given amount"""
        self.score += amount

    def lose_life(self):
        """Decrements the player's life total"""
        self.lives -= 1

PLAYER = Player(0, 20)
