from datetime import datetime, date,timedelta
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (
    BooleanProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from libs.lib_remote_config import RemoteConfig
from libs.pay_schedule import PaySchedule




class ScheduleMarkerItem(BoxLayout):
    marker_title = StringProperty("")
    marker_subtitle = StringProperty("")


class ScheduleTodayItem(BoxLayout):
    pass


class HistoryScreen(Screen):

    shows = ListProperty([])
    today_index = NumericProperty(0)
    pay_schedule = None

    def on_pre_enter(self):
        self.load_schedule()


    def _pay_marker(self, marker_type, target_date):
        """
        Create a calendar marker for the schedule.
        """

        if marker_type == "pay_period":
            period = self.pay_schedule.period_for_date(target_date)

            return {
                "key_viewclass": "ScheduleMarkerItem",
                "is_today": False,
                "is_pay_period": True,
                "is_pay_week": False,
                "is_pay_day": False,
                "marker_title": "PAY PERIOD",
                "marker_subtitle": self.pay_schedule.format_range(
                    period["start"],
                    period["end"],
                ),
            }

        if marker_type == "pay_week":
            week = self.pay_schedule.pay_week_for_date(target_date)

            return {
                "key_viewclass": "ScheduleMarkerItem",

                "is_today": False,
                "is_pay_period": False,
                "is_pay_week": True,
                "is_pay_day": False,
                "marker_title": "PAY WEEK",
                "marker_subtitle": self.pay_schedule.format_range(
                    week["start"],
                    week["end"],
                ),
            }

        if marker_type == "pay_day":
            return {
                "key_viewclass": "ScheduleMarkerItem",

                "is_today": False,
                "is_pay_period": False,
                "is_pay_week": False,
                "is_pay_day": True,
                "marker_title": "PAY DAY",
                "marker_subtitle": self.pay_schedule.format_date(
                    target_date,
                ),
            }

        return None






    def load_schedule(self):

        app = App.get_running_app()
        remote_config = RemoteConfig()

        self.pay_schedule = PaySchedule(
            remote_config.config
        )



        if not hasattr(app, "rhino_db") or app.rhino_db is None:
            print("[SCHEDULE] No database available")
            return

        rows = app.rhino_db.get_all_shows()

        # Sort chronologically
        rows.sort(key=self._sort_key)










        today = datetime.now().date()
        print("[SCHEDULE] APP TODAY =", today)
        print("[SCHEDULE] APP NOW   =", datetime.now())
        

        # -----------------------------------------------------
        # BUILD SHOW EVENTS
        # -----------------------------------------------------

        events = []

        for row in rows:
            show_date = self._parse_date(row.get("date"))

            if show_date is None:
                continue

            time_string = str(
                row.get("time", "")
            ).strip()

            events.append({
                "date": show_date,
                "time": time_string,
                "priority": 30,
                "data": self._show_to_item(row),
            })

        # -----------------------------------------------------
        # BUILD PAY SCHEDULE EVENTS
        # -----------------------------------------------------

        events.extend(
            self._build_pay_markers(rows)
        )

        # -----------------------------------------------------
        # SORT EVERYTHING CHRONOLOGICALLY
        # -----------------------------------------------------

        def event_sort_key(event):
            time_string = event["time"]

            parsed_time = None

            for fmt in (
                "%H:%M",
                "%I:%M %p",
                "%I:%M%p",
            ):
                try:
                    parsed_time = datetime.strptime(
                        time_string,
                        fmt,
                    ).time()
                    break
                except ValueError:
                    pass

            if parsed_time is None:
                parsed_time = datetime.min.time()

            return (
                event["date"],
                parsed_time,
                event["priority"],
            )

        events.sort(key=event_sort_key)

        # -----------------------------------------------------
        # INSERT TODAY MARKER
        # -----------------------------------------------------

        data = []
        today_index = None
        today_marker_added = False

        for event in events:

            event_date = event["date"]

            # Put TODAY immediately before today's shows,
            # but after any pay-period/pay-week marker occurring
            # at the beginning of today.
            if (
                not today_marker_added
                and event_date >= today
                and not event["data"].get("is_pay_day", False)
            ):
                today_index = len(data)

                data.append({
                    "key_viewclass": "ScheduleTodayItem",

                    "is_today": True,
                    "is_pay_period": False,
                    "is_pay_week": False,
                    "is_pay_day": False,
                    "marker_title": "",
                    "marker_subtitle": "",
                })

                today_marker_added = True

            data.append(event["data"])

        # If there are no future events, put TODAY at the end.
        if not today_marker_added:
            today_index = len(data)

            data.append({
                "key_viewclass": "ScheduleTodayItem",

                "is_today": True,
                "is_pay_period": False,
                "is_pay_week": False,
                "is_pay_day": False,
                "marker_title": "",
                "marker_subtitle": "",
            })

        self.shows = data
        self.today_index = today_index
        for i, item in enumerate(data):
            print(
                "[RV]",
                i,
                item.get("key_viewclass"),
                item.get("marker_title", ""),
                item.get("marker_subtitle", ""),
                item.get("show", "")[:40],
            )
        rv = self.ids.schedule_rv
        rv.data = data

        print(
            f"[SCHEDULE] Loaded {len(rows)} shows "
            f"(today marker index: {today_index})"
        )

        Clock.schedule_once(
            self._scroll_to_today,
            0.3,
        )





    
    def _build_pay_markers(self, rows):
        dates = []

        for row in rows:
            show_date = self._parse_date(row.get("date"))

            if show_date:
                dates.append(show_date)

        today = datetime.now().date()
        dates.append(today)

        if not dates:
            return []

        first_date = min(dates)
        last_date = max(dates)

        # Extend far enough to include the next payday.
        payday = self.pay_schedule.payday_for_date(last_date)

        if payday:
            last_date = max(last_date, payday)

        markers = []

        current = first_date

        while current <= last_date:

            # -----------------------------
            # PAY PERIOD
            # -----------------------------

            period = self.pay_schedule.period_for_date(current)

            if (
                period
                and current == period["start"]
            ):
                markers.append({
                    "date": current,
                    "time": "00:00",
                    "priority": 10,
                    "data": self._pay_marker(
                        "pay_period",
                        current,
                    ),
                })

            # -----------------------------
            # PAY WEEK
            # -----------------------------

            week = self.pay_schedule.pay_week_for_date(current)

            if current == week["start"]:
                markers.append({
                    "date": current,
                    "time": "00:01",
                    "priority": 20,
                    "data": self._pay_marker(
                        "pay_week",
                        current,
                    ),
                })

            # -----------------------------
            # PAY DAY
            # -----------------------------

            if self.pay_schedule.is_payday(current):
                markers.append({
                    "date": current,
                    "time": "23:59",
                    "priority": 40,
                    "data": self._pay_marker(
                        "pay_day",
                        current,
                    ),
                })

            current += timedelta(days=1)

        print(
            "[PAY SCHEDULE] Generated",
            len(markers),
            "markers",
        )

        for marker in markers:
            print(
                "[PAY SCHEDULE]",
                marker["data"].get("marker_title"),
                marker["data"].get("marker_subtitle"),
            )

        return markers

    def _show_to_item(self, row):

        date = self._parse_date(
            row.get("date")
        )

        if date:

            day = date.strftime(
                "%a"
            ).upper()

            date_text = date.strftime(
                "%b %d"
            ).upper()

        else:

            day = ""

            date_text = row.get(
                "date",
                "",
            )

        return {

            "key_viewclass": "ShowCard",


            "is_today": False,

            "show": row.get(
                "show",
                "",
            ),

            "day": day,

            "date": date_text,

            "time": row.get(
                "time",
                "",
            ),

            "venue": row.get(
                "venue",
                "",
            ),

            "address": row.get(
                "location",
                "",
            ),

            "position": row.get(
                "position",
                "",
            ),

            "show_class": row.get(
                "type",
                "",
            ),

            "status": row.get(
                "status",
                "",
            ),

            "venue_code": "",

            "status_icon": self._status_icon(
                row
            ),

            "cancelled": bool(
                row.get(
                    "cancelled",
                    0,
                )
            ),
        }

    def _status_icon(self, row):

        if row.get("cancelled"):
            return "close"

        status = str(
            row.get(
                "status",
                "",
            )
        ).lower()

        if "confirm" in status:
            return "check"

        return ""

    def _sort_key(self, row):

        date = self._parse_date(
            row.get("date")
        )

        if date is None:
            return datetime.max

        time_string = str(
            row.get("time", "")
        ).strip()

        for fmt in (
            "%H:%M",
            "%I:%M %p",
            "%I:%M%p",
        ):

            try:

                parsed_time = datetime.strptime(
                    time_string,
                    fmt,
                ).time()

                return datetime.combine(
                    date,
                    parsed_time,
                )

            except ValueError:
                pass

        return datetime.combine(
            date,
            datetime.min.time(),
        )

    def _parse_date(self, value):

        if not value:
            return None

        value = str(value).strip()

        formats = (
            "%m/%d/%Y",
            "%m/%d/%y",
            "%Y-%m-%d",
            "%m-%d-%Y",
            "%m-%d-%y",
        )

        for fmt in formats:

            try:

                return datetime.strptime(
                    value,
                    fmt,
                ).date()

            except ValueError:
                pass

        print(
            f"[SCHEDULE] Could not parse date: {value}"
        )

        return None

    def _scroll_to_today(self, *args):
        rv = self.ids.schedule_rv
        layout = rv.layout_manager

        if not rv.data or layout is None:
            return

        try:
            # Ask the RecycleView layout to bring TODAY into view.
            layout.goto_view(self.today_index)

            # Give the layout one frame to create the actual view.
            Clock.schedule_once(self._scroll_to_today_widget, 0)

        except Exception:
            import traceback
            traceback.print_exc()


    def _scroll_to_today_widget(self, *args):
        rv = self.ids.schedule_rv

        try:
            today_view = rv.view_adapter.get_visible_view(self.today_index)

            if today_view is None:
                # The view hasn't been created yet; try again next frame.
                Clock.schedule_once(self._scroll_to_today_widget, 0.05)
                return

            # Let Kivy's ScrollView handle the actual positioning.
            rv.scroll_to(
                today_view,
                padding=12,
                animate=False,
            )

            print(
                f"[SCHEDULE] Scrolled to TODAY index={self.today_index}"
            )

        except Exception:
            import traceback
            print("[SCHEDULE] Could not scroll to TODAY:")
            traceback.print_exc()