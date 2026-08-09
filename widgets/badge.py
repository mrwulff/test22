from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.card import MDCard




class Badge(MDCard):
    text = StringProperty("SHOW")

    bg_color = ColorProperty((0.2, 0.5, 1, 1))
    fg_color = ColorProperty((1, 1, 1, 1))
    bg_color = ColorProperty((0.2,0.5,1,1))
    fg_color = ColorProperty((1,.1,.1,.1))