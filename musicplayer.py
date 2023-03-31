import arcade
import os
import main

class MusicPlayer:
    def __init__(self, window_class):
        song_path = os.path.join("assets", "audio", "in_the_shadows_2.wav")
        disco_song_path = os.path.join("assets", "audio", "in_the_shadows_2.wav")
        self.normal_song = arcade.load_sound(song_path)
        self.disco_song = arcade.load_sound(disco_song_path)
        self.pan = 0.0
        self.loop = True
        self.speed = 1.0
        self.volume_change = 0.1
        self.volume = main.GAME_MANAGER.music_volume

        self.active_music_player = None
        if main.GAME_MANAGER.disco_mode:
            self.song = self.disco_song
        else:
            self.song = self.normal_song
        
    def play(self):
        self.active_music_player = arcade.play_sound(
            self.song, self.volume, self.pan, self.loop, self.speed
        )
        if main.GAME_MANAGER.play_music == False:
            self.active_music_player.pause()

    def start(self):
        self.active_music_player.play()
        

    def stop(self):
        self.active_music_player.pause()


    def volume_up(self):
        if main.GAME_MANAGER.music_volume < 1:
            main.GAME_MANAGER.music_volume += self.volume_change
            self.song.set_volume(main.GAME_MANAGER.music_volume, self.active_music_player)

    def volume_down(self):
        if main.GAME_MANAGER.music_volume >= self.volume_change:
            main.GAME_MANAGER.music_volume -= self.volume_change
            self.song.set_volume(main.GAME_MANAGER.music_volume, self.active_music_player)

    def disco_mode_song(self):
        if main.GAME_MANAGER.disco_mode:
            self.active_music_player.pause()
            self.song = self.disco_song
            self.play()
        else:
            self.active_music_player.pause()
            self.song = self.normal_song
            self.play()

