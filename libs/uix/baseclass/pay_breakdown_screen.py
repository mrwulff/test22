from datetime import datetime

from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard


class PaystubShiftCard(MDCard):
    shift_date = StringProperty("")
    shift_time = StringProperty("")
    payroll_item_id = StringProperty("")
    show_name = StringProperty("")
    hours = StringProperty("")
    pay = StringProperty("")


class PaystubBreakdownScreen(Screen):

    paystub_id = StringProperty("")
    pay_date = StringProperty("")
    period = StringProperty("")

    reg_hours = StringProperty("0.0 hrs")
    ot_hours = StringProperty("0.0 hrs")
    dt_hours = StringProperty("0.0 hrs")
    weekly_ot_hours = StringProperty("0.0 hrs")
    meal_penalty_hours = StringProperty("0.0 hrs")
    rest_break_penalty_hours = StringProperty("0.0 hrs")

    total_hours = StringProperty("0.0 hrs")
    total_pay = StringProperty("$0.00")

    summary_height = NumericProperty(68)

    def on_pre_enter(self):
        print("[PAY BREAKDOWN] on_pre_enter")
        print("[PAY BREAKDOWN] paystub_id =", self.paystub_id)

        self.load_paystub()

    def load_paystub(self):
        app = App.get_running_app()

        print("[PAY BREAKDOWN] load_paystub")
        print("[PAY BREAKDOWN] app.db =", app.db)

        if not self.paystub_id:
            return

        rows = app.db.get_paystubs()

        paystub = None

        for row in rows:
            if str(row["id"]) == str(self.paystub_id):
                paystub = row
                break

        if paystub is None:
            print(
                "[PAY BREAKDOWN] ERROR: "
                f"Could not find paystub {self.paystub_id}"
            )
            return

        self.pay_date = str(
            paystub["pay_date"] or ""
        )

        self.period = (
            f"{paystub['pay_period_start']} – "
            f"{paystub['pay_period_end']}"
        )

        reg = float(
            paystub["reg_hours"] or 0
        )

        ot = float(
            paystub["ot_hours"] or 0
        )

        dt = float(
            paystub["dt_hours"] or 0
        )

        weekly_ot = float(
            paystub["weekly_ot_hours"] or 0
        )

        meal = float(
            paystub["meal_penalty_hours"] or 0
        )

        rest = float(
            paystub["rest_break_penalty_hours"] or 0
        )

        total_hours = reg + ot + dt

        self.reg_hours = f"{reg:.1f} hrs"
        self.ot_hours = f"{ot:.1f} hrs"
        self.dt_hours = f"{dt:.1f} hrs"
        self.weekly_ot_hours = f"{weekly_ot:.1f} hrs"
        self.meal_penalty_hours = f"{meal:.1f} hrs"
        self.rest_break_penalty_hours = f"{rest:.1f} hrs"

        self.total_hours = f"{total_hours:.1f} hrs"

        show_money = (
            str(
                app.db.get_user_setting(
                    "show_pay_amounts",
                    "True",
                )
            ).lower()
            == "true"
        )

        if show_money:
            self.total_pay = (
                f"${float(paystub['payroll_total'] or 0):,.2f}"
            )
        else:
            self.total_pay = "••••••"

        self.build_summary()
        self.load_shifts(paystub)

    # ---------------------------------------------------------
    # PAY SUMMARY
    # ---------------------------------------------------------

    def build_summary(self):
        """
        Create only the summary rows that actually contain
        non-zero values.
        """

        container = self.ids.summary_container

        container.clear_widgets()

        rows = [
            ("Regular", self.reg_hours),
            ("Overtime", self.ot_hours),
            ("Double Time", self.dt_hours),
            ("Weekly OT", self.weekly_ot_hours),
            ("Meal Penalty", self.meal_penalty_hours),
            ("Rest Break", self.rest_break_penalty_hours),
        ]

        visible_rows = []

        for label, value in rows:

            if label != "Regular" and value == "0.0 hrs":
                continue

            visible_rows.append(
                (label, value)
            )

        for label, value in visible_rows:

            row = self.create_summary_row(
                label,
                value,
            )

            container.add_widget(row)

        # Padding + row heights.
        #
        # Each row is 36dp.
        # Top/bottom padding is 16dp each.
        self.summary_height = (
            32 + (len(visible_rows) * 36)
        )

    def create_summary_row(self, label, value):
        """
        Create one payroll summary row.
        """

        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.label import MDLabel

        row = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=36,
        )

        label_widget = MDLabel(
            text=label,
            font_size=16,
        )

        value_widget = MDLabel(
            text=value,
            font_size=16,
            halign="right",
            text_size=(None, None),
        )

        row.add_widget(label_widget)
        row.add_widget(value_widget)

        return row

    # ---------------------------------------------------------
    # SHIFTS
    # ---------------------------------------------------------

    def load_shifts(self, paystub):
        rows = self._get_payroll_items(
            paystub["paystub_key"]
        )

        container = self.ids.shift_container

        container.clear_widgets()

        for row in rows:

          card = PaystubShiftCard(
              payroll_item_id=str(row["id"]),
              show_name=str(row["show"] or "Unknown Show"),
              shift_date=self._format_shift_date(row["time_in"]),
              shift_time=self._format_shift_time(
                  row["time_in"],
                  row["time_out"],
              ),
              hours=self._format_hours(row),
              pay=self._format_pay(row),
          )

          container.add_widget(card)
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





    def _get_payroll_items(self, paystub_key):

        app = App.get_running_app()

        rows = app.db.db.execute(
            """
            SELECT *
            FROM payroll_items
            WHERE paystub_id = ?
            ORDER BY time_in ASC
            """,
            (paystub_key,),
        ).fetchall()

        return rows

    # ---------------------------------------------------------
    # FORMATTING
    # ---------------------------------------------------------

    def _format_shift_date(self, value):

        if not value:
            return ""

        try:
            dt = datetime.strptime(
                value,
                "%m/%d/%Y %I:%M:%S %p",
            )

            return dt.strftime(
                "%b %-d · %-I:%M %p"
            )

        except ValueError:
            return str(value)

    def _format_hours(self, row):

      reg = float(row["reg_hours"] or 0)
      ot = float(row["ot_hours"] or 0)
      dt = float(row["dt_hours"] or 0)
      weekly_ot = float(row["weekly_ot_hours"] or 0)

      parts = []

      if reg:
          parts.append(f"{reg:g} REG")

      if ot:
          parts.append(f"{ot:g} OT")

      if dt:
          parts.append(f"{dt:g} DT")

      if weekly_ot:
          parts.append(f"{weekly_ot:g} WEEKLY OT")

      if not parts:
          return "No hours"

      return " · ".join(parts)

    def _format_pay(self, row):

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

        return (
            f"${float(row['pay'] or 0):,.2f}"
        )

    # ---------------------------------------------------------
    # NAVIGATION
    # ---------------------------------------------------------

    def go_back(self):

        app = App.get_running_app()

        if hasattr(app, "change_screen"):
            app.change_screen(
                "pay",
                "left",
            )
        else:
            self.manager.current = "pay"


# Existing lazy-loader expects this name.
pay_breakdownscreen = PaystubBreakdownScreen