#
#import main
class GameManager:
    def __init__(self):
        self.score = 0

        self.current_options = None
        self.open_options = False
        # self.music = musicplayer.MusicPlayer()
        self.music_volume = 0.4
        self.sound_volume = 0.5
        self.play_music = True
        self.play_sound = True
        self.disco_mode = False

    def update_score(self, following_enemies: int, delta_time):
        self.score += (following_enemies**3) * delta_time
