import arcade
from HelperClasses import vector

class Player:

    def __init__(self, spawn_x, spawn_y):

        self.up = False
        self.down = False
        self.right = False
        self.left = False

        self.position = vector.Vector2(spawn_x, spawn_y)

        self.move = vector.Vector2(0, 0)
        self.speed = 500

    def update(self, delta_time):

        self.position = self.position + self.move * self.speed * delta_time

    def draw_self(self):

        arcade.draw_rectangle_filled(self.position.x, self.position.y, 20, 35, arcade.color.RHYTHM)

    def receive_key_down(self, key: int):

        if key == arcade.key.W or key == arcade.key.UP:
            self.move.y += 1

        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move.y += -1

        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move.x += -1

        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move.x += 1

    def receive_key_up(self, key: int):

        if key == arcade.key.W or key == arcade.key.UP:
            self.move.y -= 1

        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move.y -= -1

        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move.x -= -1

        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move.x -= 1