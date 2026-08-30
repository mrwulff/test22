import json
import logging
import os
import urllib.request

from kivy.utils import platform


REMOTE_CONFIG_URL = (
    "https://raw.githubusercontent.com/mrwulff/"
    "schedulara-config/main/config.json"
)

DEFAULT_CONFIG = {
    "version": 0,
    "show_prefixes": {
        "(MGM) ": "MGM",
        "(Dolby) ": "Dolby",
    },
}


class RemoteConfig:

    def __init__(self):
        self.config = DEFAULT_CONFIG.copy()
        self._load_cached()

    # ---------------------------------------------------------
    # Cache location
    # ---------------------------------------------------------

    def _cache_path(self):
       
        from kivy.app import App
        return os.path.join(
            App.get_running_app().user_data_dir,
            "remote_config.json"
        )



    # ---------------------------------------------------------
    # Load cached config
    # ---------------------------------------------------------

    def _load_cached(self):
        path = self._cache_path()

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, dict):
                self.config.update(data)

                logging.info(
                    "Loaded cached remote config v%s",
                    self.config.get("version", "?")
                )

        except Exception as e:
            logging.info(
                "No cached remote config: %s",
                e
            )

    # ---------------------------------------------------------
    # Download latest config
    # ---------------------------------------------------------

    def update(self):
        try:
            logging.info("Checking remote config...")
            print (REMOTE_CONFIG_URL,'url')

            request = urllib.request.Request(
                REMOTE_CONFIG_URL,
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

            if not isinstance(data, dict):
                raise ValueError("Remote config is not a JSON object")

            # Make sure the important section exists.
            if "show_prefixes" not in data:
                raise ValueError(
                    "Remote config missing show_prefixes"
                )

            if not isinstance(
                data["show_prefixes"],
                dict
            ):
                raise ValueError(
                    "show_prefixes must be an object"
                )

            self.config = data

            self._save_cached()

            logging.info(
                "Remote config updated to v%s",
                self.config.get("version", "?")
            )

            return True

        except Exception as e:

            logging.warning(
                "Remote config update failed: %s",
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
                "Could not save remote config: %s",
                e
            )

    # ---------------------------------------------------------
    # Show prefixes
    # ---------------------------------------------------------

    @property
    def show_prefixes(self):
        return self.config.get(
            "show_prefixes",
            DEFAULT_CONFIG["show_prefixes"]
        )