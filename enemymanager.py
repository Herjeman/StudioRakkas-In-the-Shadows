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
        for instance in self.active_enemies:
            instance.update(delta_time, active_player, self)

        # Update score
        main.GAME_MANAGER.update_score(self.following_enemies, delta_time)

    def draw_enemies(self):
        for instance in self.active_enemies:
            instance.draw_self()

    def spawn_new_enemy(self, active_player):
        """Spawns a new guard"""

        # find a spot at a reasonable distance from player
        offset = random.randint(
            self.minimum_spawn_distance, self.maximum_spawn_distance
        )

        spawn_position = (
            active_player.position + vector.get_random_unit_vector() * offset
        )

        self.active_enemies.append(enemy.Enemy(spawn_position.x, spawn_position.y))
