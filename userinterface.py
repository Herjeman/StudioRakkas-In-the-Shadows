import arcade
import arcade.gui
import main
import soundoptions
import generaloptions


class Options:
    '''Class for option mennue accessed by "ESCAPE"'''

    def __init__(self):
        self.open_options = False
        self.points: int = 0
        self.uimanager = arcade.gui.UIManager()
        self.points = 10

        self.sound_options = soundoptions.SoundOptions()
        self.general_options = generaloptions.GeneralOptions()

        main.GAME_MANAGER.UI_sound.append(self.sound_options)
        main.GAME_MANAGER.UI_general.append(self.general_options)

        self.general_options.sound_options = main.GAME_MANAGER.UI_sound[
            0
        ]  # Evil pointer hack

        self.open_options = False

        # arcade.draw_text()

    def recive_key_down(self, key):
        # iif escape iif pressed and options are openn sett all options to false
        if key == arcade.key.ESCAPE:
            if self.open_options:
                self.open_options = False
                self.general_options.uimanager.disable()
            else:
                # if no optiosn open and press scape start standard optionns
                self.open_options = True
                self.option_buttons()

    def update_score(self):
        self.points = int(main.GAME_MANAGER.score)

    def draw_self(self):
        arcade.draw_text(
            self.points,
            main.SCREEN_WIDTH / 32,
            main.SCREEN_HEIGHT / 1.10,
            self.general_options.uimanager.enable(),
        )

    def draw_self(self):
        # socriing
        arcade.draw_text(
            self.points,
            main.SCREEN_WIDTH / 32,
            main.SCREEN_HEIGHT / 1.10,
            arcade.color.BABY_BLUE,
            40,
            40,
        )  # anchor_x="right", anchor_y="top" to channge to top right cornner
        # draw the buttons for diferennt options
        if self.open_options:
            arcade.draw_rectangle_filled(
                main.SCREEN_WIDTH / 2,
                main.SCREEN_HEIGHT / 2,
                main.SCREEN_WIDTH / 2,
                main.SCREEN_HEIGHT / 1.25,
                arcade.color.RED,
            )
            self.uimanager.draw()

    def option_buttons(self):
        self.uimanager.enable()
        resume_game_button = arcade.gui.UIFlatButton(text="Resume Game", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+200,
                child=resume_game_button,
            )
        )
        resume_game_button.on_click = self.resume_game_button_klick
        self.uimanager.enable()
        new_game_button = arcade.gui.UIFlatButton(text="New Game", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=+100,
                child=new_game_button,
            )
        )
        new_game_button.on_click = self.new_game_button_klick
        sound_button = arcade.gui.UIFlatButton(text="Sound", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", align_y=0, child=sound_button
            )
        )
        sound_button.on_click = self.sound_button_klick
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=-100,
                child=quit_button,
            )
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

        if self.sound_options.open_sound:
            self.sound_options.draw_self()
        else:
            self.general_options.draw_self()
