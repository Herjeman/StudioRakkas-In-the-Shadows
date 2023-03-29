import arcade
import os


class SFXPlayer:
    def __init__(self):

        damage_sfx_path = os.path.join("assets", "audio", "oof.wav")
        self.sfx_damage = arcade.load_sound(damage_sfx_path)

        self.volume = 0.5
        self.pan = 0.0
        self.loop = False
        self.speed = 1.0
        self.volume_change = 0.1

        self.active_sfx_player = None

    def play_damage(self):
        self.active_sfx_player = arcade.play_sound(
            self.sfx_damage, self.volume, self.pan, self.loop, self.speed
        )

    def start(self):
        self.active_sfx_player.pause()

    def stop(self):
        self.active_sfx_player.play()

    def volume_up(self):
        if self.volume < 1:
            self.volume += self.volume_change
            self.song.set_volume(self.volume, self.active_sfx_player)

    def volume_down(self):
        if self.volume >= self.volume_change:
            self.volume -= self.volume_change
            self.song.set_volume(self.volume, self.active_sfx_player)
            print(self.song.get_volume(self.active_sfx_player))