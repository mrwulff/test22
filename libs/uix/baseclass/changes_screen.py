from datetime import datetime

from kivy.metrics import dp
from kivy.properties import (
    StringProperty,
    ColorProperty,
    NumericProperty,
)
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard

from libs.lib_rhino_db import RhinoDatabase


class PendingConfirmCard(MDCard):

    show_name = StringProperty("")
    show_date = StringProperty("")
    show_time = StringProperty("")
    confirm_id = StringProperty("")


class ChangeCard(MDCard):

    show_name = StringProperty("")
    show_date = StringProperty("")
    show_time = StringProperty("")

    change_type = StringProperty("")
    change_summary = StringProperty("")
    change_count = NumericProperty(1)

    timestamp = StringProperty("")

    badge = StringProperty("")
    badge_color = ColorProperty(
        (0.4, 0.4, 0.4, 1)
    )


class ChangesScreen(Screen):

    def get_badge(self, change_type):

        change = (change_type or "").lower().strip()

        if change == "new":
            return "NEW", (0.20, 0.65, 0.30, 1)

        if change == "modified":
            return "MODIFIED", (0.90, 0.65, 0.10, 1)

        if change in ("canceled", "cancelled"):
            return "CANCELED", (0.85, 0.20, 0.20, 1)

        if change == "removed":
            return "REMOVED", (0.40, 0.40, 0.40, 1)

        return (
            change.upper() or "?",
            (0.40, 0.40, 0.40, 1),
        )

    def format_timestamp(self, timestamp):

        if not timestamp:
            return ""

        try:
            dt = datetime.fromisoformat(timestamp)

            return (
                f"{dt:%b} {dt.day}, {dt:%Y} "
                f"{dt:%I:%M %p}"
            )

        except (ValueError, TypeError):
            return timestamp

    def format_field_value(self, value):

        if value is None or str(value).strip() == "":
            return "—"

        return str(value).strip()

    def on_pre_enter(self, *args):

        print("ChangesScreen ENTER")

        db = RhinoDatabase()

        try:
            self.load_pending_confirmations(db)
            self.load_schedule_changes(db)

        finally:
            db.close()

    def load_pending_confirmations(self, db):

        pending_list = self.ids.pending_list
        pending_list.clear_widgets()

        pending = db.get_pending_confirmations()

        print(
            "[CONFIRM] Pending confirmations:",
            len(pending),
        )

        # The section contains the heading/button and the list.
        # With no pending shows, both are hidden and take no space.
        if pending:
            self.ids.pending_header.height = dp(48)
            self.ids.pending_header.opacity = 1
            self.ids.pending_header.disabled = False
        else:
            self.ids.pending_header.height = 0
            self.ids.pending_header.opacity = 0
            self.ids.pending_header.disabled = True

        for show in pending:

            print(
                "[CONFIRM]",
                show["show"],
                show["date"],
                show["time"],
                show["confirm_id"],
            )

            card = PendingConfirmCard(
                show_name=show["show"] or "Unknown Show",
                show_date=show["date"] or "",
                show_time=show["time"] or "",
                confirm_id=show["confirm_id"] or "",
            )

            pending_list.add_widget(card)

    def load_schedule_changes(self, db):

        change_list = self.ids.change_list
        change_list.clear_widgets()

        changes = db.get_changes(100)

        print(
            "[CHANGES] Grouped change cards:",
            len(changes),
        )

        for change in changes:

            change_type = change["change_type"] or ""

            badge, badge_color = self.get_badge(
                change_type
            )

            field_lines = []

            for field_change in change.get("fields", []):

                field_name = (
                    field_change.get("field") or ""
                ).replace("_", " ").upper()

                old_value = self.format_field_value(
                    field_change.get("old_value")
                )

                new_value = self.format_field_value(
                    field_change.get("new_value")
                )

                field_lines.append(
                    f"{field_name}: {old_value}  →  {new_value}"
                )

            if not field_lines:

                if change_type.lower() == "new":
                    field_lines.append("Show added to schedule")

                elif change_type.lower() == "removed":
                    field_lines.append("Show removed from schedule")

                else:
                    field_lines.append("Schedule updated")

            summary = "\n".join(field_lines)

            timestamp = self.format_timestamp(
                change.get("timestamp")
            )

            card = ChangeCard(
                show_name=change.get("show") or "Unknown Show",
                show_date=change.get("date") or "",
                show_time=change.get("time") or "",
                change_type=change_type,
                change_summary=summary,
                change_count=max(1, len(field_lines)),
                timestamp=timestamp,
                badge=badge,
                badge_color=badge_color,
            )

            change_list.add_widget(card)