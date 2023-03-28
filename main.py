import arcade
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
from pyglet.math import Vec2
from arcade.experimental.lights import Light, LightLayer

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Unknown Game"

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = camera.CAMERA_SPEED

# Color of darkness
AMBIENT_COLOR = (10, 10, 10)
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
        self.ui = userinterface.Options()

        self.music_player = musicplayer.MusicPlayer()

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)
        # print(self.camera.camera_sprites)
        # self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        # self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

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

        # Start music
        self.music_player.play()

    def on_draw(self):
        """Render the screen"""

        # clear screen
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera.draw()

        # Do rendering here
        self.background_sprite_list.draw()
        self.player.draw_self()
        self.enemy_manager.draw_enemies()
        self.ui.draw_self()

    def on_update(self, delta_time: float):
        """Update logic goes here"""

        self.player.update(delta_time)
        self.enemy_manager.update(delta_time, self.player)
        self.ui.update_score()
        self.follow_camera()
        self.camera.follow_camera(self.player)

    def on_key_press(self, key, key_modifiers):
        """Called when a key on the keyboard is pressed"""

        self.player.receive_key_down(key)
        self.ui.recive_key_down(key)

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
