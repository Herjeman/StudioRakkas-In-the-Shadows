import arcade
import os

from GameObjectRework import sprite
from HelperClasses import vector


class Poop:
    def __init__(self, spawn_x, spawn_y, active_player, decay_time: float, scale: float = 2.5):

        self.position = vector.Vector2(spawn_x, spawn_y)

        self.active_width = 16 * scale
        self.active_height = 16 * scale
        self.hit_box = arcade.get_rectangle_points(self.position.x, self.position.y, self.active_width, self.active_height)
        self.affected_objects = []

        self.active_player = active_player

        if decay_time <= 0:
            self.will_ever_decay = False
        else:
            self.decay_time = decay_time
            self.will_ever_decay = True

        sprite_path = os.path.join("assets", "enemy_sprites", "poop_sprite.png")
        self.sprite, self.sprite_list = sprite.set_up_single_sprite(sprite_path, scale)

    def update(self, delta_time):

        if self.active_player not in self.affected_objects and arcade.are_polygons_intersecting(self.active_player.get_hit_box(), self.hit_box):
            self.active_player.slow_down()
            self.affected_objects.append(self.active_player)

        for instance in self.affected_objects:
            if not arcade.are_polygons_intersecting(instance.get_hit_box(), self.hit_box):
                self.affected_objects.remove(instance)
                instance.remove_slow_down()

        self.sprite.set_position(self.position.x, self.position.y)
        self.sprite_list.update()
        self.sprite_list.update_animation()

        if self.will_ever_decay:
            self.decay_time -= delta_time
            if self.decay_time < 0:
                return True
        return False

    def draw_self(self):

        self.sprite.draw()


