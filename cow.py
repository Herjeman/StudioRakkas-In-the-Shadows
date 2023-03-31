import arcade
import os
import enemymanager
import player
import random
import poop

from HelperClasses import vector
from GameObjectRework import sprite


class Cow:
    def __init__(
            self,
            spawn_x,
            spawn_y,
            enemy_manager,
            active_player,
            ):

        self.speed = 10
        self.move_direction = vector.zero()
        self.time_until_next_change = float(random.randint(0, 5))
        self.position = vector.Vector2(spawn_x, spawn_y)

        self.enemy_manager = enemy_manager
        self.active_player = active_player
        self.sfx_player = enemy_manager.sfx_player

        sprite_path = os.path.join("assets", "enemy_sprites", "cow_sprite.png")
        self.sprite, self.sprite_list = sprite.set_up_sprites(sprite_path, 3.5)

    def update(self, delta_time):

        self.change_direction(delta_time)
        self.move(delta_time)

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

    def move(self, delta_time):

        self.position += self.move_direction * self.speed * delta_time

        self.sprite.change_x = self.move_direction.x
        self.sprite.change_y = self.move_direction.y

    def draw_self(self):
        self.sprite_list.draw()

    def poop(self):
        if random.randint(0, 4) == 0:
            self.enemy_manager.active_poops.append(poop.Poop(self.position.x, self.position.y, self.active_player, -1))
            self.sfx_player.play_poop()

    def change_direction(self, delta_time):
        if self.time_until_next_change < 0:
            directions = \
                [
                    vector.zero(),
                    vector.up(),
                    vector.down(),
                    vector.left(),
                    vector.right()
                ]

            for direction in directions:
                if self.move_direction.x == direction.x and self.move_direction.y == direction.y:
                    directions.remove(direction)
                    break

            self.move_direction = random.choice(directions)
            self.time_until_next_change = float(random.randint(1, 6))

            self.poop()

        else:
            self.time_until_next_change -= delta_time



