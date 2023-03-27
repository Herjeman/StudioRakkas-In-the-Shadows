import guard
import main
import player
import random
import userinterface
from HelperClasses import vector


class GuardManager:

    def __init__(self):
        self.spawn_interval = 5
        self.spawn_timer = self.spawn_interval
        self.active_guards = []
        self.minimum_spawn_distance = 300
        self.maximum_spawn_distance = 500

    def update(self, delta_time, active_player):

        self.spawn_timer -= delta_time

        if self.spawn_timer < 0:
            self.spawn_new_guard(active_player)
            self.spawn_timer = self.spawn_interval

        for instance in self.active_guards:
            instance.update(delta_time, active_player)

    def draw_guards(self):
        for instance in self.active_guards:
            instance.draw_self()

    def spawn_new_guard(self, active_player):
        """Spawns a new guard"""

        # find a spot at a reasonable distance from player
        offset = random.randint(self.minimum_spawn_distance, self.maximum_spawn_distance)

        spawn_position = active_player.position + vector.get_random_unit_vector()*offset

        self.active_guards.append(guard.Guard(spawn_position.x, spawn_position.y))
