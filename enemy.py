import random

import arcade
import numpy
import math

import enemymanager
import player
import os

from HelperClasses import vector


# TODO
# make guard animation work


class Enemy:
    def __init__(self, spawn_x, spawn_y):

        self.speed = 400
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.follow_distance = 250
        self.stop_follow_distance = 500
        self.following = False

        self.set_up_sprite()

    def set_up_sprite(self):
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

    def update(
        self,
        delta_time,
        active_player: player.Player,
        enemy_manager: enemymanager.EnemyManager,
    ):

        move_vector = self.position - active_player.position
        distance_to_player = move_vector.get_magnitude()

        move_vector = move_vector.get_normalized()

        if distance_to_player < self.follow_distance:
            if not self.following:
                # Started following, add to enemies following
                enemy_manager.following_enemies += 1
                self.following = True

        elif self.following and distance_to_player > self.stop_follow_distance:
            # Was following last cycle, subtract from enemies following
            enemy_manager.following_enemies -= 1
            self.following = False

        if self.following:
            self.position -= move_vector * self.speed * delta_time

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

        # Process collision
        collided = False

        if self.sprite.collides_with_sprite(active_player.sprite):
            # Collided with player, undo Move
            self.position += move_vector * self.speed * delta_time

        if not collided:
            for enemy in enemy_manager.active_enemies:
                if enemy == self:
                    continue

                if self.sprite.collides_with_sprite(enemy.sprite):
                    # Collided with other enemy, check if it is in the move direction
                    collision_direction: vector.Vector2 = self.position - enemy.position
                    collision_direction = collision_direction.get_normalized()

                    if vector.multiply_dot(move_vector, collision_direction) > 0.3:
                        # Collision is in move direction
                        collided = True
                        break

        if collided:
            # Undo move
            self.position += move_vector * self.speed * delta_time

            # Rotate Move
            collision_angle = numpy.degrees(vector.compare_angle(move_vector, collision_direction))

            if 90 < collision_angle < 180:
                collision_direction = collision_direction.get_rotated(-65)

            elif 180 < collision_angle < 210:
                collision_direction = collision_direction.get_rotated(65)

            move_vector = collision_direction

            # Redo move at lower speed
            self.position += move_vector * self.speed * delta_time * 0.5


    def draw_self(self):
        # arcade.draw_rectangle_filled(
        # )
        self.sprite_list.draw()
