from datetime import datetime

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class PaystubItemScreen(Screen):
    payroll_item_id = StringProperty("")

    show_name = StringProperty("")
    job_number = StringProperty("")
    position = StringProperty("")
    client = StringProperty("")

    shift_date = StringProperty("")
    shift_time = StringProperty("")

    reg_hours = StringProperty("")
    ot_hours = StringProperty("")
    dt_hours = StringProperty("")
    weekly_ot_hours = StringProperty("")
    meal_penalty_hours = StringProperty("")
    rest_break_penalty_hours = StringProperty("")

    base_rate = StringProperty("")
    blended_rate = StringProperty("")
    total_pay = StringProperty("")

    schedule_status = StringProperty("")
    schedule_date = StringProperty("")
    schedule_time = StringProperty("")
    schedule_job = StringProperty("")
    schedule_position = StringProperty("")

    def on_pre_enter(self):
        print("[PAY ITEM] on_pre_enter")
        print("[PAY ITEM] payroll_item_id =", self.payroll_item_id)

        self.load_item()

    def load_item(self):
        app = App.get_running_app()

        print("[PAY ITEM] load_item")
        print("[PAY ITEM] app.db =", app.db)

        if not self.payroll_item_id:
            print("[PAY ITEM] No payroll item ID")
            return

        row = app.db.db.execute(
            """
            SELECT *
            FROM payroll_items
            WHERE id = ?
            LIMIT 1
            """,
            (self.payroll_item_id,),
        ).fetchone()

        if row is None:
            print(
                "[PAY ITEM] Payroll item not found:",
                self.payroll_item_id,
            )
            return

        self.show_name = str(row["show"] or "Unknown Show")
        self.job_number = str(row["job_number"] or "")
        self.position = str(row["position"] or "")
        self.client = str(row["client"] or "")

        self.shift_date = self._format_date(row["time_in"])
        self.shift_time = self._format_shift_time(
            row["time_in"],
            row["time_out"],
        )

        self.reg_hours = self._format_hours(row["reg_hours"])
        self.ot_hours = self._format_hours(row["ot_hours"])
        self.dt_hours = self._format_hours(row["dt_hours"])
        self.weekly_ot_hours = self._format_hours(
            row["weekly_ot_hours"]
        )
        self.meal_penalty_hours = self._format_hours(
            row["meal_penalty_hours"]
        )
        self.rest_break_penalty_hours = self._format_hours(
            row["rest_break_penalty_hours"]
        )

        self.base_rate = self._format_money(
            row["base_rate"]
        )
        self.blended_rate = self._format_money(
            row["blended_rate"]
        )
        self.total_pay = self._format_pay(
            row["pay"]
        )

        self.load_schedule(row)

    def load_schedule(self, payroll_row):
        app = App.get_running_app()

        show_id = payroll_row["show_id"]

        if not show_id:
            self.schedule_status = "No Rhino schedule match"
            self.schedule_date = ""
            self.schedule_time = ""
            self.schedule_job = ""
            self.schedule_position = ""

            print("[PAY ITEM] No Rhino show linked")
            return

        show = app.db.db.execute(
            """
            SELECT *
            FROM shows
            WHERE id = ?
            LIMIT 1
            """,
            (show_id,),
        ).fetchone()

        if show is None:
            self.schedule_status = "Rhino schedule entry not found"
            return

        self.schedule_status = "Matched Rhino schedule"

        self.schedule_date = str(
            show["date"] or ""
        )

        self.schedule_job = str(
            show["job"] or ""
        )

        self.schedule_position = str(
            show["position"] or ""
        )

        # Try the common time fields without assuming
        # exactly which version of the shows schema is present.
        start = self._first_value(
            show,
            "time_in",
            "start_time",
            "start",
            "time",
        )

        end = self._first_value(
            show,
            "time_out",
            "end_time",
            "end",
        )

        if start and end:
            self.schedule_time = f"{start} – {end}"
        elif start:
            self.schedule_time = str(start)
        else:
            self.schedule_time = ""

        print("[PAY ITEM] Rhino show matched:", show_id)

    def _first_value(self, row, *names):
        for name in names:
            try:
                value = row[name]
            except (KeyError, IndexError):
                continue

            if value not in (None, ""):
                return value

        return ""

    def _format_date(self, value):
        if not value:
            return ""

        try:
            dt = datetime.strptime(
                value,
                "%m/%d/%Y %I:%M:%S %p",
            )

            return dt.strftime("%b %-d, %Y")

        except ValueError:
            return str(value)

    def _format_shift_time(self, time_in, time_out):
        if not time_in:
            return ""

        try:
            start = datetime.strptime(
                time_in,
                "%m/%d/%Y %I:%M:%S %p",
            )

            if not time_out:
                return start.strftime("%-I:%M %p")

            end = datetime.strptime(
                time_out,
                "%m/%d/%Y %I:%M:%S %p",
            )

            result = (
                f"{start.strftime('%-I:%M %p')} – "
                f"{end.strftime('%-I:%M %p')}"
            )

            if end.date() > start.date():
                result += " (+1 day)"

            return result

        except ValueError:
            return ""

    def _format_hours(self, value):
        if value in (None, ""):
            return "—"

        value = float(value)

        if value == 0:
            return "—"

        return f"{value:g} hrs"

    def _format_money(self, value):
        if value in (None, ""):
            return "—"

        value = float(value)

        if value == 0:
            return "—"

        return f"${value:,.2f}"

    def _format_pay(self, value):
        app = App.get_running_app()

        show_money = (
            str(
                app.db.get_user_setting(
                    "show_pay_amounts",
                    "True",
                )
            ).lower()
            == "true"
        )

        if not show_money:
            return "••••••"

        return f"${float(value or 0):,.2f}"

    def go_back(self):
        app = App.get_running_app()

        print("[PAY ITEM] Going back to pay breakdown")

        if hasattr(app, "change_screen"):
            app.change_screen(
                "pay_breakdown",
                "right",
            )
        else:
            self.manager.current = "pay_breakdown"


pay_itemscreen = PaystubItemScreen