import arcade
import arcade.gui
import main

class Options:
    def __init__(self):
        self.open_options = False
        self.points: int = 0
        self.uimanager = arcade.gui.UIManager()

# arcade.draw_text()
    def recive_key_down(self, key):
        if key == arcade.key.ESCAPE:
            if self.open_options:
                self.open_options = False
            else:
                self.open_options = True
                self.option_buttons()

    def update_score(self, score: float):
        self.points = int(score)

    def draw_self(self):
        arcade.draw_text(self.points, main.SCREEN_WIDTH/32, main.SCREEN_HEIGHT/1.10,
                         arcade.color.BABY_BLUE,40,40) #anchor_x="right", anchor_y="top" to channge to top right cornner
        if self.open_options:
            arcade.draw_rectangle_filled(main.SCREEN_WIDTH/2,main.SCREEN_HEIGHT/2, main.SCREEN_WIDTH/2, main.SCREEN_HEIGHT/1.25, arcade.color.RED)
            self.uimanager.draw()
            
    def option_buttons(self):
        self.uimanager.enable()
        resume_game_button = arcade.gui.UIFlatButton(text="Resume Game",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=resume_game_button)
        )
        resume_game_button.on_click = self.resume_game_button_klick
        self.uimanager.enable()
        new_game_button = arcade.gui.UIFlatButton(text="New Game",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=new_game_button)
        )
        new_game_button.on_click = self.new_game_button_klick
        sound_button = arcade.gui.UIFlatButton(text="Sound",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=sound_button)
        )
        sound_button.on_click = self.sound_button_klick
        quit_button = arcade.gui.UIFlatButton(text="Quit",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-100,
                child=quit_button)
        )
        quit_button.on_click = self.quit_game_button_klick

    def resume_game_button_klick(self, event):
        print("resume button", event)
        
    def new_game_button_klick(self, event):
        print("new game button", event) 

    def sound_button_klick(self, event):
        print("sound button", event) 
            
    def quit_game_button_klick(self, event):
        print("quit button")  

