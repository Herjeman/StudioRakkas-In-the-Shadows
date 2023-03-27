import arcade
import os
from HelperClasses import vector


class Player:
    def __init__(self, spawn_x, spawn_y):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.move = vector.Vector2(0, 0)
        self.speed = 500

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
        self.sprite.scale = 2.5
        self.sprite_list.append(self.sprite)

    def update(self, delta_time):

        self.position = self.position + self.move.get_normalized() * self.speed * delta_time
        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

    def draw_self(self):

        self.sprite_list.draw()

    def receive_key_down(self, key: int):

        if key == arcade.key.W or key == arcade.key.UP:
            self.move.y += 1
            self.sprite.change_y += 1
            self.up = True

        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move.y -= 1
            self.sprite.change_y -= 1
            self.down = True

        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move.x -= 1
            self.sprite.change_x -= 1
            self.left = True

        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move.x += 1
            self.sprite.change_x += 1
            self.right = True

    def receive_key_up(self, key: int):

        if key == arcade.key.W or key == arcade.key.UP:
            self.move.y -= 1
            self.sprite.change_y -= 1
            self.right = False

        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move.y += 1
            self.sprite.change_y += 1
            self.right = False

        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move.x += 1
            self.sprite.change_x += 1
            self.right = False

        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move.x -= 1
            self.sprite.change_x -= 1
            self.right = False
