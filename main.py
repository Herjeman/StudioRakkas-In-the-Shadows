import random

import arcade
import pyglet.math
import player
import enemy
import os
import enemymanager
import gamemanager
import sfxplayer
import userinterface
from HelperClasses import vector
import userinterface
import musicplayer
import camera
import light
from pyglet.math import Vec2
import game_ower_view
from GameObjectRework import sprite

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Unknown Game"

MAP_SIZE = 2400
SCALING = 2  # TODO - implement globally where needed
MAP_BOUNDARY = MAP_SIZE * SCALING
# Color of darkness
AMBIENT_COLOR = light.AMBIENT_COLOR
GAME_MANAGER = gamemanager.GameManager()


class GameWindow(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_thunder_cooldown = 0
        self.thunder_timer = 0
        self.background_sprite_list = None
        self.border_layer = None
        self.ground_layer = None
        self.game_over_view = None
        self.game_over = None
        self.player_light = None
        self.te_list = None
        self.pause = None
        self.light_layer = None
        self.light = None
        self.camera_gui = None
        self.camera = None
        self.ui = None
        self.player = None
        self.sfx_player = None
        self.music_player = None
        self.enemy_manager = None
        self.game_map = None
        """test"""
        # self.music_volume = 0.5
        # self.sound_volume = 0.5
        # self.play_music = True
        # self.play_sound = True

    def setup(self):
        """Sets up the game. Call to restart the game"""
        self.background_sprite_list = None

        self.music_player = musicplayer.MusicPlayer(self)
        self.sfx_player = sfxplayer.SFXPlayer(self)
        self.enemy_manager = enemymanager.EnemyManager(self)

        self.ui = userinterface.UserInterface(self.sfx_player, self.music_player, self)

        self.camera = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.light = light.GameLight(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer = self.light.light_layer
        self.pause = False
        self.game_over = False

        # Create Sprite Lists

        # MAP
        map_1 = os.path.join("assets", "map", "150x150.json")
        layer_options = {
            "ground": {
                "use_spatial_hash": True,
            },
            "border": {
                "use_spatial_hash": True,
            },
        }
        self.game_map = arcade.load_tilemap(map_1, SCALING, layer_options)
        self.end_of_map = self.game_map.width

        self.ground_layer = self.game_map.sprite_lists["ground"]
        self.border_layer = self.game_map.sprite_lists["border"]

        self.player = player.Player(
            SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, self.sfx_player, self
        )

        self.game_over_view = game_ower_view.GameOverView(self.music_player, self)

        self.light_layer.set_background_color(arcade.color.BLACK)
        self.player_light = self.light.player_light

        # Start music
        self.music_player.play()

    def on_draw(self):
        """Render the screen"""

        # clear screen
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera.camera_sprites.use()

        # Do rendering here

        # Rendered inside light layer
        with self.light_layer:
            self.ground_layer.draw()
            self.border_layer.draw()
            # self.background_sprite_list.draw()
            self.enemy_manager.draw_enemies()
            self.player.draw_self()

        self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        # self.camera.draw_test_box()
        # score is shown on ths layer
        self.camera.camera_gui.use()

        # use this if u want a border
        # self.camera.draw_border()

        self.ui.draw_self()
        if self.game_over:
            self.game_over_view.draw_self()

    def on_update(self, delta_time: float):
        """Update logic goes here"""
        if self.pause == False and self.game_over == False:
            self.player.update(delta_time)
            self.enemy_manager.update(delta_time, self.player)
            self.light.update_flicker(self.player, delta_time)
            self.light.disco_mode(delta_time)
            self.evaluate_thunder(delta_time)
            self.light.update_thunder()
            self.light.call_lightning(self.player)
            self.camera.follow_camera(self.player)
            self.ui.update_score()

    def on_key_press(self, key, key_modifiers):
        """Called when a key on the keyboard is pressed"""

        self.player.receive_key_down(key)
        self.ui.recive_key_down(key)
        # self.light.receive_key_down(key)

    def on_key_release(self, key, key_modifiers):
        """Called whenever a key on the keyboard is released"""

        self.player.receive_key_up(key)

    def on_mouse_motion(self, a, y, delta_x, delta_y):
        """Called when the mouse is moved"""

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def evaluate_thunder(self, delta_time):

        if self.thunder_timer < self.current_thunder_cooldown * 0.35:
            self.sfx_player.play_rain()
        elif self.thunder_timer < self.current_thunder_cooldown - 5:
            self.sfx_player.stop_rain()

        if self.thunder_timer < 0:
            self.light.do_lightning()
            self.sfx_player.play_thunder()
            self.thunder_timer = random.randint(20, 60)
            self.current_thunder_cooldown = self.thunder_timer

        else:
            self.thunder_timer -= delta_time


def main():
    """Main game function"""
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
