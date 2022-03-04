
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainApp(App):

    def animate_button(self, instance):
        anim = Animation(size_hint=(1, 1), t="out_bounce", duration=2) + Animation(size_hint=(0.8, 0.2),
                                                                                   t="out_bounce", duration=1)
        anim.start(instance)

    def frog_tapped(self, instance):
        self.animate_button(instance)

        burpsound = SoundLoader.load('Burp-Sound-effect.wav')
        burpsound.play()

        fartsound = SoundLoader.load('Fart-sound-effect.wav')
        Clock.schedule_once(lambda x: fartsound.play(), 2)



    def build(self):
        main_layout = BoxLayout(orientation="vertical", spacing=10, minimum_height=0.2)
        Window.clearcolor = (0.454901961, 0.819607843, 0.352941176, 1)

        filler_space1 = Label(text='', size_hint=(1, 0.1),
                              pos_hint={"center_x": 0.5, "center_y": 0.5})

        txt_noiseinput = TextInput(text="",
                                   size_hint=(1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0},
                                   halign="center", font_name="frog-font.ttf",
                                   font_size=45, hint_text="bericht: plplpplplplplp?"
                                   )

        txt_nameinput = TextInput(text="", size_hint=(1, 0.05), pos_hint={"center_x": 0.5, "center_y": 0.5},
                                  halign="center", font_name="frog-font.ttf", hint_text="Zender?",
                                  font_size=25)

        button = Button(text="", pos_hint={"center_x": 0.5, "center_y": 0.5},
                        size_hint=(0.8, 0.2),
                        background_normal="DiVaFrOg.png",
                        on_press=self.frog_tapped,
                        background_down="DiVaFrOg.png")
        # Builder.load_file("main.kv")

        main_layout.add_widget(txt_nameinput)
        main_layout.add_widget(txt_noiseinput)
        main_layout.add_widget(filler_space1)
        main_layout.add_widget(button)
        return main_layout


if __name__ == "__main__":
    app = MainApp()
    app.run()
