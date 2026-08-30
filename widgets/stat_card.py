from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.card import MDCard
print("loading stat_card")


class StatCard(MDCard):
    print("loading stat_card2")
    icon = StringProperty("calendar-check")

    value = StringProperty("")
    title = StringProperty("")
    subtitle = StringProperty("")

    icon_color = ColorProperty((1, 1, 1, 1))
    circle_color = ColorProperty((1, 1, 1, .12))