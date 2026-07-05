from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty


class AppShell(MDBoxLayout):

    screen_manager = ObjectProperty()

    def go(self, screen):
        if self.screen_manager:
            self.screen_manager.current = screen