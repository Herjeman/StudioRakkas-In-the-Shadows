import arcade


class GameManager:

    def __init__(self):
        self.score = 0

    def update_score(self, following_enemies: int, delta_time):
        self.score += (following_enemies ** 3) * delta_time
