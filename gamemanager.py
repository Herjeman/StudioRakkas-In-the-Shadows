import musicplayer
#import main
class GameManager:
    def __init__(self):
        self.score = 0

        self.current_options = None
        self.open_options = False
        #self.music = musicplayer.MusicPlayer()

    def update_score(self, following_enemies: int, delta_time):
        self.score += (following_enemies**3) * delta_time
