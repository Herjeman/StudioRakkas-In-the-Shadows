import arcade
import player
import main
from pyglet.math import Vec2

CAMERA_SPEED = 1


class GameCamera:
    def __init__(self, width, height):

        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)

    def draw(self):
        self.camera_sprites.use()

    def follow_camera(self, player: player.Player):
        """Camera that follows player"""
        position = Vec2(
            player.position.x - main.SCREEN_WIDTH / 2,
            player.position.y - main.SCREEN_HEIGHT / 2,
        )
        self.camera_sprites.move_to(position, CAMERA_SPEED)
