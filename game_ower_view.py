import arcade
import main
class GameOverView():
    def __init__(self, game_window):
        super().__init__()
        self.time_taken = 0
        self.game_window = game_window

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def draw_self(self):
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)
        output_total = f"Total Score: {round(main.GAME_MANAGER.score)}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)


