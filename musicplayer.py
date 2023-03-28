import arcade
import os


class MusicPlayer:

    def __init__(self):
        song_path = os.path.join("assets", "audio", "music1.mp3")
        self.song = arcade.load_sound(song_path)

        self.volume = 1
        self.pan = 0.0
        self.loop = True
        self.speed = 1.0

        self.active_music_player = None

    def play(self):
        self.active_music_player = arcade.play_sound(self.song, self.volume, self.pan, self.loop, self.speed)

    def stop(self):
        arcade.stop_sound(self.active_music_player)
