from kivy.properties import (
    StringProperty,
    ColorProperty,
    BooleanProperty,
)
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ColorProperty


class NavButton(MDBoxLayout):

    icon = StringProperty("home")
    text = StringProperty("Home")

    active = BooleanProperty(False)

    icon_color = ColorProperty((1, 1, 1, 1))
    circle_color = ColorProperty((0, 0, 0, 0))
    

    active_color = ColorProperty((0.40, 0.55, 1, 1))