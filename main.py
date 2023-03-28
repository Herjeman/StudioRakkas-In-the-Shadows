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
from arcade.experimental.lights import Light, LightLayer
from pyglet.math import Vec2

# 1280x720 = HD
# 1920x1080 = FullHD
SCREEN_WIDTH = 1640
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Unknown Game"

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
        self.ui = userinterface.UserInterface()

        self.music_player = musicplayer.MusicPlayer()

        self.camera = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = camera.GameCamera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Light Related
        self.light_layer = None
        self.player_light = None

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

        # Light Related
        self.light_layer = LightLayer(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.light_layer.set_background_color(arcade.color.BLACK)
        # Creates a light that follows the player around.
        radius = 175
        mode = "soft"
        color = (
            arcade.csscolor.DARK_GOLDENROD
        )  # DARK_GOLDENROD  # PALE_GOLDENROD  # LIGHT_SLATE_GREY
        self.player_light = Light(0, 0, radius, color, mode)

        # Start music
        self.music_player.play()

    def on_draw(self):
        """Render the screen"""

        # clear screen
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera.camera_sprites.use()

        # Do rendering here
        # Light Related
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

        self.player.update(delta_time)
        self.enemy_manager.update(delta_time, self.player)
        self.camera.follow_camera(self.player)
        self.player_light.position = self.player.position.x, self.player.position.y
        self.ui.update_score()

    def on_key_press(self, key, key_modifiers):
        """Called when a key on the keyboard is pressed"""

        self.player.receive_key_down(key)
        self.ui.recive_key_down(key)

        if key == arcade.key.TAB:
            # --- Light related ---
            # We can add/remove lights from the light layer. If they aren't
            # in the light layer, the light is off.
            if self.player_light in self.light_layer:
                self.light_layer.remove(self.player_light)
            else:
                self.light_layer.add(self.player_light)

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
