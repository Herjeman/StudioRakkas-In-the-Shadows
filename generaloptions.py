import arcade
import arcade.gui
import main
import userinterface

class GeneralOptions():
    ''' Class for option mennue accessed by "SPACE"'''
    def __init__(self):
        self.open_options = False
        self.uimanager = arcade.gui.UIManager()
        self.sound_options = None
        self.option_buttons()

    def option_buttons(self):
        #self.uimanager.enable()
        resume_game_button = arcade.gui.UIFlatButton(text="Resume Game",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=resume_game_button)
        )
        resume_game_button.on_click = self.resume_game_button_click
        new_game_button = arcade.gui.UIFlatButton(text="New Game",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=new_game_button)
        )
        new_game_button.on_click = self.new_game_button_click
        sound_button = arcade.gui.UIFlatButton(text="Sound",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=sound_button)
        )
        sound_button.on_click = self.sound_button_click
        quit_button = arcade.gui.UIFlatButton(text="Quit",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-100,
                child=quit_button)
        )
        quit_button.on_click = self.quit_game_button_click

    def draw_self(self):
        return self.uimanager.draw()


    def resume_game_button_click(self, event):
        print("resume button", event)
        
        
    def new_game_button_click(self, event):
        print("new game button", event) 

    def sound_button_click(self, event):
        self.sound_options.open_sound = True
        self.uimanager.disable()
        self.sound_options.uimanager.enable()
            
            
    def quit_game_button_click(self, event):
        print("quit button")  


