import arcade
import arcade.gui
import main
import soundoptions
import generaloptions


class UserInterface:
    '''Class for option mennue accessed by "ESCAPE"'''

    def __init__(self):
        self.points: int = 0
        # self.uimanager = arcade.gui.UIManager()
        self.points = 10

        self.sound_options = soundoptions.SoundOptions()
        self.general_options = generaloptions.GeneralOptions()
        main.GAME_MANAGER.current_options = self.general_options

        # self.general_options.sound_options = main.GAME_MANAGER.UI_sound[
        #     0
        # ]  # Evil pointer hack

    def recive_key_down(self, key):
        # if escape iif pressed and options are openn sett all options to false
        if key == arcade.key.ESCAPE:
            if main.GAME_MANAGER.open_options:
                main.GAME_MANAGER.open_options = False
                main.GAME_MANAGER.current_options.disable()
            else:
                # if no optiosn open and press scape start standard optionns
                main.GAME_MANAGER.open_options = True
                main.GAME_MANAGER.current_options = self.general_options
                main.GAME_MANAGER.current_options.option_buttons()

    def update_score(self):
        self.points = int(main.GAME_MANAGER.score)

    # def draw_self(self):
    #     arcade.draw_text(
    #         self.points,
    #         main.SCREEN_WIDTH / 32,
    #         main.SCREEN_HEIGHT / 1.10,
    #         #gamemanager.GameManager.UI_general.uimanager.enable(),
    #     )

    def draw_self(self):
        # socriing
        arcade.draw_text(
            self.points,
            main.SCREEN_WIDTH / 5,
            main.SCREEN_HEIGHT / 1.17,
            arcade.color.BABY_BLUE,
            40,
            40,
        )  # anchor_x="right", anchor_y="top" to channge to top right cornner
        # draw the buttons for diferennt options
        if main.GAME_MANAGER.open_options:
            main.GAME_MANAGER.current_options.draw_self()

    # def option_buttons(self):
    #     self.uimanager.enable()
    #     resume_game_button = arcade.gui.UIFlatButton(text="Resume Game", width=200)
    #     self.uimanager.add(
    #         arcade.gui.UIAnchorWidget(
    #             anchor_x="center_x",
    #             anchor_y="center_y",
    #             align_y=+200,
    #             child=resume_game_button,
    #         )
    #     )
    #     resume_game_button.on_click = self.resume_game_button_klick
    #     self.uimanager.enable()
    #     new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
    #     self.uimanager.add(
    #         arcade.gui.UIAnchorWidget(
    #             anchor_x="center_x",
    #             anchor_y="center_y",
    #             align_y=+100,
    #             child=new_game_button,
    #         )
    #     )
    #     new_game_button.on_click = self.new_game_button_klick
    #     sound_button = arcade.gui.UIFlatButton(text="Sound", width=200)
    #     self.uimanager.add(
    #         arcade.gui.UIAnchorWidget(
    #             anchor_x="center_x", anchor_y="center_y", align_y=0, child=sound_button
    #         )
    #     )
    #     sound_button.on_click = self.sound_button_klick
    #     quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
    #     self.uimanager.add(
    #         arcade.gui.UIAnchorWidget(
    #             anchor_x="center_x",
    #             anchor_y="center_y",
    #             align_y=-100,
    #             child=quit_button,
    #         )
    #     )
    #     quit_button.on_click = self.quit_game_button_klick

    # def resume_game_button_klick(self, event):
    #     print("resume button", event)

    # def new_game_button_klick(self, event):
    #     print("new game button", event)

    # def sound_button_klick(self, event):
    #     print("sound button", event)

    # def quit_game_button_klick(self, event):
    #     print("quit button")

    #     if self.sound_options.open_sound:
    #         self.sound_options.draw_self()
    #     else:
    #         self.general_options.draw_self()
