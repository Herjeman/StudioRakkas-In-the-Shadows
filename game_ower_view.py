import arcade
import main
class GameOverView():
    def __init__(self, music_player, game_window):
        super().__init__()
        self.time_taken = 0
        self.window_class = game_window
        self.uimanager = arcade.gui.UIManager()
        self.game_over_buttons()
        self.music_player = music_player
        self.restart = False


    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def draw_self(self):
        """
        Draw "Game over" across the screen.
        """
        # arcade.draw_text("Game Over", main.SCREEN_WIDTH/2-20, main.SCREEN_HEIGHT/2-20, arcade.color.WHITE, 40)

        arcade.draw_text("Game Over",main.SCREEN_WIDTH/2, 
                         main.SCREEN_HEIGHT/2+100,arcade.color.RED_DEVIL,40,anchor_x="center",anchor_y="center")
        self.uimanager.draw()
        self.uimanager.enable()

    def game_over_buttons(self):
        restart_game_button = arcade.gui.UIFlatButton(text="Restart Game", width=200)
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                align_y=0,
                child=restart_game_button,
            )
        )
        restart_game_button.on_click = self.restart_game_click

    def restart_game_click(self, event):
        if not self.restart:
            self.window_class.sfx_player.stop_all_sfx()
            self.window_class.setup()
            self.music_player.stop()
            main.GAME_MANAGER.score = 0
            self.restart = True
