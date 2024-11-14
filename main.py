import kivy
import kivy.app
import kivy.uix.label
from kivy.utils import platform
class dtd_app(kivy.app.App):
    def build(self):
        return kivy.uix.label.Label(text="Hello World")
    
dtd_app().run()