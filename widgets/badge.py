from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout


class Badge(MDBoxLayout):
    text = StringProperty("")
    icon = StringProperty("")

    bg_color = ColorProperty((0.2, 0.55, 1.0, 1))
    fg_color = ColorProperty((1, 1, 1, 1))