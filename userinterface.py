import arcade
import arcade.gui
import main

class UserInterface:
    def __init__(self):
        self.open_options = False
        self.points = 100000000000000

# arcade.draw_text()
    def recive_key_down(self, key):
        if key == arcade.key.ESCAPE:
            if self.open_options:
                self.open_options = False
            else:
                self.open_options = True
    def draw_self(self):
        arcade.draw_text(self.points,main.SCREEN_WIDTH/32, main.SCREEN_HEIGHT/1.10,
                         arcade.color.BABY_BLUE,40,0,'left')
        if self.open_options:
            arcade.draw_rectangle_filled(main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/2, main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/1.25, arcade.color.RED)
                    # Create a vertical BoxGroup to align buttons
    
        # self.uimanager = arcade.gui.UIManager()
        # self.uimanager.enable()
        # start_button = arcade.gui.UIFlatButton(text="Start Game",width=200)
  
        # start_button.on_click = self.on_buttonclick
        
            
