import arcade
import arcade.gui
import main
import userinterface

class SoundOptions():
    ''' Class for option mennue accessed by "SPACE"'''
    def __init__(self):
        self.open_sound = False
        self.uimanager = arcade.gui.UIManager()
        self.volume_buttons()

    def volume_buttons(self):
        #self.uimanager.enable()
        valume_up_button = arcade.gui.UIFlatButton(text="Volume UP",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=valume_up_button)
        )
        valume_up_button.on_click = self.volume_up_click

        volume_down_button = arcade.gui.UIFlatButton(text="Volume DOWN",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=volume_down_button)
        )
        volume_down_button.on_click = self.volume_down_click

        volume_off_button = arcade.gui.UIFlatButton(text="Volume Off",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=volume_off_button)
        )
        volume_off_button.on_click = self.volume_off_click
        
        options_button = arcade.gui.UIFlatButton(text="Options",width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=options_button)
        )
        options_button.on_click = self.options_click

    def draw_self(self):
        return self.uimanager.draw()

    def volume_up_click(self, event):
        print("volume up", event)
    
    def volume_down_click(self, event):
        print("volume down", event) 

    def volume_off_click(self, event):
        print("volume off", event) 

    def options_click(self, event):
        print("options click")
        # self.general_options.open_options = True
        # self.uimanager.disable()
        # self.general_options.uimanager.enable()
