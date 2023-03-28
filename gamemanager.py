class GameManager:
    def __init__(self):
        self.score = 0

        self.UI_sound = None
        self.UI_general = None
        self.current_options = None

    def update_score(self, following_enemies: int, delta_time):
        self.score += (following_enemies**3) * delta_time
