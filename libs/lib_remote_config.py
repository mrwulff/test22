import json
import logging
import os
import urllib.request
import urllib.parse

from kivy.app import App


REMOTE_CONFIG_BASE_URL = (
    "https://raw.githubusercontent.com/"
    "mrwulff/schedulara-config/main/"
)

DEFAULT_CONFIG = {
    "version": 0,
    "show_prefixes": {
        "(MGM) ": "MGM",
        "(Dolby) ": "Dolby",
    },
}


class RemoteConfig:

    def __init__(self, filename="config.json", default=None):
        self.filename = filename

        if default is None:
            default = DEFAULT_CONFIG

        self.default = default
        self.config = default.copy()

        self._load_cached()

    # ---------------------------------------------------------
    # Remote URL
    # ---------------------------------------------------------

    @property
    def remote_url(self):
        return (
            REMOTE_CONFIG_BASE_URL
            + urllib.parse.quote(self.filename)
        )

    # ---------------------------------------------------------
    # Cache location
    # ---------------------------------------------------------

    def _cache_path(self):

        # Turn position_list.json into a safe cache filename
        cache_name = self.filename.replace("/", "_")

        return os.path.join(
            App.get_running_app().user_data_dir,
            "remote_" + cache_name
        )

    # ---------------------------------------------------------
    # Load cached config
    # ---------------------------------------------------------

    def _load_cached(self):

        path = self._cache_path()

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

            self.config = data

            logging.info(
                "Loaded cached remote file: %s",
                self.filename
            )

        except Exception as e:

            logging.info(
                "No cached remote file %s: %s",
                self.filename,
                e
            )

    # ---------------------------------------------------------
    # Download latest config
    # ---------------------------------------------------------

    def update(self):

        try:

            logging.info(
                "Checking remote config: %s",
                self.filename
            )

            request = urllib.request.Request(
                self.remote_url,
                headers={
                    "User-Agent": "Schedulara-iOS"
                }
            )

            with urllib.request.urlopen(
                request,
                timeout=10
            ) as response:

                data = json.loads(
                    response.read().decode("utf-8")
                )

            self.config = data

            self._save_cached()

            logging.info(
                "Remote file updated: %s",
                self.filename
            )

            return True

        except Exception as e:

            logging.warning(
                "Remote file update failed (%s): %s",
                self.filename,
                e
            )

            return False

    # ---------------------------------------------------------
    # Save cache
    # ---------------------------------------------------------

    def _save_cached(self):

        path = self._cache_path()

        try:

            os.makedirs(
                os.path.dirname(path),
                exist_ok=True
            )

            with open(
                path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    self.config,
                    f,
                    indent=4
                )

        except Exception as e:

            logging.warning(
                "Could not save remote file %s: %s",
                self.filename,
                e
            )

    # ---------------------------------------------------------
    # Generic data access
    # ---------------------------------------------------------

    @property
    def data(self):
        return self.config

    # ---------------------------------------------------------
    # Show prefixes
    # ---------------------------------------------------------

    @property
    def show_prefixes(self):

        return self.config.get(
            "show_prefixes",
            DEFAULT_CONFIG["show_prefixes"]
        )