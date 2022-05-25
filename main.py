from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider


class Main(BoxLayout):
    click = None
    value = 130

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.on_slider_value(self)

    def on_size(self, *args):
        print(self.width, self.height)

    def on_slider_value(self, widget):
        self.value = widget.value
        return self.value

    def change_icon(self, widget):
        if widget.text == '▶️':
            widget.text = '⏸️'
            self.start_metronome()
        else:
            widget.text = '▶️'
            self.stop_metronome()

    def start_metronome(self):
        print(self.on_slider_value(self))
        self.click = SoundLoader.load(f"sounds/{self.on_slider_value(self)}.ogg")
        self.click.volume = 1.5
        self.click.play()

    def stop_metronome(self):
        self.click.stop()
        self.click.unload()
        self.click = None

    def collide_point(self, x, y):
        return self.x <= x <= self.right and self.y+40 <= y <= self.top-40


class Metronome(App):
    pass

if __name__ == '__main__':
    Metronome().run()