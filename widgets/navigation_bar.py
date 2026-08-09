from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout


class NavigationBar(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("NavigationBar created")

    def goto(self, screen):

        App.get_running_app().root.push(screen)