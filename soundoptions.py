import arcade
import arcade.gui
import main
import userinterface
import generaloptions


class SoundOptions:
    '''Class for option mennue accessed by "SPACE"'''

    def __init__(self):
        self.open_sound = False
        self.uimanager = arcade.gui.UIManager()
        self.volume_buttons()
        print("Sound options object created")

    def volume_buttons(self):

        volume_off_button = arcade.gui.UIFlatButton(text="Volume Off", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=volume_off_button,
            )
        )
        volume_off_button.on_click = self.volume_off_click

        # self.uimanager.enable()
        valume_up_button = arcade.gui.UIFlatButton(text="Volume UP", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=valume_up_button,
            )
        )
        valume_up_button.on_click = self.volume_up_click

        volume_down_button = arcade.gui.UIFlatButton(text="Volume DOWN", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=volume_down_button,
            )
        )
        volume_down_button.on_click = self.volume_down_click

        options_button = arcade.gui.UIFlatButton(text="Options", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-100,
                child=options_button,
            )
        )
        options_button.on_click = self.options_click

    def draw_self(self):
        self.uimanager.enable()
        return self.uimanager.draw()

    
    def enable(self):
        self.uimanager.enable()
    def diable(self):
        self.uimanager.disable()

    def volume_off_click(self, event):
        print("volume off", event)

    def volume_up_click(self, event):
        print("volume up", event)

    def volume_down_click(self, event):
        print("volume down", event)

    def options_click(self, event):
        main.GAME_MANAGER.current_options = generaloptions.GeneralOptions()
        self.uimanager.disable()
