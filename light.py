import arcade
import player
import random
import time
from arcade.experimental.lights import Light, LightLayer
import main

# Color of darkness - pitch black
AMBIENT_COLOR = (0, 0, 0)


class GameLight:
    """Lights in the game"""

    def __init__(self, width, height) -> None:

        self.light_layer = LightLayer(width, height)
        self.player_light = None
        self.flicker_timer = 3
        self.flickering = True
        self.disco_lights = None
        self.lightning_lights = None
        self.flash_lightning = False

    def create_light_point(
        self, x_pos: int, y_pos: int, radius: int, color: arcade.csscolor, mode: str
    ):
        """Create a static light point
        Example:
        Create a small white light
        x_pos = 100,
        y_pos = 200,
        radius = 100,
        mode = "soft",
        color = arcade.csscolor.WHITE"""

        light = Light(x_pos, y_pos, radius, color, mode)
        return light

    def player_flashlight(self):
        """Creates the light point that follows the player around"""
        if main.GAME_MANAGER.disco_mode:
            player_light = self.create_light_point(
                0,
                0,
                random.randint(150, 750),
                random.choice(
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
                ),
                mode=random.choice(["soft", "hard"]),
            )
        else:
            player_light = Light(
                0,
                0,
                random.randint(350, 350),
                random.choice(
                    [
                        arcade.csscolor.PALE_GOLDENROD,
                        arcade.csscolor.LIGHT_GOLDENROD_YELLOW,
                    ]
                ),
                "soft",
            )
        return player_light

    def light_on(self):

        if self.player_light not in self.light_layer:
            self.light_layer.add(self.player_light)

    def update_flicker(self, player, delta_time):
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

    # ------------------ Disco Mode -------------------------
    def create_disco_light_points(self):
        """Create a disco light point random somewhere on the screen"""
        disco_lights = self.create_light_point(
            random.randint(0, main.MAP_BOUNDARY),
            random.randint(0, main.MAP_BOUNDARY),
            random.randint(30, 70),
            random.choice(
                [
                    arcade.csscolor.WHITE,
                    arcade.csscolor.RED,
                    arcade.csscolor.BLUE,
                    arcade.csscolor.GREEN,
                    arcade.csscolor.PURPLE,
                    arcade.csscolor.YELLOW,
                ]
            ),
            "hard",
        )
        return disco_lights

    def disco_mode(self, delta_time):
        """disco mode on/off"""
        if main.GAME_MANAGER.disco_mode:
            if self.disco_lights not in self.light_layer:
                self.disco_lights = self.create_disco_light_points()
                self.light_layer.add(self.disco_lights)
            elif self.flicker_timer < 0:
                self.light_layer.remove(self.disco_lights)
            self.flicker_timer -= 1 * delta_time**2

    # ------------------ Lightning -------------------------
    def receive_key_down(self, key: int):
        if key == arcade.key.L:
            if not self.flash_lightning:
                self.flash_lightning = True
            else:
                self.flash_lightning = False

    def create_lightning(self):
        """Create a lightning point"""
        l = self.create_light_point(0, 0, 5000, arcade.csscolor.LEMON_CHIFFON, "hard")
        return l

    def call_lightning(self, player):
        """lightning event"""
        if self.flash_lightning:
            if self.lightning_lights not in self.light_layer:
                self.lightning_lights = self.create_lightning()
                self.light_layer.add(self.lightning_lights)
            else:
                self.light_layer.remove(self.lightning_lights)
                self.light_layer.clear()
                self.flash_lightning = False
            self.lightning_lights.position = (
                player.position.x,
                player.position.y,
            )
