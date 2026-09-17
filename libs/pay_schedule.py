from datetime import date, timedelta


class PaySchedule:
    """
    Calculates pay weeks, pay periods, and paydays from a remotely
    configured anchor date.

    The important thing here is that all calculations are based on
    calendar dates, not datetimes/timezones. This prevents the
    occasional one-day drift we've seen.
    """

    WEEKDAYS = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6,
    }

    def __init__(self, config):
        schedule = config.get("pay_schedule", {})

        self.week_start = schedule.get(
            "pay_week_start",
            "wednesday",
        ).lower()

        self.period_start = self._parse_date(
            schedule.get("pay_period_start")
        )

        self.period_length = int(
            schedule.get(
                "pay_period_length_days",
                14,
            )
        )

        self.payday = self._parse_date(
            schedule.get("payday")
        )

    # ---------------------------------------------------------
    # DATE HELPERS
    # ---------------------------------------------------------

    @staticmethod
    def _parse_date(value):
        if not value:
            return None

        if isinstance(value, date):
            return value

        return date.fromisoformat(str(value))

    # ---------------------------------------------------------
    # PAY PERIOD
    # ---------------------------------------------------------

    def period_for_date(self, target):
        """
        Return the pay period containing target.

        Example:

            2026-09-09 through 2026-09-22
            payday 2026-09-29
        """

        target = self._parse_date(target)

        if self.period_start is None:
            return None

        days_since_start = (
            target - self.period_start
        ).days

        period_number = (
            days_since_start // self.period_length
        )

        start = (
            self.period_start
            + timedelta(
                days=period_number * self.period_length
            )
        )

        end = (
            start
            + timedelta(
                days=self.period_length - 1
            )
        )

        payday = None

        if self.payday is not None:
            payday = (
                self.payday
                + timedelta(
                    days=period_number * self.period_length
                )
            )

        return {
            "number": period_number,
            "start": start,
            "end": end,
            "payday": payday,
        }

    # ---------------------------------------------------------
    # PAY WEEK
    # ---------------------------------------------------------

    def pay_week_for_date(self, target):
        """
        Return the Wednesday-Tuesday pay week containing target.
        """

        target = self._parse_date(target)

        start_weekday = self.WEEKDAYS.get(
            self.week_start,
            2,  # Wednesday
        )

        days_since_start = (
            target.weekday() - start_weekday
        ) % 7

        start = (
            target
            - timedelta(days=days_since_start)
        )

        end = (
            start
            + timedelta(days=6)
        )

        return {
            "start": start,
            "end": end,
        }

    # ---------------------------------------------------------
    # PAYDAY
    # ---------------------------------------------------------

    def is_payday(self, target):
        """
        True if target is a payday.
        """

        target = self._parse_date(target)

        payday = self.payday_for_date(target)

        return (
            payday is not None
            and target == payday
        )

    def payday_for_date(self, target):
        """
        Return the payday associated with the pay period
        containing target.
        """

        period = self.period_for_date(target)

        if period is None:
            return None

        return period["payday"]

    # ---------------------------------------------------------
    # HELPERS FOR UI
    # ---------------------------------------------------------

    @staticmethod
    def format_range(start, end):
        """
        Example:

            SEP 09 – SEP 22
        """

        return (
            f"{start.strftime('%b %d').upper()}"
            f" – "
            f"{end.strftime('%b %d').upper()}"
        )

    @staticmethod
    def format_date(value):
        """
        Example:

            TUE SEP 29
        """

        return value.strftime("%a %b %d").upper()