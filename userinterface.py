import arcade
import arcade.gui

class UserInterface:
    def __init__(self):
        self.open_options = False
        self.points = 0


    def recive_key_down(self, key):
        if key == arcade.key.ESCAPE:
            if self.open_options:
                self.open_options = False
            else:
                self.open_options = True
    
    def draw_self(self):
        arcade.draw_text(self.points,120.0,300.0,
                         arcade.color.BABY_BLUE,40,80,'left')
        if self.open_options:
            arcade.draw_rectangle_filled(600, 360, 400, 600, arcade.color.RED)
                    # Create a vertical BoxGroup to align buttons
            self.v_box = arcade.gui.UIBoxLayout()

            # Create the buttons
            start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
            self.v_box.add(start_button.with_space_around(bottom=20))

            settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
            self.v_box.add(settings_button.with_space_around(bottom=20))
