import arcade

class SpriteContainer:
    def __init__(self, path, scale: float):
        self.sprite, self.sprite_list = set_up_sprites(path, scale)


def set_up_sprites(path, scale: float = 2.5):
    sprite_list = arcade.SpriteList()
    sprite = arcade.AnimatedWalkingSprite()

    sprite.stand_right_textures = [
        arcade.load_texture(path, x=0, y=0, width=16, height=16)
    ]
    sprite.stand_left_textures = [
        arcade.load_texture(path, x=0, y=0, width=16, height=16)
    ]

    sprite.walk_down_textures = []
    sprite.walk_up_textures = []
    sprite.walk_right_textures = []
    sprite.walk_left_textures = []
    for i in range(4):
        sprite.walk_down_textures.append(
            arcade.load_texture(
                path,
                x=i * 16,
                y=0,
                width=16,
                height=16,
            )
        )
        sprite.walk_up_textures.append(
            arcade.load_texture(
                path,
                x=i * 16,
                y=16,
                width=16,
                height=16,
            )
        )
        sprite.walk_right_textures.append(
            arcade.load_texture(
                path,
                x=i * 16,
                y=32,
                width=16,
                height=16,
            )
        )
        sprite.walk_left_textures.append(
            arcade.load_texture(
                path,
                x=i * 16,
                y=48,
                width=16,
                height=16,
            )
        )
    sprite.scale = 4.5
    sprite_list.append(sprite)
    return sprite, sprite_list


