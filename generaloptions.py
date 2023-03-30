import arcade
import arcade.gui
import main
import userinterface
import soundoptions
import sfxoptions


class GeneralOptions:
    '''Class for option mennue accessed by "SPACE"'''

    def __init__(self, sfx_player, music_player,window_class):
        self.open_options = False
        self.uimanager = arcade.gui.UIManager()
        self.option_buttons()
        self.music_player = music_player
        self.window_class = window_class
        self.new_game = False
        self.sfx_player = sfx_player

    def option_buttons(self):
        # self.uimanager.enable()
        resume_game_button = arcade.gui.UIFlatButton(text="Resume Game", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=resume_game_button,
            )
        )
        resume_game_button.on_click = self.resume_game_button_click

        new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=new_game_button,
            )
        )
        new_game_button.on_click = self.new_game_button_click

        music_button = arcade.gui.UIFlatButton(text="Music", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", 
                anchor_y="center_y", 
                align_y=0, 
                child=music_button
            )
        )
        music_button.on_click = self.music_button_click

        sound_button = arcade.gui.UIFlatButton(text="Sound", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", 
                anchor_y="center_y", 
                align_y=-100, 
                child=sound_button
            )
        )
        sound_button.on_click = self.sound_button_click

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-200,
                child=quit_button,
            )
        )
        quit_button.on_click = self.quit_game_button_click

    def enable(self):
        self.uimanager.enable()
    def disable(self):
        self.uimanager.disable()

    def draw_self(self):
        self.uimanager.enable()
        return self.uimanager.draw()

    def resume_game_button_click(self, event):
        self.uimanager.disable()
        self.window_class.pause = False
        main.GAME_MANAGER.open_options = False

    def new_game_button_click(self, event):
        if not self.new_game:
            self.new_game = True
            main.GAME_MANAGER.open_options = False
            main.GAME_MANAGER.score = 0
            self.music_player.stop()
            self.window_class.setup()

    def music_button_click(self, event):
        main.GAME_MANAGER.current_options = soundoptions.SoundOptions(self.sfx_player, self.music_player, self.window_class)
        self.uimanager.disable()

    def sound_button_click(self, event):
        main.GAME_MANAGER.current_options = sfxoptions.SfxOptions(self.sfx_player, self.music_player, self.window_class)
        self.uimanager.disable()

    def quit_game_button_click(self, event):
        arcade.exit()
