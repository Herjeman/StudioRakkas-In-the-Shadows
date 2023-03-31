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
    def __init__(self, spawn_x, spawn_y, kind_sprite, max_speed=400, acceleration=20, scale=4.5):

        self.max_speed = max_speed
        self.acceleration = acceleration
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.velocity = vector.Vector2(0, 0)

        self.follow_distance = 250
        self.stop_follow_distance = 100000
        self.following = False

        sprite_path = os.path.join("assets", "enemy_sprites", kind_sprite)
        self.sprite, self.sprite_list = sprite.set_up_sprites(sprite_path, scale)

    def update(
        self,
        delta_time,
        active_player: player.Player,
        enemy_manager: enemymanager.EnemyManager,
    ):

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

        face_vector = self.velocity.get_snapped()

        self.sprite.change_x = face_vector.x
        self.sprite.change_y = face_vector.y

        self.move(delta_time)

        self.check_collision(active_player, move_vector * -1, enemy_manager, delta_time)

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

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
            active_player.take_damage(delta_time, self)

        # Check for collision with other enemies
        for enemy in enemy_manager.active_enemies:
            if enemy == self:
                continue
            try:
                if self.sprite.collides_with_sprite(enemy.sprite):
                    # Collided with other enemy, check if it is in the move direction
                    collision_direction: vector.Vector2 = self.position - enemy.position
                    collision_direction = collision_direction.get_normalized()

                    if vector.multiply_dot(self.velocity, collision_direction) > -0.3:
                        # Collision is in move direction undo move
                        self.move(delta_time * -1)

                        # Make enemy bounce off
                        self.velocity = (
                            collision_direction * self.velocity.get_magnitude()
                        )
                        self.move(delta_time * 0.6)

                        break
            except ValueError:
                print(f"WARNING!!! Missing hitbox on {enemy}.")


def get_basic_enemy():
    max_speed = 350
    acceleration = 25
    scale = 4.5
    kind_sprite = "slime_red2.png"

    return max_speed, acceleration, scale, kind_sprite


def get_small_fast_enemy():
    max_speed = 600
    acceleration = 10
    scale = 2.5
    kind_sprite = "enemy1_sprite.png"

    return max_speed, acceleration, scale, kind_sprite


def get_big_enemy():
    max_speed = 250
    acceleration = 18
    scale = 6.5
    kind_sprite = "enemy3_sprite.png"

    return max_speed, acceleration, scale, kind_sprite


def get_elite_enemy():
    max_speed = 400
    acceleration = 30
    scale = 8.5
    kind_sprite = "enemy2_sprite.png"

    return max_speed, acceleration, scale, kind_sprite


def get_random_enemy():
    rand = random.randint(1, 8)

    if rand < 4:
        return get_basic_enemy()
    elif rand < 6:
        return get_small_fast_enemy()
    elif rand < 8:
        return get_big_enemy()
    else:
        return get_elite_enemy()
