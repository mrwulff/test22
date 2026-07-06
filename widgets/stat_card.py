from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.card import MDCard
print("loading stat_card")


class StatCard(MDCard):
    print("loading stat_card2")
    icon = StringProperty("calendar-check")

    value = StringProperty("11")
    title = StringProperty("CONFIRMED")
    subtitle = StringProperty("Next in 7 days")

    icon_color = ColorProperty((1, 1, 1, 1))
    circle_color = ColorProperty((1, 1, 1, .12))