import arcade
import player

from HelperClasses import vector


class Guard:

    def __init__(self, spawn_x, spawn_y):

        self.speed = 400
        self.position = vector.Vector2(spawn_x, spawn_y)
        self.follow_distance = 250

    def update(self, delta_time, active_player: player.Player):

        distance_vector = self.position - active_player.position
        distance_to_player = distance_vector.get_magnitude()

        distance_vector = distance_vector.get_normalized()

        if distance_to_player < self.follow_distance:
            self.position = self.position - distance_vector * self.speed * delta_time

    def draw_self(self):
        arcade.draw_rectangle_filled(self.position.x, self.position.y, 20, 35, arcade.color.RHYTHM)
