import arcade
import os

from GameObjectRework import sprite
from HelperClasses import vector


class Poop:
    def __init__(self, spawn_x, spawn_y, active_player, decay_time: float):

        self.position = vector.Vector2(spawn_x, spawn_y)

        self.active_width = 100
        self.active_height = 100
        self.hit_box = arcade.get_rectangle_points(self.position.x, self.position.y, self.active_width, self.active_height)
        self.affected_objects = []

        self.active_player = active_player

        if decay_time <= 0:
            self.will_ever_decay = False
        else:
            self.decay_time = decay_time
            self.will_ever_decay = True

        # sprite_path = os.path.join()
        # self.sprite, self.sprite_list = sprite.set_up_sprites(sprite_path)

    def update(self, delta_time):

        if self.active_player not in self.affected_objects and arcade.are_polygons_intersecting(self.active_player.get_hit_box(), self.hit_box):
            self.active_player.slow_down()
            self.affected_objects.append(self.active_player)

        for instance in self.affected_objects:
            if not arcade.are_polygons_intersecting(instance.get_hit_box(), self.hit_box):
                self.affected_objects.remove(instance)
                instance.remove_slow_down()

        if self.will_ever_decay:
            self.decay_time -= delta_time
            if self.decay_time < 0:
                return True
        return False

    def draw_self(self):

        arcade.draw_rectangle_filled(
            self.position.x,
            self.position.y,
            self.active_width,
            self.active_height,
            arcade.color.BROWN)


