import json
import logging
import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_find

from libs.applibs import utils


class Root(ScreenManager):

    history = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.bind(on_keyboard=self._handle_keyboard)

        # ---------------------------------------------------------
        # Load the screen registry
        # ---------------------------------------------------------

        path = resource_find("screens.json")

        try:
            with open(path, "r", encoding="utf-8") as f:
                self.screens_data = json.load(f)

        except Exception:
            try:
                with open(
                    utils.abs_path("screens.json"),
                    "r",
                    encoding="utf-8"
                ) as f:
                    self.screens_data = json.load(f)

            except Exception:
                with open(
                    utils.abs_path("YourApp/screens.json"),
                    "r",
                    encoding="utf-8"
                ) as f:
                    self.screens_data = json.load(f)

        logging.info(
            "Root initialized with %d lazy-loaded screens",
            len(self.screens_data)
        )

    # ---------------------------------------------------------
    # Keyboard / Back button
    # ---------------------------------------------------------

    def _handle_keyboard(self, instance, key, *args):

        if key == 27:
            self.pop()
            return True

    # ---------------------------------------------------------
    # Lazy screen loading
    # ---------------------------------------------------------

    def load_screen(self, screen_name):

        """
        Lazily create and add a screen.

        The screen's Python module is imported BEFORE its KV file
        is loaded. This is important because the Python module may
        define/register custom widgets used by the KV file.
        """

        # Already loaded?
        if self.has_screen(screen_name):
            return

        # Does the screen exist in screens.json?
        if screen_name not in self.screens_data:
            raise KeyError(
                f'Screen "{screen_name}" is not defined in screens.json'
            )

        logging.info(
            "LAZY LOAD SCREEN: %s",
            screen_name
        )

        screen = self.screens_data[screen_name]

        # ---------------------------------------------------------
        # 1. Import the screen's Python module FIRST
        #
        # This allows it to register custom classes such as
        # YourContainer before the KV file references them.
        # ---------------------------------------------------------

        logging.info(
            "IMPORT SCREEN: %s",
            screen["import"]
        )

        exec(screen["import"])

        # ---------------------------------------------------------
        # 2. Load the screen's KV file
        # ---------------------------------------------------------

        kv_path = utils.abs_path(screen["kv"])

        if os.path.exists(kv_path):

            logging.info(
                "Loading KV: %s",
                kv_path
            )

            Builder.load_file(kv_path)

        else:

            # iOS packaged-app fallback
            fallback_path = utils.abs_path(
                os.path.join("YourApp", screen["kv"])
            )

            logging.info(
                "KV not found at %s",
                kv_path
            )

            logging.info(
                "Trying iOS KV path: %s",
                fallback_path
            )

            if not os.path.exists(fallback_path):
                raise FileNotFoundError(
                    f"Could not find KV file for '{screen_name}'. "
                    f"Tried:\n"
                    f"  {kv_path}\n"
                    f"  {fallback_path}"
                )

            Builder.load_file(fallback_path)

        # ---------------------------------------------------------
        # 3. Create the screen object
        # ---------------------------------------------------------

        logging.info(
            "CREATING SCREEN: %s",
            screen["object"]
        )

        screen_object = eval(screen["object"])

        # ---------------------------------------------------------
        # 4. Set the ScreenManager name
        # ---------------------------------------------------------

        screen_object.name = screen_name

        # ---------------------------------------------------------
        # 5. Add to ScreenManager
        # ---------------------------------------------------------

        logging.info(
            "ADDING SCREEN: %s",
            screen_name
        )

        self.add_widget(screen_object)

        logging.info(
            "SCREEN READY: %s",
            screen_name
        )

    # ---------------------------------------------------------
    # Make sure a screen exists before switching to it
    # ---------------------------------------------------------

    def _ensure_screen_loaded(self, screen_name):

        if not self.has_screen(screen_name):
            self.load_screen(screen_name)

    # ---------------------------------------------------------
    # Push / Navigate
    # ---------------------------------------------------------

    def push(self, screen_name, side="left"):

        """
        Lazy-load a screen, add it to navigation history,
        and switch to it.
        """

        if self.current != screen_name:

            self.history.append({
                "name": screen_name,
                "side": side
            })

        self._ensure_screen_loaded(screen_name)

        self.transition.direction = side

        self.current = screen_name

    # ---------------------------------------------------------
    # Replace navigation history
    # ---------------------------------------------------------

    def push_replacement(self, screen_name, side="left"):

        """
        Clear navigation history and switch to a screen.
        """

        self.history.clear()

        self.push(screen_name, side)

    # ---------------------------------------------------------
    # Back
    # ---------------------------------------------------------

    def pop(self):

        """
        Return to the previous screen in navigation history.
        """

        if not len(self.history) > 1:
            return

        cur_side = self.history.pop()["side"]

        prev_screen = self.history[-1]

        # Reverse the transition direction
        if cur_side == "left":
            side = "right"

        elif cur_side == "right":
            side = "left"

        elif cur_side == "up":
            side = "down"

        elif cur_side == "down":
            side = "up"

        else:
            side = "right"

        self.transition.direction = side

        self.current = prev_screen["name"]