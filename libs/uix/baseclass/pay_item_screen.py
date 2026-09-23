from datetime import datetime

from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.screenmanager import Screen


class PaystubItemScreen(Screen):
    payroll_item_id = StringProperty("")

    # ---------------------------------------------------------
    # SHIFT INFORMATION
    # ---------------------------------------------------------

    show_name = StringProperty("")
    job_number = StringProperty("")
    position = StringProperty("")
    client = StringProperty("")

    shift_date = StringProperty("")
    shift_time = StringProperty("")

    # ---------------------------------------------------------
    # PAYROLL HOURS
    # ---------------------------------------------------------

    reg_hours = StringProperty("0")
    ot_hours = StringProperty("0")
    dt_hours = StringProperty("0")
    weekly_ot_hours = StringProperty("0")

    meal_penalty_hours = StringProperty("0")
    rest_break_penalty_hours = StringProperty("0")

    # ---------------------------------------------------------
    # PAYROLL VALUES
    # ---------------------------------------------------------

    base_rate = StringProperty("$0.00")
    blended_rate = StringProperty("$0.00")
    total_pay = StringProperty("$0.00")

    # ---------------------------------------------------------
    # PAYROLL TABLE DISPLAY
    # ---------------------------------------------------------

    regular_earnings = StringProperty("")
    overtime_earnings = StringProperty("")
    weekly_ot_earnings = StringProperty("")
    double_time_earnings = StringProperty("")

    # ---------------------------------------------------------
    # SCHEDULE MATCH INFORMATION
    # ---------------------------------------------------------

    schedule_status = StringProperty("")
    schedule_date = StringProperty("")
    schedule_time = StringProperty("")
    schedule_job = StringProperty("")
    schedule_position = StringProperty("")

    # ---------------------------------------------------------
    # PRIVACY / LAYOUT
    # ---------------------------------------------------------

    show_calculations = BooleanProperty(True)

    payroll_card_height = NumericProperty(300)


    regular_calc = StringProperty("")
    overtime_calc = StringProperty("")
    weekly_ot_calc = StringProperty("")
    double_time_calc = StringProperty("")

    # ---------------------------------------------------------
    # SCREEN ENTRY
    # ---------------------------------------------------------

    regular_rate_display = StringProperty("")
    overtime_rate_display = StringProperty("")
    weekly_ot_rate_display = StringProperty("")
    weekly_ot_rate = StringProperty("")
    double_time_rate_display = StringProperty("")



    def on_pre_enter(self):
        print("[PAY ITEM] on_pre_enter")
        print("[PAY ITEM] payroll_item_id =", self.payroll_item_id)

        self.load_item()

    # ---------------------------------------------------------
    # LOAD PAYROLL ITEM
    # ---------------------------------------------------------

    def load_item(self):
        app = App.get_running_app()

        print("[PAY ITEM] load_item")
        print("[PAY ITEM] app.db =", app.db)

        if not self.payroll_item_id:
            print("[PAY ITEM] No payroll item ID")
            return

        row = app.db.db.execute(
            """
            SELECT
                id,
                show_id,
                job_number,
                class,
                position,
                client,
                show,
                time_in,
                time_out,
                reg_hours,
                ot_hours,
                dt_hours,
                weekly_ot_hours,
                meal_penalty_hours,
                rest_break_penalty_hours,
                base_rate,
                blended_rate,
                pay
            FROM payroll_items
            WHERE id = ?
            """,
            (self.payroll_item_id,),
        ).fetchone()

        if not row:
            print("[PAY ITEM] No payroll item found")
            return

        print("[PAY ITEM] row =", dict(row))

        # -----------------------------------------------------
        # BASIC SHIFT INFORMATION
        # -----------------------------------------------------

        self.show_name = row["show"] or ""
        self.job_number = row["job_number"] or ""
        self.position = row["position"] or ""
        self.client = row["client"] or ""

        # -----------------------------------------------------
        # HOURS
        # -----------------------------------------------------

        self.reg_hours = self._hours(row["reg_hours"])
        self.ot_hours = self._hours(row["ot_hours"])
        self.dt_hours = self._hours(row["dt_hours"])
        self.weekly_ot_hours = self._hours(row["weekly_ot_hours"])

        self.meal_penalty_hours = self._hours(
            row["meal_penalty_hours"]
        )

        self.rest_break_penalty_hours = self._hours(
            row["rest_break_penalty_hours"]
        )

        # -----------------------------------------------------
        # RAW RATES
        # -----------------------------------------------------

        raw_base_rate = float(row["base_rate"] or 0)
        raw_blended_rate = float(row["blended_rate"] or 0)
        raw_pay = float(row["pay"] or 0)

        # -----------------------------------------------------
        # SHIFT TIME
        # -----------------------------------------------------

        self._format_shift_times(
            row["time_in"],
            row["time_out"],
        )

        # -----------------------------------------------------
        # PRIVACY SETTING
        # -----------------------------------------------------

        show_money = (
            str(
                app.db.get_user_setting(
                    "show_pay_amounts",
                    "True",
                )
            ).lower()
            == "true"
        )

        self.show_calculations = show_money

        # -----------------------------------------------------
        # PAYROLL DISPLAY
        # -----------------------------------------------------

        if show_money:

            self.base_rate = self._money(raw_base_rate)
            self.blended_rate = self._money(row["blended_rate"])
            self.weekly_ot_rate = self.blended_rate
            self.total_pay = self._money(raw_pay)

            self._build_calculations(
                row["reg_hours"],
                row["ot_hours"],
                row["dt_hours"],
                row["weekly_ot_hours"],
                raw_base_rate,
                raw_blended_rate,
            )

        else:

            self.base_rate = "••••••"
            self.blended_rate = "••••••"
            self.total_pay = "••••••"

            self.regular_earnings = ""
            self.overtime_earnings = ""
            self.weekly_ot_earnings = ""
            self.double_time_earnings = ""

        # -----------------------------------------------------
        # DYNAMIC PAYROLL CARD HEIGHT
        # -----------------------------------------------------

        visible_rows = 1  # Regular

        if float(row["ot_hours"] or 0):
            visible_rows += 1

        if float(row["weekly_ot_hours"] or 0):
            visible_rows += 1

        if float(row["dt_hours"] or 0):
            visible_rows += 1

        # Compact card:
        #
        # header
        # rows
        # payroll total
        #
        self.payroll_card_height = (
            150
            + (visible_rows * 68)
        )

        print("[PAY ITEM] loaded:", self.show_name)
        print("[PAY ITEM] position:", self.position)
        print("[PAY ITEM] job:", self.job_number)
        print("[PAY ITEM] client:", self.client)
        print("[PAY ITEM] total:", self.total_pay)

    # ---------------------------------------------------------
    # SHIFT TIME FORMATTING
    # ---------------------------------------------------------

    def _format_shift_times(self, time_in, time_out):
        """
        Display:

            8:00 AM – 6:00 PM

        or:

            8:00 AM – 1:00 AM (+1 day)
        """

        if not time_in:
            self.shift_date = ""
            self.shift_time = ""
            return

        try:
            start = datetime.strptime(
                time_in,
                "%m/%d/%Y %I:%M:%S %p",
            )

            end = None

            if time_out:
                end = datetime.strptime(
                    time_out,
                    "%m/%d/%Y %I:%M:%S %p",
                )

            self.shift_date = start.strftime(
                "%b %-d, %Y"
            )

            start_text = start.strftime(
                "%-I:%M %p"
            )

            if end:
                end_text = end.strftime(
                    "%-I:%M %p"
                )

                if end.date() > start.date():
                    self.shift_time = (
                        f"{start_text} – "
                        f"{end_text} (+1 day)"
                    )
                else:
                    self.shift_time = (
                        f"{start_text} – "
                        f"{end_text}"
                    )

            else:
                self.shift_time = start_text

        except Exception as exc:
            print(
                "[PAY ITEM] time format error:",
                exc,
            )

            self.shift_date = str(
                time_in or ""
            )

            self.shift_time = str(
                time_in or ""
            )

    # ---------------------------------------------------------
    # EARNINGS CALCULATIONS
    # ---------------------------------------------------------
    def _build_calculations(
        self,
        reg_hours,
        ot_hours,
        dt_hours,
        weekly_ot_hours,
        base_rate,
        blended_rate,
    ):
        reg = float(reg_hours or 0)
        ot = float(ot_hours or 0)
        dt = float(dt_hours or 0)
        weekly = float(weekly_ot_hours or 0)

        base = float(base_rate or 0)
        blended = float(blended_rate or 0)

        # Regular
        if reg:
            amount = reg * base

            self.regular_rate_display = f"${base:.2f}"
            self.regular_earnings = f"${amount:,.2f}"
            self.regular_calc = (
                f"{self._hour_text(reg)} × "
                f"${base:.2f} = "
                f"${amount:,.2f}"
            )
        else:
            self.regular_rate_display = ""
            self.regular_earnings = ""
            self.regular_calc = ""

        # Daily OT = 1.5 × base rate
        if ot:
            ot_rate = base * 1.5
            amount = ot * ot_rate

            self.overtime_rate_display = f"${ot_rate:.2f}"
            self.overtime_earnings = f"${amount:,.2f}"
            self.overtime_calc = (
                f"{self._hour_text(ot)} × "
                f"${base:.2f} × 1.5 = "
                f"${amount:,.2f}"
            )
        else:
            self.overtime_rate_display = ""
            self.overtime_earnings = ""
            self.overtime_calc = ""

        # Weekly OT = 1.5 × blended rate
        if weekly:
            weekly_rate = blended if blended else base
            weekly_ot_rate = weekly_rate * 1.5
            amount = weekly * weekly_ot_rate

            self.weekly_ot_rate_display = f"${weekly_ot_rate:.4f}"
            self.weekly_ot_earnings = f"${amount:,.2f}"
            self.weekly_ot_calc = (
                f"{self._hour_text(weekly)} × "
                f"${weekly_rate:.4f} × 1.5 = "
                f"${amount:,.2f}"
            )
        else:
            self.weekly_ot_rate_display = ""
            self.weekly_ot_earnings = ""
            self.weekly_ot_calc = ""

        # Double time = 2 × base rate
        if dt:
            dt_rate = base * 2
            amount = dt * dt_rate

            self.double_time_rate_display = f"${dt_rate:.2f}"
            self.double_time_earnings = f"${amount:,.2f}"
            self.double_time_calc = (
                f"{self._hour_text(dt)} × "
                f"${base:.2f} × 2 = "
                f"${amount:,.2f}"
            )
        else:
            self.double_time_rate_display = ""
            self.double_time_earnings = ""
            self.double_time_calc = ""

    @staticmethod
    def _hour_text(value):
        value = float(value)

        if value.is_integer():
            number = str(int(value))
        else:
            number = f"{value:g}"

        return (
            f"{number} hr"
            if value == 1
            else f"{number} hrs"
        )

    @staticmethod
    def _money(value):
        if value is None:
            return "$0.00"

        #return  "534"
        return f"${float(value):,.1f}"

    # ---------------------------------------------------------
    # NAVIGATION
    # ---------------------------------------------------------

    def go_back(self):
        app = App.get_running_app()

        print("[PAY ITEM] Going back to pay")

        if hasattr(app, "change_screen"):
            app.change_screen(
                "pay",
                "right",
            )
        elif self.manager:
            self.manager.transition.direction = "right"
            self.manager.current = "pay"


    @staticmethod
    def _hours(value):
        if value is None:
            return "0"

        value = float(value)

        if value.is_integer():
            return f"{int(value)}"

        return f"{value:.2f}".rstrip("0").rstrip(".")

    @staticmethod
    def _hour_text(value):
        value = float(value)

        if value.is_integer():
            return f"{int(value)} hr" if value == 1 else f"{int(value)} hrs"

        return f"{value:g} hrs"



    

# -------------------------------------------------------------
# LAZY LOADER COMPATIBILITY
# -------------------------------------------------------------

pay_itemscreen = PaystubItemScreen