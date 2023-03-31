import arcade
import player
import random
import time
from arcade.experimental.lights import Light, LightLayer
import main

# Color of darkness
AMBIENT_COLOR = (0, 0, 0)

# TODO
# Make light_point class
# Make lightning effect


class GameLight:
    """Lights in the game"""

    def __init__(self, width, height) -> None:

        self.light_layer = LightLayer(width, height)
        self.player_light = None
        self.flicker_timer = 3
        self.flickering = True
        #self.disco_mode = main.GAME_MANAGER.disco_mode

    # def create_light_point(
    #     self, x_pos: int, y_pos: int, radius: int, color: arcade.csscolor, mode: str
    # ):
    #     """Create a static light point
    #     Example:
    #     Create a small white light
    #     x_pos = 100,
    #     y_pos = 200,
    #     radius = 100,
    #     mode = "soft",
    #     color = arcade.csscolor.WHITE"""
    #     # Create a small white light
    #     light = Light(x_pos, y_pos, radius, color, mode)
    #     # self.light_layer.add(light)
    #     return light

    def player_flashlight(self):
        """Creates the light point that follows the player around"""
        x = 0
        y = 0
        r = random.randint(350, 350)
        c = random.choice(
            [
                arcade.csscolor.PALE_GOLDENROD,
                arcade.csscolor.LIGHT_GOLDENROD_YELLOW,
            ]
        )
        mode = "soft"
        if main.GAME_MANAGER.disco_mode:
            r = random.randint(150, 750)
            c = random.choice(
                [
                    arcade.csscolor.WHITE,
                    arcade.csscolor.PURPLE,
                    arcade.csscolor.GHOST_WHITE,
                    arcade.csscolor.PALE_VIOLET_RED,
                    arcade.csscolor.ORANGE_RED,
                    arcade.csscolor.BLUE_VIOLET,
                    arcade.csscolor.TURQUOISE,
                    arcade.csscolor.GREEN,
                    arcade.csscolor.MISTY_ROSE,
                    arcade.csscolor.LIGHT_YELLOW,
                ]
            )
            mode = random.choice(["soft", "hard"])
        player_light = Light(x, y, r, c, mode)
        return player_light

    def light_on(self):

        if self.player_light not in self.light_layer:
            self.light_layer.add(self.player_light)

    def update_flicker(self, player: player.Player, delta_time):
        """updates the light that follows player, centered to player"""
        if self.player_light not in self.light_layer:
            self.player_light = self.player_flashlight()
            self.light_layer.add(self.player_light)
        elif self.flicker_timer < 0:
            self.light_layer.remove(self.player_light)
            if not main.GAME_MANAGER.disco_mode:
                if self.flickering:
                    self.flicker_timer = random.randint(2, 15) / 20
                    self.flickering = False
                else:
                    self.flicker_timer = random.randint(2, 5)
                    self.flickering = True
        self.flicker_timer -= 1 * delta_time
        self.player_light.position = player.position.x, player.position.y

    # def receive_key_down(self, key: int):
    #     if key == arcade.key.TAB:
    #         if not self.disco_mode:
    #             self.disco_mode = True
    #         else:
    #             self.disco_mode = False
