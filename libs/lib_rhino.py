# libs/rhino.py

import logging
import os
import ssl
import ast
import base64

import certifi
import mechanize

from datetime import datetime

from kivy.app import App
from kivy.resources import resource_find

import libs.lib_enc

from libs.lib_rhino_db import RhinoDatabase


# ============================================================
# SSL
# ============================================================

_real_create_default_context = ssl.create_default_context


def patched_ssl_context(*args, **kwargs):

    kwargs["cafile"] = certifi.where()

    return _real_create_default_context(
        *args,
        **kwargs,
    )


# ============================================================
# Rhino Client
# ============================================================

class RhinoClient:

    USER_AGENT = (
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) "
        "Gecko/2008071615 Firefox/3.0.1-1.fc9 Firefox/3.0.1"
    )


    # ========================================================
    # INIT
    # ========================================================

    def __init__(self):

        logging.info("Creating RhinoClient")

        # ----------------------------------------------------
        # App / data directory
        # ----------------------------------------------------

        app = App.get_running_app()

        if app is None:
            raise RuntimeError(
                "RhinoClient must be created after the Kivy App starts"
            )

        self.data_dir = app.user_data_dir


        # ----------------------------------------------------
        # Database
        # ----------------------------------------------------

        self.db = RhinoDatabase()


        # ----------------------------------------------------
        # One-time legacy JSON migration
        # ----------------------------------------------------

        self._migrate_legacy_settings()


        # ----------------------------------------------------
        # Load settings from SQLite
        # ----------------------------------------------------

        self._load_settings()


        # ----------------------------------------------------
        # Rhino URLs
        # ----------------------------------------------------

        self.login_url = ""
        self.schedule_url = ""

        self.set_city(self.city)


        # ----------------------------------------------------
        # Cached files
        # ----------------------------------------------------

        self.schedule_cache_file = os.path.join(
            self.data_dir,
            "realdata.html",
        )

        self.login_cache_file = os.path.join(
            self.data_dir,
            "fullwebsite.html",
        )


        self.schedule_html = None


        # ----------------------------------------------------
        # Runtime state
        # ----------------------------------------------------

        self.browser = self._create_browser()

        self.logged_in = False


        # ----------------------------------------------------
        # Last schedule update
        # ----------------------------------------------------

        self.last_updated = self.db.get_last_updated()


        logging.info(
            "RhinoClient ready — user=%s city=%s",
            self.username,
            self.city,
        )


    # ========================================================
    # SETTINGS
    # ========================================================

    def _load_settings(self):

        settings = self.db.get_user_settings()


        def get(key, default=None):

            return settings.get(
                key,
                default,
            )


        def get_bool(key, default=False):

            value = get(
                key,
                default,
            )

            if isinstance(value, bool):
                return value

            return str(value).lower() in (
                "true",
                "1",
                "yes",
                "on",
            )


        def get_int(key, default=0):

            try:
                return int(
                    get(
                        key,
                        default,
                    )
                )

            except (TypeError, ValueError):

                return default


        # ----------------------------------------------------
        # Account
        # ----------------------------------------------------

        self.username = get(
            "username",
            "",
        )

        self.password = get(
            "password",
            "",
        )

        self.city = get(
            "city",
            "lasvegas",
        )

        self.name = get(
            "name",
            "",
        )


        # ----------------------------------------------------
        # General settings
        # ----------------------------------------------------

        self.update = get(
            "update",
            "",
        )

        self.usecache = get_bool(
            "usecache",
            False,
        )

        self.pcolor = get(
            "pcolor",
            "Azure",
        )

        self.scolor = get(
            "scolor",
            "CRAP",
        )

        self.debug = get_bool(
            "debug",
            True,
        )

        self.theme = get(
            "theme",
            "Dark",
        )

        self.theme2 = get_bool(
            "theme2",
            True,
        )


        # ----------------------------------------------------
        # Notifications
        # ----------------------------------------------------

        self.not1 = get_bool(
            "not1",
            False,
        )

        self.not2 = get_bool(
            "not2",
            False,
        )

        self.not1time = get_int(
            "not1time",
            0,
        )

        self.not2time = get_int(
            "not2time",
            0,
        )

        self.sound_effects = get(
            "sound_effects",
            "Bang",
        )

        self.refreshreload = get_bool(
            "refreshreload",
            False,
        )

        self.not_enabled = get_bool(
            "not",
            False,
        )


        # ----------------------------------------------------
        # Schedule display
        # ----------------------------------------------------

        self.hide_canceled = get_bool(
            "hide_canceled",
            False,
        )

        self.hide_shows = get_bool(
            "hide_shows",
            False,
        )

        self.today_start = get_bool(
            "today_start",
            True,
        )

        self.twenty = get_bool(
            "twenty",
            False,
        )


        # ----------------------------------------------------
        # Profile
        # ----------------------------------------------------

        self.bio = get_bool(
            "bio",
            False,
        )

        self.nick = get_bool(
            "nick",
            True,
        )

        self.phone = get_bool(
            "phone",
            False,
        )

        self.button4 = get_bool(
            "button4",
            False,
        )

        self.hidden = get_bool(
            "hidden",
            False,
        )

        self.onboarding = get_bool(
            "onboarding",
            True,
        )


        # ----------------------------------------------------
        # Menu
        # ----------------------------------------------------

        self.menu_login = get_bool(
            "Login",
            True,
        )

        self.menu_timesheets = get_bool(
            "TimeSheets",
            True,
        )

        self.menu_settings = get_bool(
            "Settings",
            True,
        )

        self.menu_notes = get_bool(
            "Notes",
            True,
        )

        self.menu_paychecks = get_bool(
            "PayChecks",
            True,
        )

        self.menu_insights = get_bool(
            "Insights",
            True,
        )

        self.menu_search = get_bool(
            "Search",
            True,
        )

        self.menu_stats = get_bool(
            "Stats",
            True,
        )

        self.menu_cloud = get_bool(
            "Cloud",
            True,
        )

        self.menu_position_list = get_bool(
            "Position List",
            True,
        )

        self.menu_close = get_bool(
            "Close",
            True,
        )


        # ----------------------------------------------------
        # Misc
        # ----------------------------------------------------

        self.branding = get_bool(
            "branding",
            False,
        )


    # ========================================================
    # LEGACY JSON MIGRATION
    # ========================================================

    def _migrate_legacy_settings(self):

        # If the DB already has a username, we're done.
        existing_username = self.db.get_user_setting(
            "username"
        )

        if existing_username:

            logging.info(
                "Rhino settings already exist in database"
            )

            return


        app = App.get_running_app()


        possible_paths = [
            os.path.join(
                app.directory,
                "userdata.json",
            ),

            os.path.join(
                self.data_dir,
                "userdata.json",
            ),

            resource_find(
                "userdata.json"
            ),
        ]


        for path in possible_paths:

            if not path:
                continue

            if not os.path.exists(path):
                continue


            logging.info(
                "Found legacy userdata: %s",
                path,
            )


            try:

                import json

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                ) as f:

                    settings = json.load(f)


                self.db.save_user_settings(
                    settings
                )


                logging.info(
                    "Migrated %d settings into rhino.db",
                    len(settings),
                )


                return


            except Exception:

                logging.exception(
                    "Failed migrating userdata.json"
                )

                return


        logging.info(
            "No legacy userdata.json found"
        )


    # ========================================================
    # CITY / URLS
    # ========================================================

    def set_city(self, city):

        city = (
            city or "lasvegas"
        ).lower().strip()


        self.city = city


        self.login_url = (
            "https://www.thinkrhino.com/"
            f"employee/{self.city}/Index.aspx"
        )


        self.schedule_url = (
            "https://www.thinkrhino.com/"
            f"employee/{self.city}/Schedule.aspx"
        )


    # ========================================================
    # BROWSER
    # ========================================================

    def _create_browser(self):

        ssl.create_default_context = patched_ssl_context

        ssl._create_default_https_context = (
            ssl._create_unverified_context
        )


        browser = mechanize.Browser()


        browser._factory._context = (
            ssl._create_unverified_context()
        )


        browser.set_handle_robots(
            False
        )

        browser.set_handle_equiv(
            False
        )


        browser.addheaders = [
            (
                "User-agent",
                self.USER_AGENT,
            )
        ]


        return browser


    # ========================================================
    # LOGIN
    # ========================================================

    def login(
        self,
        username=None,
        encrypted_password=None,
    ):

        # ----------------------------------------------------
        # Default to credentials loaded from DB
        # ----------------------------------------------------

        if username is None:

            username = self.username


        if encrypted_password is None:

            encrypted_password = self.password


        # ----------------------------------------------------
        # Validate credentials BEFORE encryption handling
        # ----------------------------------------------------
        """
        if not username:

            raise ValueError(
                "Rhino username is missing"
            )


        if not encrypted_password:

            raise ValueError(
                "Rhino password is missing"
            )

        """
        logging.info(
            "Logging into Rhino"
        )


        # ----------------------------------------------------
        # Browser
        # ----------------------------------------------------

        if self.browser is None:

            self.browser = (
                self._create_browser()
            )


        # ----------------------------------------------------
        # Open login page
        # ----------------------------------------------------

        self.browser.open(
            self.login_url
        )


        # ----------------------------------------------------
        # Select login form
        # ----------------------------------------------------

        try:

            self.browser.select_form(
                name="ctl00"
            )

        except Exception:

            self.browser.select_form(
                nr=0
            )


        # ----------------------------------------------------
        # Credentials
        # ----------------------------------------------------

        self.browser[
            "emailaddress"
        ] = username


        try:

            password = (
                libs.lib_enc.r_password(
                    encrypted_password
                )
            )

        except Exception as e:

            logging.error(
                "Unable to decode Rhino password: %s",
                e,
            )

            raise


        self.browser[
            "mypassword"
        ] = password


        # ----------------------------------------------------
        # Submit
        # ----------------------------------------------------

        response = (
            self.browser.submit()
        )


        html = response.get_data()


        text = html.decode(
            "utf-8",
            errors="ignore",
        )


        # ----------------------------------------------------
        # Verify login
        # ----------------------------------------------------

        success = (
            "View My Schedule" in text
            or "Schedule.aspx" in text
            or "Logout" in text
        )


        if success:

            self.logged_in = True

            self.last_updated = (
                datetime.now()
            )


            logging.info(
                "Rhino login successful"
            )


            return html


        self.logged_in = False


        logging.warning(
            "Rhino login failed"
        )


        return False


    # ========================================================
    # OPEN LOGIN PAGE
    # ========================================================

    def open_login_page(self):

        return self.browser.open(
            self.login_url
        )


    # ========================================================
    # DOWNLOAD SCHEDULE
    # ========================================================

    def download_schedule(self):

        if not self.logged_in:

            logging.warning(
                "Downloading schedule before login"
            )


        logging.info(
            "Downloading Rhino schedule"
        )


        response = self.browser.open(
            self.schedule_url
        )


        html = response.get_data()


        # ----------------------------------------------------
        # Save last updated time
        # ----------------------------------------------------

        self.last_updated = (
            datetime.now()
        )


        self.db.set_last_updated(
            self.last_updated
        )


        logging.info(
            "Schedule updated: %s",
            self.last_updated,
        )


        return html


    # ========================================================
    # SAVE SCHEDULE
    # ========================================================

    def save_schedule(self, filename):

        html = self.download_schedule()


        if not html:

            logging.warning(
                "No schedule HTML received"
            )

            return False


        os.makedirs(
            os.path.dirname(filename)
            or ".",
            exist_ok=True,
        )


        with open(
            filename,
            "wb",
        ) as f:

            f.write(html)


        logging.info(
            "Saved Rhino schedule: %s",
            filename,
        )


        return filename


    # ========================================================
    # LOAD CACHED HTML
    # ========================================================

    def load_cached_html(self):

        if not os.path.exists(
            self.schedule_cache_file
        ):

            logging.warning(
                "No cached schedule found: %s",
                self.schedule_cache_file,
            )

            return None


        try:

            with open(
                self.schedule_cache_file,
                "rb",
            ) as f:

                self.schedule_html = (
                    f.read()
                )


            logging.info(
                "Loaded cached Rhino schedule"
            )


            return self.schedule_html


        except OSError as e:

            logging.error(
                "Unable to load cached schedule: %s",
                e,
            )

            return None


    # ========================================================
    # GET SCHEDULE
    # ========================================================

    def get_schedule(self):

        """
        Convenience method.

        Returns downloaded schedule HTML.
        """

        return self.download_schedule()


    # ========================================================
    # CLOSE
    # ========================================================

    def close(self):

        if self.db:

            self.db.close()

            self.db = None

    def has_credentials(self):

        return bool(
            self.username and
            self.password
        )