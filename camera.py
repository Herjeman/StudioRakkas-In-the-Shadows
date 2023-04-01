import arcade
import player
import main
import os
from pyglet.math import Vec2

CAMERA_SPEED = 0.08
# VIEWPORT_MARGIN = 50


class GameCamera:
    """Camera class"""

    def __init__(self, width, height):

        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)
        self.view_bottom = 0
        self.view_left = 0

    def draw_border(self):
        # border_sprite = os.path.join("assets", "HUD", "switch_border_1640x1000.png")
        # arcade.Sprite(
        #     border_sprite,
        #     center_x=main.SCREEN_WIDTH / 2,
        #     center_y=main.SCREEN_HEIGHT / 2,
        # ).draw()
        """Draw the box that we shows player pos (X,Y).
        This is just for illustration purposes. DONT USE IN GAME"""
        arcade.draw_rectangle_filled(
            main.SCREEN_WIDTH / 2, 20, main.SCREEN_WIDTH, 40, arcade.color.ALMOND
        )
        text = (
            f"Player pos: (X:{self.camera_sprites.position[0]:5.1f}, "
            f"Y:{self.camera_sprites.position[1]:5.1f}) FOR TESTING ONLY"
        )

        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def draw_test_box(self):
        """Draw the box that we work to make sure the user stays inside of.
        This is just for illustration purposes. DONT USE IN GAME"""
        left_boundary = 50
        right_boundary = 2400 * 2 - 50
        top_boundary = 2400 * 2 - 50
        bottom_boundary = 50
        arcade.draw_lrtb_rectangle_outline(
            left_boundary,
            right_boundary,
            top_boundary,
            bottom_boundary,
            arcade.color.RED,
            2,
        )

    def follow_camera(self, player):
        """Camera that follows player, centered screen"""
        left_boundary = self.view_left
        right_boundary = self.view_left + main.MAP_BOUNDARY - main.SCREEN_WIDTH
        top_boundary = self.view_bottom + main.MAP_BOUNDARY - main.SCREEN_HEIGHT
        bottom_boundary = self.view_bottom

        screen_center_x = player.position.x - (self.camera_sprites.viewport_width / 2)
        screen_center_y = player.position.y - (self.camera_sprites.viewport_height / 2)

        # Don't let camera travel past 0 or over (map size * screen width)
        if screen_center_x < left_boundary:
            screen_center_x = 0
        if screen_center_x > right_boundary:
            screen_center_x = self.view_left + main.MAP_BOUNDARY - main.SCREEN_WIDTH
        if screen_center_y < bottom_boundary:
            screen_center_y = 0
        if screen_center_y > top_boundary:
            screen_center_y = self.view_bottom + main.MAP_BOUNDARY - main.SCREEN_HEIGHT

        player_centered = screen_center_x, screen_center_y
        self.camera_sprites.move_to(player_centered)
