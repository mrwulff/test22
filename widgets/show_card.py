from kivy.properties import (
    StringProperty,
    ColorProperty,
)

from kivymd.uix.card import MDCard
CLASS_COLORS = {
    "IN": (0.22, 0.72, 0.43, 1),
    "SHOW": (0.18, 0.45, 0.93, 1),
    "OUT": (0.95, 0.58, 0.12, 1),
}

POSITION_COLORS = {
    "L3": (0.22,0.72,0.43,1),
    "A1": (0.18,0.45,0.93,1),
    "FOH": (0.42,0.32,0.86,1),
    "PM": (.35,.35,.35,1),
    "C": (0.90,0.55,0.10,1),
}

class ShowCard(MDCard):
    badge = StringProperty("IN")
    badge_color = ColorProperty((0.25, 0.75, 0.45, 1))

    position = StringProperty("L3")
    position_color = ColorProperty((0.25, 0.75, 0.45, 1))

    day = StringProperty("Thu")
    date = StringProperty("Jun 18")
    time = StringProperty("7:00 PM")

    show = StringProperty("ACMA Awards")
    venue = StringProperty("MGM Grand Garden Arena")
    address = StringProperty("3799 S Las Vegas Blvd")

    stripe_color = ColorProperty((0.25, 0.75, 0.45, 1))

    show_class = StringProperty("IN")
    position = StringProperty("L3")