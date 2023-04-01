import random

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

        button_sfx_path = os.path.join("assets", "audio", "Press Button.wav")
        self.sfx_button = arcade.load_sound(button_sfx_path)

        # -------- THUNDER --------
        self.thunder_sounds = []

        thunder_path = os.path.join("assets", "audio", "Thunder1.wav")
        self.thunder_sounds.append(arcade.load_sound(thunder_path))

        thunder_path = os.path.join("assets", "audio", "Thunder2.wav")
        self.thunder_sounds.append(arcade.load_sound(thunder_path))

        thunder_path = os.path.join("assets", "audio", "Thunder3.wav")
        self.thunder_sounds.append(arcade.load_sound(thunder_path))

        # --------- RAIN ----------
        rain_path = os.path.join("assets", "audio", "Rain.wav")
        self.sfx_rain = arcade.load_sound(rain_path)

        # ------- FOOTSTEPS -------
        self.footstep_sounds = []

        footstep_path = os.path.join("assets", "audio", "Grass1.wav")
        self.footstep_sounds.append(arcade.load_sound(footstep_path))

        footstep_path = os.path.join("assets", "audio", "Grass2.wav")
        self.footstep_sounds.append(arcade.load_sound(footstep_path))

        footstep_path = os.path.join("assets", "audio", "Grass3.wav")
        self.footstep_sounds.append(arcade.load_sound(footstep_path))

        footstep_path = os.path.join("assets", "audio", "Grass4.wav")
        self.footstep_sounds.append(arcade.load_sound(footstep_path))



        self.volume = main.GAME_MANAGER.sound_volume
        self.pan = 0.0
        self.loop = False
        self.speed = 1.0
        self.volume_change = 0.1
        self.sound_on = main.GAME_MANAGER.play_sound # True at setup

        self.rain: bool = False

        self.active_sfx_player = None
        self.active_thunder_player = None
        self.active_rain_player = None
        self.active_footstep_player = None

    def play_damage(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_damage, self.volume, self.pan, self.loop, self.speed
            )

    def play_poop(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_poop, self.volume * 0.5, self.pan, self.loop, self.speed
            )

    def play_moo(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_moo, self.volume * 0.7, self.pan, self.loop, self.speed
            )

    def play_poop_walk(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_poop_walk, self.volume, self.pan, self.loop, self.speed
            )

    def play_button_sound(self):
        if self.sound_on:
            self.active_sfx_player = arcade.play_sound(
                self.sfx_button, self.volume, self.pan, self.loop, self.speed
            )

    def play_thunder(self):
        if self.sound_on:
            sound = random.choice(self.thunder_sounds)
            self.active_thunder_player = arcade.play_sound(
                sound, self.volume, self.pan, self.loop, self.speed
            )

    def play_rain(self):
        if self.sound_on and not self.rain:
            self.active_rain_player = arcade.play_sound(
                self.sfx_rain, self.volume * 0.6, self.pan, True, self.speed
            )
            self.rain = True

    def stop_rain(self):
        if self.rain:
            if self.active_rain_player is not None:
                arcade.stop_sound(self.active_rain_player)
            self.rain = False

    def play_footstep(self):
        if self.sound_on:
            sound = random.choice(self.footstep_sounds)
            self.active_footstep_player = arcade.play_sound(
                sound, self.volume * 0.06, self.pan, self.loop, self.speed
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
