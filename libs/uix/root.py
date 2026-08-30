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

        # Load the screen registry.
        path = resource_find("screens.json")
        
        try:
            with open(path) as f:
                self.screens_data = json.load(f)
        except Exception:
            try:
                with open(utils.abs_path("screens.json")) as f:
                    self.screens_data = json.load(f)
            except Exception:
                with open(utils.abs_path("YourApp/screens.json")) as f:
                    self.screens_data = json.load(f)
        
        #with open(utils.abs_path("screens.json")) as f:
        #    self.screens_data = json.load(f)

        logging.info(
            "Root initialized with %d lazy-loaded screens",
            len(self.screens_data)
        )

    def _handle_keyboard(self, instance, key, *args):
        if key == 27:
            self.pop()
            return True

    def load_screen(self, screen_name):
        """
        Lazily create and add a screen.

        The screen's Python class and KV file are only loaded when the
        screen is actually requested.
        """

        if self.has_screen(screen_name):
            return

        if screen_name not in self.screens_data:
            raise KeyError(
                f'Screen "{screen_name}" is not defined in screens.json'
            )

        logging.info("LAZY LOAD SCREEN: %s", screen_name)

        screen = self.screens_data[screen_name]

        # Load the KV file.
        try:
            Builder.load_file(utils.abs_path(screen["kv"]))
        except Exception:
           Builder.load_file("YourApp/" + screen["kv"])
        #Builder.load_file(utils.abs_path(screen["kv"]))
        # Import the screen class.
        exec(screen["import"])

        # Create the screen object.
        screen_object = eval(screen["object"])

        screen_object.name = screen_name

        logging.info("ADDING SCREEN: %s", screen_name)

        self.add_widget(screen_object)

        logging.info("SCREEN READY: %s", screen_name)

    def _ensure_screen_loaded(self, screen_name):
        """
        Make sure a named screen exists before ScreenManager tries
        to switch to it.
        """

        if not self.has_screen(screen_name):
            self.load_screen(screen_name)

    def push(self, screen_name, side="left"):
        """
        Lazy-load a screen, add it to navigation history, and switch to it.
        """

        if self.current != screen_name:
            self.history.append({
                "name": screen_name,
                "side": side
            })

        self._ensure_screen_loaded(screen_name)

        self.transition.direction = side
        self.current = screen_name

    def push_replacement(self, screen_name, side="left"):
        """
        Clear navigation history and switch to a screen.
        """

        self.history.clear()
        self.push(screen_name, side)

    def pop(self):
        """
        Return to the previous screen in navigation history.
        """

        if not len(self.history) > 1:
            return

        cur_side = self.history.pop()["side"]
        prev_screen = self.history[-1]

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