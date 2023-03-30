import pyglet.math

import cow
import enemy
import gamemanager
import main
import player
import random
import userinterface
from HelperClasses import vector


class EnemyManager:
    def __init__(self):
        self.spawn_interval = 5
        self.spawn_timer = self.spawn_interval
        self.active_enemies = []
        self.active_cows = []
        self.active_poops = []
        self.cow_spawn_chance_percent = 10
        self.minimum_spawn_distance = 300
        self.maximum_spawn_distance = 500
        self.following_enemies = 0

    def update(self, delta_time, active_player: player.Player):

        # Check spawn timer and spawn enemy if time
        self.spawn_timer -= delta_time
        if self.spawn_timer < 0:
            self.spawn_new_enemy(active_player)
            self.spawn_timer = self.spawn_interval

        # Update enemies
        for instance in self.active_poops:
            if instance.update(delta_time):
                self.active_poops.remove(instance)
                del instance

        for instance in self.active_cows:
            instance.update(delta_time)

        for instance in self.active_enemies:
            instance.update(delta_time, active_player, self)

        # Update score
        main.GAME_MANAGER.update_score(self.following_enemies, delta_time)

    def draw_enemies(self):

        for instance in self.active_poops:
            instance.draw_self()

        for instance in self.active_cows:
            instance.draw_self()

        for instance in self.active_enemies:
            instance.draw_self()

    def spawn_new_enemy(self, active_player):
        """Spawns a new enemy, on rare occasions a cow instead"""

        # find a spot at a reasonable distance from player
        offset = random.randint(
            self.minimum_spawn_distance, self.maximum_spawn_distance
        )

        spawn_position = (
            active_player.position + vector.get_random_unit_vector() * offset
        )

        if random.randint(1, 100) <= self.cow_spawn_chance_percent:
            # Spawn a cow instead of a ghost
            self.active_cows.append(cow.Cow(spawn_position.x, spawn_position.y, self, active_player))
            return

        max_speed = random.randint(300, 495)
        acceleration = random.randint(20, 50)
        scale = random.randint(4, 8)
        self.active_enemies.append(enemy.Enemy(spawn_position.x, spawn_position.y, max_speed, acceleration, scale))

    def is_point_colliding_with_enemy(self, point: pyglet.math.Vec2, exclude: enemy = None):
        """Returns true if the point is colliding with an enemy. An object can be passed to exclude, intended to skip
        self"""

        for instance in self.active_enemies:
            if instance == exclude:
                continue

            if instance.sprite.collides_with_point((point.x, point.y)):
                return True

        return False
