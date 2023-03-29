import random

import arcade
import numpy
import math
from GameObjectRework import sprite
import enemymanager
import player
import os

from HelperClasses import vector


# TODO
# make guard animation work


class Enemy:
    def __init__(self, spawn_x, spawn_y, max_speed=400, acceleration=20, scale=4.5):

        self.sprite = max_speed
        self.sprite_list = acceleration

        self.max_speed = max_speed
        self.acceleration = acceleration
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.velocity = vector.Vector2(0, 0)

        self.follow_distance = 250
        self.stop_follow_distance = 750
        self.following = False

        self.sprite, self.sprite_list = sprite.set_up_sprites(
            os.path.join("assets", "enemy_sprites", "enemy1_sprite.png"), scale)

    def update(
            self,
            delta_time,
            active_player: player.Player,
            enemy_manager: enemymanager.EnemyManager,
    ):

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

        move_vector = active_player.position - self.position
        distance_to_player = move_vector.get_magnitude()

        move_vector = move_vector.get_normalized()

        enemy_manager.following_enemies += self.evaluate_follow(distance_to_player)

        if self.following:
            self.velocity += move_vector * self.acceleration

            if self.velocity.get_magnitude() > self.max_speed:
                self.velocity = self.velocity.get_normalized() * self.max_speed

        elif self.velocity.get_magnitude() != 0:
            self.velocity = self.velocity * 0.5

        self.move(delta_time)

        self.check_collision(active_player, move_vector * -1, enemy_manager, delta_time)

    def draw_self(self):
        self.sprite_list.draw()

    def move(self, delta_time):
        self.position += self.velocity * delta_time

    def evaluate_follow(self, distance_to_player):
        if distance_to_player < self.follow_distance:
            if not self.following:
                # Started following, add to enemies following
                self.following = True
                return 1
            else:
                return 0

        elif self.following and distance_to_player > self.stop_follow_distance:
            # Was following last cycle, subtract from enemies following
            self.following = False
            return -1

        else:
            return 0

    def check_collision(self, active_player, move_vector, enemy_manager, delta_time):
        # Check for collision with player
        if self.sprite.collides_with_sprite(active_player.sprite):
            # Collided with player, undo Move
            self.position += move_vector * self.max_speed * delta_time
            active_player.take_damage()

        # Check for collision with other enemies
        for enemy in enemy_manager.active_enemies:
            if enemy == self:
                continue
            try:
                if self.sprite.collides_with_sprite(enemy.sprite):
                    # Collided with other enemy, check if it is in the move direction
                    collision_direction: vector.Vector2 = self.position - enemy.position
                    collision_direction = collision_direction.get_normalized()

                    if vector.multiply_dot(move_vector, collision_direction) > 0:
                        # Collision is in move direction undo most of move
                        self.move(delta_time * -0.5)
                        break
            except ValueError:
                print(f'WARNING!!! Missing hitbox on {enemy}.')
