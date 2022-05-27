from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pygame

class Main(BoxLayout):
    click = None
    value = 130
    pygame.init()
    metronome_on = False

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.on_slider_value(self)

    def on_slider_value(self, widget):
        self.value = widget.value
        if self.metronome_on is True:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f"sounds/{self.value}.ogg")
            pygame.mixer.music.play()

    def change_icon(self, widget):
        if widget.text == '▶️':
            widget.text = '⏸️'
            self.metronome_on = True
            self.on_slider_value(self)
        else:
            widget.text = '▶️'
            self.metronome_on = False
            self.stop_metronome()

    def start_metronome(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(f"sounds/{self.on_slider_value(self)}.ogg")
        pygame.mixer.music.play()

    def stop_metronome(self):
        pygame.mixer.music.stop()

class Metronome(App):
    pass

if __name__ == '__main__':
    Metronome().run()

