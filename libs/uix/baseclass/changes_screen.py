from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard

from libs.lib_rhino_db import RhinoDatabase


from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.card import MDCard
from datetime import datetime


class ChangeCard(MDCard):

    show_name = StringProperty("")
    change_type = StringProperty("")
    field = StringProperty("")
    old_value = StringProperty("")
    new_value = StringProperty("")
    timestamp = StringProperty("")

    badge = StringProperty("")
    badge_color = ColorProperty((0.4, 0.4, 0.4, 1))
    change_badge = StringProperty("")

    show_name = StringProperty("")
    show_date = StringProperty("")
    show_time = StringProperty("")


class ChangesScreen(Screen):

    def get_badge(self, change_type):

        change = (change_type or "").lower().strip()

        if change == "new":
            return "NEW", (0.20, 0.65, 0.30, 1)

        if change == "modified":
            return "MODIFIED", (0.90, 0.65, 0.10, 1)

        if change in ("canceled", "cancelled"):
            return "CANCELED", (0.85, 0.20, 0.20, 1)

        return change.upper() or "?", (0.40, 0.40, 0.40, 1)

    def on_pre_enter(self):

        print("ChangesScreen ENTER")

        db = RhinoDatabase()
        changes = db.get_changes(100)

        data = []

        for change in changes:

            change_type = change["change_type"] or ""

            badge, badge_color = self.get_badge(change_type)
            change_badge = (change["field"] or "").upper()

            # Format timestamp
            timestamp = change["timestamp"] or ""

            try:
                dt = datetime.fromisoformat(timestamp)
                timestamp = f"{dt:%b} {dt.day}, {dt:%Y} {dt:%I:%M %p}"
            except (ValueError, TypeError):
                pass

            data.append({
                "timestamp": timestamp,

                "change_type": change_type,
                "field": change["field"] or "",
                "old_value": change["old_value"] or "",
                "new_value": change["new_value"] or "",

                "show_name": change["show"] or "Unknown Show",
                "venue": change["venue"] or "",
                "show_date": change["date"] or "",
                "show_time": change["time"] or "",

                "badge": badge,
                "badge_color": badge_color,
                "change_badge": change_badge,
            })

        self.ids.changes_rv.data = data

        db.close()