from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.properties import ColorProperty


class ShowCard(MDCard):

    show = StringProperty()

    day = StringProperty()
    date = StringProperty()
    time = StringProperty()

    venue = StringProperty()
    address = StringProperty()

    position = StringProperty("")
    show_class = StringProperty("")
    status = StringProperty("")
    venue_code = StringProperty("")
    status_icon = StringProperty("")   # <-- add this
    hours = StringProperty("")
    pay = StringProperty("")



    

    class_color = ColorProperty((0.18, 0.55, 0.92, 1))
    status_color = ColorProperty((0.20, 0.72, 0.35, 1))
    position_color = ColorProperty((0.58, 0.42, 0.95, 1))
    venue_color = ColorProperty((0.60, 0.38, 0.90, 1))