import arcade
import os
import main


class SFXPlayer:
    def __init__(self, window_class):

        damage_sfx_path = os.path.join("assets", "audio", "oof.wav")
        self.sfx_damage = arcade.load_sound(damage_sfx_path)

        poop_sfx_path = os.path.join("assets", "audio", "poop.wav")
        self.sfx_poop = arcade.load_sound(poop_sfx_path)

        poop_walk_sfx_path = os.path.join("assets", "audio", "poop_walk.wav")
        self.sfx_poop_walk = arcade.load_sound(poop_walk_sfx_path)

        moo_sfx_path = os.path.join("assets", "audio", "moo.wav")
        self.sfx_moo = arcade.load_sound(moo_sfx_path)

        self.volume = main.GAME_MANAGER.sound_volume
        self.pan = 0.0
        self.loop = False
        self.speed = 1.0
        self.volume_change = 0.1
        self.sound_on = main.GAME_MANAGER.play_sound # True at setup

        self.active_sfx_player = None

    def play_damage(self):
        if self.sound_on:
            print(main.GAME_MANAGER.play_sound)
            self.active_sfx_player = arcade.play_sound(
                self.sfx_damage, self.volume, self.pan, self.loop, self.speed
            )

    def play_poop(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_poop, self.volume, self.pan, self.loop, self.speed
            )

    def play_moo(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_moo, self.volume, self.pan, self.loop, self.speed
            )

    def play_poop_walk(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_poop_walk, self.volume, self.pan, self.loop, self.speed
            )

    def sound_enabled(self):
        self.sound_on = True

    def sound_disabled(self):
        self.sound_on = False

    def volume_up(self):
        if self.volume < 1:
            self.volume += self.volume_change
            main.GAME_MANAGER.sound_volume += main.GAME_MANAGER.sound_volume

    def volume_down(self):
        if self.volume >= self.volume_change:
            self.volume -= self.volume_change
            main.GAME_MANAGER.sound_volume -= main.GAME_MANAGER.sound_volume