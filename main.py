import arcade
import pyglet.math

import player
import enemy
import os
import enemymanager
import gamemanager
import userinterface
from HelperClasses import vector
import userinterface
import musicplayer
import camera
import light
from pyglet.math import Vec2

# 1280x720 = HD
# 1920x1080 = FullHDd
SCREEN_WIDTH = 1640
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Unknown Game"

# Color of darkness
AMBIENT_COLOR = light.AMBIENT_COLOR
GAME_MANAGER = gamemanager.GameManager()


class GameWindow(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player = player.Player(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
        self.enemy_manager = enemymanager.EnemyManager()
        # self.game_manager = gamemanager.GameManager()

        self.background_sprite_list = None

        self.music_player = musicplayer.MusicPlayer()

        self.ui = userinterface.UserInterface(self.music_player, self)

        self.camera = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.light = light.GameLight(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer = self.light.light_layer
        self.pause = False

    def setup(self):
        """Sets up the game. Call to restart the game"""

        # Create Sprite Lists
        self.background_sprite_list = arcade.SpriteList()

        # Creates a bigger background from one sprite
        for x in range(-128, 2000, 128):
            for y in range(-128, 1000, 128):
                sprite = arcade.Sprite(os.path.join("assets", "tile", "grass_400.png"))
                sprite.position = x, y
                self.background_sprite_list.append(sprite)

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
            self.background_sprite_list.draw()
            self.player.draw_self()
            self.enemy_manager.draw_enemies()
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)

        self.camera.camera_gui.use()

        # use this if u want a border
        # self.camera.draw_border()

        self.ui.draw_self()

    def on_update(self, delta_time: float):
        """Update logic goes here"""
        if self.pause == False:
            self.player.update(delta_time)
            self.enemy_manager.update(delta_time, self.player)
            self.camera.follow_camera(self.player)
            self.light.update(self.player)
            self.ui.update_score()

    def on_key_press(self, key, key_modifiers):
        """Called when a key on the keyboard is pressed"""

        self.player.receive_key_down(key)
        self.ui.recive_key_down(key)
        self.light.receive_key_down(key)

    def on_key_release(self, key, key_modifiers):
        """Called whenever a key on the keyboard is released"""

        self.player.receive_key_up(key)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
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


def main():
    """Main game function"""
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()

