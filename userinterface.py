import arcade
import arcade.gui
import main
import soundoptions
import generaloptions


class UserInterface():
    '''Class for option mennue accessed by "ESCAPE"'''

    def __init__(self, sfx_player, music_player, window_class):
        self.points: int = 0
        # self.uimanager = arcade.gui.UIManager()
        self.points = 10
        #self.sound_options = soundoptions.SoundOptions(music_player)
        self.window_class = window_class
        self.sfx_player = sfx_player
        self.general_options = generaloptions.GeneralOptions(self.sfx_player, music_player, self.window_class)
        main.GAME_MANAGER.current_options = self.general_options



    def recive_key_down(self, key):
        # if escape iif pressed and options are openn sett all options to false
        if key == arcade.key.ESCAPE: 
            if main.GAME_MANAGER.open_options:
                self.window_class.pause = False
                main.GAME_MANAGER.open_options = False
                main.GAME_MANAGER.current_options.disable()

            else:
                # if no optiosn open and press scape start standard optionns
                self.window_class.pause = True
                main.GAME_MANAGER.open_options = True
                main.GAME_MANAGER.current_options = self.general_options
                main.GAME_MANAGER.current_options.option_buttons()

    def update_score(self):
        self.points = int(main.GAME_MANAGER.score)

    def draw_self(self):
        # socriing
        arcade.draw_text(
            self.points,
            main.SCREEN_WIDTH / 22,
            main.SCREEN_HEIGHT / 1.1,
            arcade.color.BABY_BLUE,
            40,
            40,
        )  # anchor_x="right", anchor_y="top" to channge to top right cornner
        # draw the buttons for diferennt options
        if main.GAME_MANAGER.open_options:
            main.GAME_MANAGER.current_options.draw_self()
