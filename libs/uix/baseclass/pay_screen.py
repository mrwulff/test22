from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.app import App
from kivymd.uix.menu import MDDropdownMenu


class PaystubCard(MDCard):
    paystub_id = StringProperty("")
    pay_date = StringProperty("")
    period = StringProperty("")
    summary = StringProperty("")
    total = StringProperty("")


class PayScreen(Screen):

    def on_pre_enter(self):
        self.load_paystubs()

    def load_paystubs(self):
        app = App.get_running_app()
        db = app.db

        show_money = (
            str(
                db.get_user_setting(
                    "show_pay_amounts",
                    "True",
                )
            ).lower()
            == "true"
        )

        self.show_money = show_money

        self.paystub_rows = db.get_paystubs()

        self._display_paystubs(self.paystub_rows)


    def _display_paystubs(self, rows):
        self.ids.paystub_list.data = [
            {
                "paystub_id": str(row["id"]),
                "pay_date": str(row["pay_date"] or ""),
                "period": (
                    f"{row['pay_period_start']} – "
                    f"{row['pay_period_end']}"
                ),
                "summary": (
                    f"{row['item_count']} entries · "
                    f"{float(row['reg_hours'] or 0) + float(row['ot_hours'] or 0) + float(row['dt_hours'] or 0):.1f} hrs"
                ),
                "total": (
                    f"${float(row['payroll_total'] or 0):,.2f}"
                    if self.show_money
                    else "••••••"
                ),
            }
            for row in rows
        ]
    def import_paystub(self):
        print("[PAY] Import paystub pressed")

    def show_sort_menu(self, caller):
        items = [
            {
                "text": "Date",
                "on_release": lambda: self.sort_paystubs("date"),
            },
            {
                "text": "Pay",
                "on_release": lambda: self.sort_paystubs("pay"),
            },
            {
                "text": "Hours",
                "on_release": lambda: self.sort_paystubs("hours"),
            },
        ]

        self.sort_menu = MDDropdownMenu(
            caller=caller,
            items=items,
        )

        self.sort_menu.open()


    def sort_paystubs(self, sort_by):
        if hasattr(self, "sort_menu"):
            self.sort_menu.dismiss()

        if not hasattr(self, "paystub_rows"):
            return

        rows = list(self.paystub_rows)

        if sort_by == "date":
            rows.sort(
                key=lambda row: str(
                    row.get("pay_date") or ""
                ),
                reverse=True,
            )

        elif sort_by == "pay":
            rows.sort(
                key=lambda row: float(
                    row.get("payroll_total") or 0
                ),
                reverse=True,
            )

        elif sort_by == "hours":
            rows.sort(
                key=lambda row: (
                    float(row.get("reg_hours") or 0)
                    + float(row.get("ot_hours") or 0)
                    + float(row.get("dt_hours") or 0)
                ),
                reverse=True,
            )

        self._display_paystubs(rows)