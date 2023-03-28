import arcade
import os


class MusicPlayer:
    def __init__(self):
        song_path = os.path.join("assets", "audio", "in_the_shadows_2.wav")
        self.song = arcade.load_sound(song_path)

        self.volume = 0.5
        self.pan = 0.0
        self.loop = True
        self.speed = 1.0
        self.volume_change = 0.1

        self.active_music_player = None
        print("music innnitiated")
        
    def play(self):
        self.active_music_player = arcade.play_sound(
            self.song, self.volume, self.pan, self.loop, self.speed
        )

    def start(self):
        self.active_music_player.pause()

    def stop(self):
        self.active_music_player.play()

    def volume_up(self):
        if self.volume < 1:
            self.volume += self.volume_change
            self.song.set_volume(self.volume, self.active_music_player)

    def volume_down(self):
        if self.volume >= self.volume_change:
            self.volume -= self.volume_change
            self.song.set_volume(self.volume, self.active_music_player)
            print(self.song.get_volume(self.active_music_player))
