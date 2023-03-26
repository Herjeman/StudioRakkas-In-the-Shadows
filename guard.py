import arcade
import player
import os

from HelperClasses import vector


# TODO
# make guard animation work


class Guard:
    def __init__(self, spawn_x, spawn_y):

        self.speed = 400
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.follow_distance = 250
        self.set_up()

    def set_up(self):
        player_sprite = os.path.join("assets", "player", "player_sprite.png")

        self.sprite_list = arcade.SpriteList()
        self.sprite = arcade.AnimatedWalkingSprite()

        self.sprite.stand_right_textures = [
            arcade.load_texture(player_sprite, x=0, y=0, width=16, height=16)
        ]
        self.sprite.stand_left_textures = [
            arcade.load_texture(player_sprite, x=0, y=0, width=16, height=16)
        ]

        self.sprite.walk_down_textures = []
        self.sprite.walk_up_textures = []
        self.sprite.walk_right_textures = []
        self.sprite.walk_left_textures = []
        for i in range(4):
            self.sprite.walk_down_textures.append(
                arcade.load_texture(
                    player_sprite,
                    x=i * 16,
                    y=0,
                    width=16,
                    height=16,
                )
            )
            self.sprite.walk_up_textures.append(
                arcade.load_texture(
                    player_sprite,
                    x=i * 16,
                    y=16,
                    width=16,
                    height=16,
                )
            )
            self.sprite.walk_right_textures.append(
                arcade.load_texture(
                    player_sprite,
                    x=i * 16,
                    y=32,
                    width=16,
                    height=16,
                )
            )
            self.sprite.walk_left_textures.append(
                arcade.load_texture(
                    player_sprite,
                    x=i * 16,
                    y=48,
                    width=16,
                    height=16,
                )
            )
        self.sprite.scale = 4.5
        self.sprite_list.append(self.sprite)

    def update(self, delta_time, active_player: player.Player):

        distance_vector = self.position - active_player.position
        distance_to_player = distance_vector.get_magnitude()

        distance_vector = distance_vector.get_normalized()

        if distance_to_player < self.follow_distance:
            self.position = self.position - distance_vector * self.speed * delta_time

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

    def draw_self(self):
        # arcade.draw_rectangle_filled(
        # )
        self.sprite_list.draw()
        self.position.x, self.position.y, 20, 35, arcade.color.GHOST_WHITE
