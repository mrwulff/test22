from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.logger import Logger
from kivymd.uix.card import MDCard


class TodayScreen(Screen):

    def on_enter(self, *args):
        Logger.info("TODAY: on_enter")

    def on_pre_enter(self, *args):
        Logger.info("TODAY: on_pre_enter")

    def on_kv_post(self, *args):
        Logger.info("TODAY: on_kv_post")
class LoginCard(MDCard):
    pass
