from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivy.app import App
#from kivymd.uix.menu import MDDropdownMenu


class PaystubCard(MDCard):
    paystub_id = StringProperty("")
    pay_date = StringProperty("")
    period = StringProperty("")
    summary = StringProperty("")
    total = StringProperty("")


class PayScreen(Screen):
    sort_by = StringProperty("date")
    sort_reverse = True

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

        self.ids.paystub_list.data = []

        data = []

        for row in rows:

            total_hours = (
                float(row["reg_hours"] or 0)
                + float(row["ot_hours"] or 0)
                + float(row["dt_hours"] or 0)
                + float(row["weekly_ot_hours"] or 0)
                + float(row["meal_penalty_hours"] or 0)
                + float(row["rest_break_penalty_hours"] or 0)
            )

            data.append(
                {
                    "paystub_id": str(row["id"]),
                    "pay_date": str(row["pay_date"] or ""),
                    "period": (
                        f"{row['pay_period_start']} – "
                        f"{row['pay_period_end']}"
                    ),
                    "summary": (
                        f"{row['item_count']} shifts · "
                        f"{row['show_count']} shows · "
                        f"{total_hours:.1f} hrs"
                    ),
                    "total": (
                        f"${float(row['payroll_total'] or 0):,.2f}"
                        if self.show_money
                        else "••••••"
                    ),
                }
            )

        self.ids.paystub_list.data = data
    def import_paystubs(self):
        app = App.get_running_app()

        print("[PAY SCREEN] Downloading new paystubs")

        try:
            app.dlpp()

            # Reload the list from SQLite.
            self.load_paystubs()

            print("[PAY SCREEN] Paystub list refreshed")

        except Exception as exc:
            print(
                "[PAY SCREEN] Paystub import failed:",
                exc,
            )

    def show_sort_menu(self, caller):
        self.sort_panel_open = not getattr(
            self,
            "sort_panel_open",
            False,
        )

        self.ids.sort_panel.opacity = (
            1 if self.sort_panel_open else 0
        )

        self.ids.sort_panel.disabled = not self.sort_panel_open

    def sort_paystubs(self, sort_by):

        if hasattr(self, "sort_menu"):
            self.sort_menu.dismiss()

        # Same sort = reverse direction.
        if sort_by == self.sort_by:
            self.sort_reverse = not self.sort_reverse

        # New sort = start descending.
        else:
            self.sort_by = sort_by
            self.sort_reverse = True

        if not hasattr(self, "paystub_rows"):
            return

        rows = list(self.paystub_rows)

        if sort_by == "date":

            rows.sort(
                key=lambda row: str(
                    row.get("pay_date") or ""
                ),
                reverse=self.sort_reverse,
            )

        elif sort_by == "pay":

            rows.sort(
                key=lambda row: float(
                    row.get("payroll_total") or 0
                ),
                reverse=self.sort_reverse,
            )

        elif sort_by == "hours":

            rows.sort(
                key=lambda row: (
                    float(row.get("reg_hours") or 0)
                    + float(row.get("ot_hours") or 0)
                    + float(row.get("dt_hours") or 0)
                    + float(row.get("weekly_ot_hours") or 0)
                    + float(row.get("meal_penalty_hours") or 0)
                    + float(row.get("rest_break_penalty_hours") or 0)
                ),
                reverse=self.sort_reverse,
            )

        elif sort_by == "shows":

            rows.sort(
                key=lambda row: int(
                    row.get("show_count") or 0
                ),
                reverse=self.sort_reverse,
            )

        elif sort_by == "shifts":

            rows.sort(
                key=lambda row: int(
                    row.get("item_count") or 0
                ),
                reverse=self.sort_reverse,
            )

        self._display_paystubs(rows)