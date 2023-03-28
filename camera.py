import arcade
import player
import main
import os
from pyglet.math import Vec2

CAMERA_SPEED = 0.08


class GameCamera:
    """Camera class"""

    def __init__(self, width, height):

        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)

    def draw_border(self):
        border_sprite = os.path.join("assets", "HUD", "switch_border_1640x1000.png")
        arcade.Sprite(
            border_sprite,
            center_x=main.SCREEN_WIDTH / 2,
            center_y=main.SCREEN_HEIGHT / 2,
        ).draw()
        # arcade.draw_rectangle_filled(
        #     main.SCREEN_WIDTH // 2, 20, main.SCREEN_HEIGHT, 40, arcade.color.ALMOND
        # )
        # text = (
        #     f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, "
        #     f"{self.camera_sprites.position[1]:5.1f})"
        # )

        # arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def follow_camera(self, player: player.Player):
        """Camera that follows player, centered screen"""
        position = Vec2(
            player.position.x - main.SCREEN_WIDTH / 2,
            player.position.y - main.SCREEN_HEIGHT / 2,
        )
        self.camera_sprites.move_to(position, CAMERA_SPEED)
