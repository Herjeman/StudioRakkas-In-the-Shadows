import arcade
import os
from HelperClasses import vector
from GameObjectRework import sprite


class Player:
    def __init__(self, spawn_x, spawn_y, sfx_player, game_window):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.move = vector.Vector2(0, 0)
        self.speed = 500
        self.hp = 100
        self.slow = False
        self.game_window = game_window

        sprite_path = os.path.join("assets", "player", "player_sprite.png")
        # sprite_path = os.path.join("assets", "enemy_sprites", "slime_red2.png")
        self.sprite, self.sprite_list = sprite.set_up_sprites(sprite_path)
        self.sfx_player = sfx_player

    def update(self, delta_time):

        if self.hp < 100:
            # Five seconds to regen from 1 hp
            self.hp += int(20 * delta_time)

        if self.slow:
            delta_time = delta_time * 0.2

        self.position = (
            self.position + self.move.get_normalized() * self.speed * delta_time
        )

        self.process_collision(delta_time)

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

    def process_collision(self, delta_time):
        cows = self.game_window.enemy_manager.active_cows

        for cow in cows:
            if self.sprite.collides_with_sprite(cow.sprite):
                direction = self.position - cow.position
                direction = direction.get_normalized()

                self.position = self.position + direction * self.speed * delta_time
        # self.sprite.set_hit_box(self.get_hit_box())
        # print(self.get_hit_box())
        # self.sprite.set_hit_box([
        #    (-20, -40),
        #    (-20, 40),
        #    (20, 40),
        #    (20, -40),
        # ])
        # if self.sprite.collides_with_sprite(self.game_window.border_layer):
        #     print("yessssssssss")
        try:
            collisions = arcade.check_for_collision_with_list(self.sprite, self.game_window.border_layer)
        except ValueError:
            print('WARNING, tried to access player hitbox before it was set')
            return

        if collisions:
            direction = self.position - vector.Vector2(collisions[0].center_x, collisions[0].center_y)
            direction = direction.get_normalized()
            self.position = self.position + direction * self.speed * delta_time * 1.5
        #print(self.game_window.border_layer.position)



    def take_damage(self, delta_time, enemy, damage=5):
        self.hp -= damage
        self.sfx_player.play_damage()

        direction = self.position - enemy.position
        direction = direction.get_normalized()

        self.position = self.position + direction * self.speed * delta_time * 5

        if self.hp <= 0:
            self.game_window.game_over = True

    def slow_down(self):
        self.slow = True
        self.sfx_player.play_poop_walk()

    def remove_slow_down(self):
        self.slow = False

    def get_hit_box(self):
        return arcade.get_rectangle_points(self.position.x, self.position.y, 16, 16)

