from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.widget import MDWidget


class Badge(MDWidget):
    text = StringProperty("SHOW")

    bg_color = ColorProperty((0.20, 0.55, 1.0, 1))
    fg_color = ColorProperty((1, 1, 1, 1))