import arcade
import arcade.gui
import main
import userinterface
import generaloptions


class SfxOptions:
    '''Class for option mennue accessed by "SPACE"'''

    def __init__(self, sfx_player, music_player, window_class):
        self.sound_on = main.GAME_MANAGER.play_sound
        self.open_sound = False
        self.uimanager = arcade.gui.UIManager()
        self.volume_buttons()
        self.music_player = music_player
        self.window_class = window_class
        self.sfx_player = sfx_player


    def volume_buttons(self):
        if self.sound_on:
            text = "Sound OFF"
            click_funcntion = self.volume_off_click
        else:
            text = "Sound ON"
            click_funcntion = self.volume_on_click
        
        volume_off_button = arcade.gui.UIFlatButton(text=text, width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=volume_off_button,
            )
        )
        volume_off_button.on_click = click_funcntion
        

        # self.uimanager.enable()
        valume_up_button = arcade.gui.UIFlatButton(text="Sound UP", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=valume_up_button,
            )
        )
        valume_up_button.on_click = self.volume_up_click

        volume_down_button = arcade.gui.UIFlatButton(text="Sound DOWN", width=200)
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
    def disable(self):
        self.uimanager.disable()


    # different buttons
    def volume_on_click(self, event):
        self.sfx_player.sound_enabled()
        self.sfx_player.play_button_sound()
        self.sound_on = True
        self.volume_buttons()
        main.GAME_MANAGER.play_sound = True


    def volume_off_click(self, event):
        self.sfx_player.play_button_sound()
        self.sfx_player.sound_disabled()
        self.sound_on = False
        self.volume_buttons()
        main.GAME_MANAGER.play_sound = False

        # self.uimanager.remove(child=volume_off_button)

    def volume_up_click(self, event):
        self.sfx_player.play_button_sound()
        self.sfx_player.volume_up()

    def volume_down_click(self, event):
        self.sfx_player.play_button_sound()
        self.sfx_player.volume_down()

    # disables uimannager for sound options
    def options_click(self, event):
        self.sfx_player.play_button_sound()
        main.GAME_MANAGER.current_options = generaloptions.GeneralOptions(self.sfx_player, self.music_player, self.window_class)
        self.uimanager.disable()
