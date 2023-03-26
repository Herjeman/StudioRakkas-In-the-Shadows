import arcade
import player
import guard
import os
import guardmanager
from HelperClasses import vector
import userinterface

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Unknown Game"


class GameWindow(arcade.Window):
    """
    Main application class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player = player.Player(0, 0)
        self.guard = guard.Guard(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)

        self.background_sprite_list = None
        self.guard_manager = guardmanager.GuardManager()
        self.ui = userinterface.UserInterface()

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

    def on_draw(self):
        """Render the screen"""

        # clear screen
        self.clear()

        # Do rendering here
        self.background_sprite_list.draw()
        self.player.draw_self()
        self.guard.draw_self()
        self.ui.draw_self()

    def on_update(self, delta_time: float):
        """Update logic goes here"""

        self.player.update(delta_time)
        self.guard.update(delta_time, self.player)

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
