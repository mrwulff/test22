###cp \schedulara\.buildozer\android\platform\build-arm64-v8a_armeabi-v7a\dists\kw.schedulara\build\outputs\apk\debug\kw.schedullogara-0.1-arm64-v8a_armeabi-v7a-debug.apk /mnt/c/Users/kw/Desktop/app.apk
###
### RELEASE 10.2.2023
###
debug = False
debug_online = False
from kivy.clock import Clock
import humanize
from datetime import timedelta
from functools import partial



import logging
# from kivy.logger import Logger

if 1 == 2:
    logging.basicConfig(
        format="%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in "
        "function %(funcName)s] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
        level=logging.DEBUG,
    )


from kivy.config import Config

Config.set("kivy", "log_name", "my_file.log")

Config.set("kivy", "log_level", "info")

Config.write()


print("what")


# import logging
# logging.basicConfig(
# level=logging.INFO,
# format='%(asctime)s %(levelname)s %(threadName)s[%(thread)s] %(message)s  %(filename)s %(lineno)d')

# logging.disable(logging.ERROR)


from ast import Pass
from asyncio import queues
from kivy.utils import hex_colormap


import profile
import time
import sys
from kivy.metrics import dp
from kivy.base import ExceptionHandler, ExceptionManager

from kivy.utils import platform
from kivymd.uix.button import (
    MDFabButton,
    MDExtendedFabButton,
    MDExtendedFabButtonText,


    MDExtendedFabButtonIcon,
)
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerLabel,
    MDNavigationDrawerItem,
    MDNavigationDrawerItemLeadingIcon,
    MDNavigationDrawerItemText,
    MDNavigationDrawerItemTrailingText,
    MDNavigationDrawerDivider,
)

import libs.lib_positions
import libs.lib_readuserdata

# from kivymd.uix.list import (
# ThreeLineAvatarIconListItem,
# IconLeftWidget,
# OneLineListItem,
# )
logging.info("What")

from kivymd.uix.snackbar import (
    MDSnackbar,
    MDSnackbarSupportingText,
    MDSnackbarButtonContainer,
    MDSnackbarActionButton,
    MDSnackbarActionButtonText,
    MDSnackbarCloseButton,
    MDSnackbarText,
)
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
)


from kivymd.uix.divider import MDDivider
from kivy.uix.widget import Widget
from kivymd.uix.button import MDButton, MDButtonText


from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)

import libs.lib_new
import libs.lib_cal


class E(ExceptionHandler):
    def handle_exception(self, inst):
        # Logger.exception("Exception caught by ExceptionHandler")
        # snackbar("ERROR!  " + str(inst))
        MDSnackbar(
            MDSnackbarText(
                text=str(inst),
            ),
            MDSnackbarButtonContainer(
                MDSnackbarActionButton(
                    MDSnackbarActionButtonText(text="Action button"),
                ),
                MDSnackbarCloseButton(
                    icon="close",
                ),
                pos_hint={"center_y": 0.5},
            ),
            y=dp(24),
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

        return ExceptionManager.PASS


if debug == True:
    ExceptionManager.add_handler(E())

#
#
send_to_sentry = False
if platform != "ios" and debug == True and debug_online == True:
    import sentry_sdk

    from sentry_sdk.integrations.logging import LoggingIntegration

    f = open("secrets.txt", "r")
    for line in f.readlines():
        yo = line
    sentry_sdk.init(
        dsn=line,
        # dsn="https://531fb56e8ac34fc3a2c624cc9cb43ee7@app.glitchtip.com/4771",
        # integrations=[
        # LoggingIntegration(
        #    level = logging.INFO,           # Capture info and above as breadcrumbs (this is the default)
        #    event_level = logging.WARNING)
        # ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
tic = time.perf_counter()
from libs.uix.root import Root

ios = True
notch = True
debug = True
scale = 2
useold = False

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, Property
from kivymd.uix.boxlayout import MDBoxLayout

# from kivymd.uix.list import IRightBodyTouch, ILeftBodyTouch
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp

# from kivymd.tools.hotreload.app import MDApp


from kivy.core.window import Window
from kivy.app import App
# from kivy.config import Config

# Config.set("kivy", "log_level", "all")

# apply all these changes
# Config.write()


# from kivymd.uix.snackbar import Snackbar
# from kivymd.toast import toast
# from kivymd.uix.pickers import MDColorPicker

# from kivymd.uix.pickers import MDThemePicker
from kivymd.uix.pickers import MDTimePickerDialVertical, MDModalDatePicker

# from kivymd.uix.picker import MDDatePicker
from kivymd.uix.pickers.datepicker import MDDockedDatePicker

# from kivymd.uix.pickers import MDTimePicker
#from kivymd_extensions.sweetalert import SweetAlert

from kivy.uix.popup import Popup
from kivymd.uix.menu import MDDropdownMenu

from kivymd.uix.list import (
    #    MDListItem,
    #    TwoLineAvatarListItem,
    #    ThreeLineListItem,
    #    ThreeLineAvatarListItem,
    # )
    MDList,
    MDListItem,
    BaseListItem,
    BaseListItemText,
    BaseListItemIcon,
    MDListItemLeadingIcon,
    MDListItemTrailingIcon,
    MDListItemHeadlineText,
    MDListItemTertiaryText,
    MDListItemLeadingAvatar,
    MDListItemSupportingText,
    MDListItemTrailingCheckbox,
    MDListItemTrailingSupportingText,
)

# from kivymd.uix.expansionpanel import (
#    MDExpansionPanel,
#    MDExpansionPanelTwoLine,
#    MDExpansionPanelThreeLine,
# )


from kivy.uix.label import Label

# from kivymd.uix.datatables import MDDataTable
# from kivymd.uix.button import MDFlatButton
from kivymd.uix.segmentedbutton import MDSegmentedButton, MDSegmentedButtonItem

import datetime
import libs.lib_think as lib_think

try:
    import libs.lib_google2 as lib_google
except:
    pass


import libs.lib_google2 as lib_google

import libs.lib_readuserdata as lib_readuserdata

from kivy.uix.scatter import Scatter
from kivy.uix.image import AsyncImage


import os

os.environ["KIVY_NO_CONSOLELOG"] = "1"


import kivy

cwd = os.getcwd()
from pyparsing import ParseExpression
import webcolors

w = 1125 / 3
h = 2436 / 3

ipad = False
# ipad = False
if ipad == True:
    w = 2048 / 2
    h = 2732 / 2


# Config.set("graphics", "width", str(w))
# Config.set("graphics", "height", str(h))
if platform == "win":
    Window.size = (w, h)
# scale = 1
# if platform not in ["android", "ios"]:
#    Window.size = (320,640)

App.get_running_app()


if platform == "android":
    from kivy.config import Config

    Config.set("graphics", "fullscreen", "auto")
    Config.set("graphics", "window_state", "maximized")
    from kivy.core.window import Window

    Window.maximize()
    Config.write()
if platform == "android5":
    from kivy.config import Config

    Config.set("graphics", "fullscreen", "auto")
    # Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    # Window.size = (600,900)
    from kivy.core.window import Window

    Window.maximize()

    # Window.size = (1366, 768)
    Window.fullscreen = True
    # Config.set("graphics", "width", str(800))

    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity

    View = autoclass("android.view.View")

    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        # width,height gives false layout events, on pinch/spread
        # so use Window.width and Window.height
        if Window.width > Window.height:
            # Hide status bar
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            # Show status bar
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)


toc1 = time.perf_counter()
logging.info(str(tic - toc1) + "firsttimer")
from kivy.utils import platform
print (platform,'PLATFORM')
import urllib.request

# import storagepath

# storagepath.get_downloads_dir()

if platform == "ios":
    app = App.get_running_app()
    import ios
    from pyobjus import autoclass

    NSURL = autoclass("NSURL")
    UIApplication = autoclass("UIApplication")
    sharedApplication = UIApplication.sharedApplication()
import libs.lib_new




class AboutScreen(Screen):
    pass


class TrophyScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class SmoothLabel(Label):
    pass


class HistoryScreen(Screen):
    pass


class PayScreen(Screen):
    pass


class YourContainer(MDBoxLayout):
    adaptive_width = True
    adaptive_size = True


# class CustomOneLineListItem(MDBoxLayout, MDListItem):
#    adaptive_width = True
#    adaptive_size = True
#    # text = True
#    pass


# class MDListItem2(IRightBodyTouch, MDBoxLayout):
#    # adaptive_width = True
#    pass


class HistoryItem(Screen):
    text = StringProperty()


class AnimateMoneyScreen(Screen):
    text = StringProperty()


class PayItem(Screen):
    text = StringProperty()


class NewSlider(Screen):
    text = StringProperty()


from kivy.uix.label import Label


class MD3Card(Screen):
    text = StringProperty()


class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""

    # from datetime import datetime

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set the date_text label to today's date when useer first opens dialog box
        now = datetime.datetime.now()
        self.ids.newhours.text = now

    def show_date_picker(self):
        """Opens the date picker"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""

        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)


from kivymd.uix.card import MDCardSwipe


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty, ListProperty


class RV(RecycleView):
    rv_data_list = (
        ListProperty()
    )  # A list property is used to hold the data for the recycleview, see the kv code

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rv_data_list = [
            {"left_text": f"Left {i}", "right_text": f"Right {i}"} for i in range(2)
        ]
        # This list comprehension is used to create the data list for this simple example.
        # The data created looks like:
        # [{'left_text': 'Left 0', 'right_text': 'Right 0'}, {'left_text': 'Left 1', 'right_text': 'Right 1'},
        # {'left_text': 'Left 2', 'right_text': 'Right 2'}, {'left_text': 'Left 3'},...
        # notice the keys in the dictionary correspond to the kivy properties in the TwoButtons class.
        # The data needs to be in this kind of list of dictionary formats.  The RecycleView instances the
        # widgets, and populates them with data from this list.

    def add(self):
        l = len(self.rv_data_list)
        self.rv_data_list.extend(
            [
                {"left_text": f"Added Left {i}", "right_text": f"Added Right {i}"}
                for i in range(l, l + 1)
            ]
        )


class SwipeToDeleteItem2(Screen):
    text = StringProperty()

    def click(self, *args):
        global idex
        global mjds

        idex = self.ids.idmdlabel.text

        try:
            junk, idex = str.split(idex, "***")
            idex = int(idex)
            newxxx = xxx[idex]
        except:
            """"""
            newxxx = []
        try:
            import libs.lib_extractjson as lib_extractjson

            rate = lib_extractjson.extract_pos(App, config_file, xxx[idex][8])
            App.get_running_app().root.current_screen.ids["rate"].text = rate
        except:
            App.get_running_app().root.current_screen.ids["rate"].text = "Notes"
        from datetime import datetime

        now = datetime.now()
        try:
            import libs.lib_tinyfs as lib_tinyfs

            today, fdate = lib_tinyfs.format_text(idex, mjds, now, "info")
        except:
            pass
        if 1 == 1:
            App.get_running_app().root.current_screen.ids["date"].text = fdate
            # App.get_running_app().root.current_screen.ids['d0'].text=str(newxxx[0])
            # App.get_running_app().root.current_screen.ids['d1'].text=str(newxxx[1])
            App.get_running_app().root.current_screen.ids["jobid"].text = str(newxxx[2])
            App.get_running_app().root.current_screen.ids["show"].text = str(newxxx[3])
            App.get_running_app().root.current_screen.ids["venue"].text = str(newxxx[4])
            App.get_running_app().root.current_screen.ids["location"].text = str(
                newxxx[5]
            )
            App.get_running_app().root.current_screen.ids["client"].text = str(
                newxxx[6]
            )
            App.get_running_app().root.current_screen.ids["type"].text = str(newxxx[7])
            App.get_running_app().root.current_screen.ids["wrench"].text = str(
                newxxx[8]
            )
            App.get_running_app().root.current_screen.ids["status"].text = str(
                newxxx[10]
            )
            App.get_running_app().root.current_screen.ids["notes"].text = str(
                newxxx[11]
            )
            App.get_running_app().root.current_screen.ids["d12"].text = str(newxxx[12])
            App.get_running_app().root.current_screen.ids["d13"].text = str(newxxx[9])
            # App.get_running_app().root.current_screen.ids["d10"].text = str(newxxx[13])
            if newxxx[8] == "ME":
                App.get_running_app().root.current_screen.ids[
                    "pos"
                ].icon = "power-socket-us"
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + x["city"] + ".png"
            )
        # except:
        #    (newxxx)

        try:
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + mjds[idex]["venue"].upper() + ".png"
            )
        except:
            App.get_running_app().root.current_screen.ids["image"].source = (
                "images/" + x["city"] + ".png"
            )


class ContentNavigationDrawer(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class P(FloatLayout):
    pass


from kivymd.uix.dialog import MDDialog


class IngredientDialog(MDDialog):
    pass


# class TwoLineAvatarListItem22(TwoLineAvatarListItem):
#    icon = StringProperty("")
#    # icon2 = StringProperty("android")
#    # icon_color = Property([0, 0, 1, 0])
#    # text_color = Property("")


class Prestore(FloatLayout):
    pass


from kivymd.uix.button import MDButton

"""
class MyToggleButton(MDButton, MDToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = self.theme_cls.primary_light
"""


class MyLabel(Screen):
    def on_size(self, *args):
        self.text_size = self.size


from kivymd.uix.card import MDCard


class BlankMDCard(MDCard):
    text = StringProperty()
    text2 = StringProperty()


newcolor = (0.2, 0.2, 0.2)
x = ""
ad = ""
xxx = ""
idex = 1
browser = ""
plus_search = 0
today_index = 0
s_index = 0
pp_index = 0
cal_index = 0


class RecipeLine(MDBoxLayout):
    text = StringProperty()


class Content(MDBoxLayout):
    pass


class Content2(MDBoxLayout):
    pass


from plyer import filechooser

"""
class CountDownLbl(Label):
    angle = NumericProperty(0)
    startCount = NumericProperty(20)
    Count = NumericProperty()

    def __init__(self, **kwargs):
        super(CountDownLbl, self).__init__(**kwargs)
        Clock.schedule_once(self.set_Circle, 0.1)
        self.Count = self.startCount
        Clock.schedule_interval(lambda x: self.set_Count(), 1)

    def set_Count(self):
        self.Count = self.Count - 1

    def set_Circle(self, dt):
        self.angle = self.angle + dt * 360
        if self.angle >= 360:
            self.angle = 0
        Clock.schedule_once(self.set_Circle, 0.1)
"""

x = []
from kivymd.uix.relativelayout import MDRelativeLayout


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


from kivy.uix.bubble import Bubble


class cut_copy_paste(Bubble):
    pass


class Demo3App(MDApp):
    def restart(self, wow):
        self.root.clear_widgets()
        self.stop()
        return Demo3App().run()

    import os

    cal_width = dp(0)
    cal_height = dp(50)
    cal_font_size = 3
    cal_size_hint = (0.0, None)
    cal_bg = (0, 0, 0, 0)

    cwd = os.getcwd()

    fday = ""
    lday = ""
    date_range_pp = "All"
    date_range_search = "All"
    sort_search = "timeIn"
    sort_pp = "paydate"
    scale = 1
    reverse = True
    reverse_search = True
    sp = True

    i = 0
    logging.info(str(tic - time.perf_counter()) + "supershort")
    cspacing = 10

    mtype = "top"
    bradius = 10 * scale
    radius = 10 * scale
    cpadding = 20
    cradius = 0
    cradius4 = 0, 0, 0, 0
    c_top = 3
    sound_effects = ["Ding", "Bang", "Lol"]
    custom_range = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017]
    lunches = ["0", "1", "2", "3"]
    oth = ["8", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    # oth = ["8", "10"]
    mheight = dp(170)
    note_index = ""
    pictures = [
        "light",
        "hammer",
        "speaker",
        "bossman",
        "default",
    ]
    locations = [
        "denver",
        "dc",
        "florida",
        "georgia",
        "indiana",
        "kentucky",
        "lasvegas",
        "losangeles",
        "louisiana",
        "michigan",
        "minnesota",
        "missouri",
        "mississippi",
        "montana",
        "newmexico",
        "northerncalifornia",
        "northwest",
        "ohio",
        "reno",
        "california",
        "southcarolina",
        "tempe",
        "memphis",
        "texas",
        "tucson",
        "wisconsin",
    ]
    js = []
    pcolor = [
        "Red",
        "Pink",
        "Purple",
        # "DeepPurple",
        "Indigo",
        "Blue",
        "LightBlue",
        "Cyan",
        "Teal",
        "Green",
        "LightGreen",
        "Lime",
        "Yellow",
        # "Amber",
        "Orange",
        # "DeepOrange",
        "Brown",
        "Gray",
        "BlueGray",
    ]
    pcolor = [name_color.capitalize() for name_color in hex_colormap.keys()]

    icons_height = dp(40)
    right_hint = None, 0.9
    right_width = dp(70)
    wall = [
        "rhino.jpg",
        "Dark.jpg",
        "Light.jpg",
        "Sing.jpg",
        "schedulara.png",
        "neon.jpg",
        "neon2.jpg",
        "neon3.jpg",
        "grid.png",
    ]
    wall_index = 0
    profile = 0
    profile_data = []
    data = {
        "History": "calendar-star",
        "Paystubs": "cash-100",
        "Stats": "chart-areaspline",
        "Trophys": "trophy-award",
        # "Old_Schedule": "book-clock",
        "About": "information",
        "firedb": "database",
        # "Profile": "account-circle",
        # "Chat": "message-outline",
        "Google Cal Backup": "google-downasaur",
        "Settings": "cog-outline",
        "Backup": "test-tube",
        "animate": "test-tube-empty",
    }
    c_radius = dp(3)

    def get_dates(self, t):
        from datetime import datetime
        from dateutil.relativedelta import relativedelta

        now = datetime.now()
        if t == "All":
            date_string = "1 January, 2000"
            d = datetime.strptime(date_string, "%d %B, %Y")

            date_string = "1 January, 2099"
            now = datetime.strptime(date_string, "%d %B, %Y")
        if t == "Year":
            d = datetime.now() - relativedelta(years=1)
        if t == "YTD":
            d = datetime.now().date().replace(month=1, day=1)
            d = datetime.combine(d, datetime.min.time())
            now = datetime.now().date().replace(month=12, day=31)
            now = datetime.combine(now, datetime.min.time())
        if type(t) == int:
            d = datetime.now().date().replace(month=1, day=1, year=t)
            d = datetime.combine(d, datetime.min.time())
            now = datetime.now().date().replace(month=12, day=31, year=t)
            now = datetime.combine(now, datetime.min.time())

        # logging.info(d, type(d), now, "RETURN DATE RANGE")

        return d, now

    def close_menu(self):
        self.root.current_screen.ids.nav_drawer.set_state("close")

    def call(self, lol):
        self.root.current_screen.ids.menub.close_stack()
        if lol.icon == "cog-outline":
            self.do_settings()
        if lol.icon == "database":
            self.do_db()
        if lol.icon == "account-circle":
            self.do_profile()

        if lol.icon == "message-outline":
            self.do_chat(0)

        if lol.icon == "chart-areaspline":
            fdate, ldate = self.get_dates("YTD")
            self.do_new_stats(fdate, ldate, "YTD")
        if lol.icon == "cash-100":
            # self.do_payperiod("paydate", self.rreverse)
            self.do_payperiod_f("YTD")
        if lol.icon == "google-downasaur":
            self.do_google_cal()
        if lol.icon == "test-tube":
            self.do_gbackup()
        if lol.icon == "information":
            self.poppy("about")

        if lol.icon == "test-tube-empty":
            self.test_animate()

    def test_animate(self):
        logging.info("test animate")

    def do_restore(self, f):
        import shutil

        global x

        f2 = lib_google.search_files(ad, f)
        f3 = lib_google.download_google_drive(ad, f2)
        fw = open(ad + "/temp.zip", "wb")
        fw.write(f3)
        fw.close()
        shutil.unpack_archive(ad + "/temp.zip", ad)
        x = lib_readuserdata.readuserdata(App, ad, ios)

    def do_gbackup(self):
        os.chdir(cwd)
        self.root.push("backupgoogle")

        import libs.lib_new
        import datetime

        import humanize

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            logging.info(x["drive_id"])
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)
        l_backup = App.get_running_app().root.current_screen.ids["last_backup"]
        # l_backup.text=
        if x.get("last_backup") == None:
            l_backup.secondary_text = "Last Backup: Never"
        else:
            old_update = datetime.datetime.strptime(
                x["last_backup"], "%Y-%m-%d %H:%M:%S.%f"
            )
            now = datetime.datetime.now()
            diff2 = humanize.naturaltime(now - old_update)
            l_backup.secondary_text = "Last Backup: " + diff2
        # logging.info(x.get("last_backup"), "LAST BACKUP")

    def do_backups(self):
        import os
        import shutil
        import datetime

        global x

        bu = ["backup_checks", "backup_config", "backup_shows"]
        for i in range(len(bu)):
            if x[bu[i]]:
                if bu[i] == "backup_checks":
                    src = os.path.join(ad, "pp")
                    dest = os.path.join(ad, "backup/pp")
                    try:
                        shutil.rmtree(dest)
                    except:
                        pass
                    destination = shutil.copytree(src, dest)
                if bu[i] == "backup_shows":
                    src = os.path.join(ad, "future_shows")
                    dest = os.path.join(ad, "backup/future_shows")

                    try:
                        shutil.rmtree(dest)
                    except:
                        pass
                    destination = shutil.copytree(src, dest)
                if bu[i] == "backup_config":
                    src = os.path.join(ad, "userdata.json.txt")
                    dest = os.path.join(ad, "backup/userdata.json")
                    destination = shutil.copy2(src, dest)

        zsrc = os.path.join(ad, "backup")
        zdest = os.path.join(ad, "backup")
        shutil.make_archive(zsrc, "zip", zdest)
        import libs.lib_google2

        self.do_test_open()
        tt = libs.lib_google2.google_files(ad, "backup.zip", x["drive_id"])
        # nf = os.path.join(ad, "shows2.zip")
        # nf='C:/Users/kw/AppData/Roaming/demo3/shows2.zip'
        # shutil.make_archive(ad + "/show3", "zip", ad + "/shows")
        now = datetime.datetime.now()
        # now = humanize.naturaltime(now)
        import libs.lib_updateuserdata

        x["last_backup"] = str(now)

        libs.lib_updateuserdata.updateuser(x, ad)
        self.do_gbackup()

    def file_selection(self, selection):
        import os
        import logging as Logger

        tmp_images_path = ad
        if selection:
            path = str(selection[0])
            if not os.path.exists(tmp_images_path):
                os.makedirs(tmp_images_path)

            filename = os.path.basename(path)

            tmp_file = os.path.join(tmp_images_path, filename)
            # copyfile(path, tmp_file)

            Logger.debug(f"Image copied to tmp folder: {tmp_file}")
            Logger.debug(f"Image selected: {path}")

            logging.info(f"Temp: {tmp_file}\nReal: {path}")
            logging.info("on_image_selected", path)
        else:
            path = ""

    def find_gbackups(self):
        try:
            import libs.lib_google2 as lib_google
        except:
            return
        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            logging.info(x["drive_id"], "drive.id find_gbackups")
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)

        z = lib_google.find_backup(ad, [x["drive_id"]])
        return z

    def do_test_open(self):
        import libs.lib_new

        if x.get("drive_id") == None:
            x["drive_id"] = lib_google.search_files(ad, "Schedulara_Backups")

            logging.info(x["drive_id"])
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)
        return x

    def snackbarx(self, text1):
        MDSnackbar(
            MDSnackbarText(
                text=text1,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

    def add_google_calendar(self, y):
        import libs.lib_google2 as lib_google

        if x.get("cal_id") != None:
            lib_google.google_calendar_add(ad, y, x["cal_id"])
            # lib_google.get_calendar_service(ad)

    def find_events(self, rang):
        import libs.lib_google2 as lib_google

        z = lib_google.google_calendar_list(ad, x, True)

    def remove_google_token(self, z):
        import os

        try:
            os.remove(ad + "/" + z)
            self.snackbarx("success")
        except:
            self.snackbarx("failed to remove")

    def delete_future_shows(self):
        import libs.lib_new
        import datetime
        import json

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"]
        for show in range(len(gg)):
            z = self.filename(gg[show]) + ".json"
            # for line in x2.readlines():
            now = datetime.datetime.now()
            time = now.strftime("%m%d%Y")
            z2 = str.split(z, " ")
            z2 = z2[0]
            z2 = str.split(z2, "_")
            z2 = z2[0]

            if 1 == 1:
                date_object = datetime.datetime.strptime(z2, "%m%d%Y")
                if date_object > datetime.datetime.now():
                    x2 = ad + "/future_shows/" + self.filename(gg[show]) + ".json"
                    with open(x2) as json_file:
                        data = json.load(json_file)
                        if data.get("google_id") != None:
                            del data["google_id"]
                        data["updated"] = True
                    json_file.close()
                    data_new = json.dumps(data, indent=4)
                    nf = open(x2, "w")
                    nf.write(data_new)
                    nf.close

    def do_google_cal(self):
        import libs.lib_readuserdata
        import json

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)
        import libs.lib_google2 as lib_google
        import libs.lib_new

        # lib_google.create(ad)
        if x.get("cal_id") == None:
            x["cal_id"] = lib_google.make_user_cals(ad)
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"]
        added = 0
        found = 0
        if x.get("cal_id") != None:
            for show in range(len(gg)):
                flag = 0
                # self.snackbarx(gg[show]["show"])
                if gg[show].get("google_id") == None:
                    # lib_google.google_calendar_add(ad, gg[show], x["cal_id"])

                    x2 = open(
                        ad + "/future_shows/" + self.filename(gg[show]) + ".json",
                        "r",
                    )
                    found = found + 1
                    x2 = ad + "/future_shows/" + self.filename(gg[show]) + ".json"
                    with open(x2) as json_file:
                        data = json.load(json_file)
                        logging.info(data.get("google_id"), "lololol")
                        if data.get("google_id") != None:
                            flag == 1
                    if flag == 0:
                        try:
                            os.mkdir(ad + "/future_shows")
                        except:
                            "ok"
                        zz = lib_google.google_calendar_add(ad, gg[show], x["cal_id"])
                        gg[show]["google_id"] = zz
                        x2 = open(
                            ad + "/future_shows/" + self.filename(gg[show]) + ".json",
                            "w",
                        )

                        json_object = json.dumps(gg[show], indent=4)
                        self.snackbarx("Added " + str(added))

                        x2.write(json_object)
                        added = 1 + added

            self.snackbarx("Added " + str(added) + ", Found " + str(found))

    def filename(self, x):
        f = str.replace(x["show"], "/", "")
        f = str.replace(f, ":", "")
        f1 = str.replace(x["date"], "/", "")
        f2 = str.replace(x["time"], ":", "")
        f3 = x["job"]
        return f1 + "_" + f2 + f3 + f

    def format_date(self, d, year):
        from datetime import datetime

        if year == "short":
            d = d.strftime("%m/%d")
        if year == "full":
            d = d.strftime("%m/%d/%Y")

        return str(d)

    def do_new_stats_format(self, f):
        fdate, ldate = self.get_dates(f)
        if 1 == 1:
            self.do_new_stats(fdate, ldate, f)
        # except:
        #    logging.info("div by 0")

    def check_stats(self, li):
        # logging.info(li, "LIST OF CHECKS")
        sum2 = sum(li)
        try:
            ave = sum2 / (len(li))
        except:
            ave = -1
        return round(sum2, 2), round(ave, 2)

    future_pos = {
        "name": "Future Position",
        "file": "jason_show_cache_real.json",
        "filter": "pos",
        "id": "c6",
    }

    future_venue = {
        "name": "Future Venue",
        "file": "jason_show_cache_real.json",
        "filter": "venue",
        "id": "c7",
    }

    future_type = {
        "name": "Future Show Type",
        "file": "jason_show_cache_real.json",
        "filter": "type",
        "id": "c8",
    }
    venue_chart = {
        "name": "Venue",
        "file": "json_pps.json",
        "filter": "VENUE",
        "id": "c5",
    }
    client_chart = {
        "name": "Client",
        "file": "json_pps.json",
        "filter": "CLIENT",
        "id": "c4",
    }
    paycheck_amount_chart = {
        "name": "Paycheck Amount",
        "file": "json_pps.json",
        "filter": "PCDA",
        "id": "c3",
    }
    type_chart = {
        "name": "Type",
        "file": "json_pps.json",
        "filter": "TYPE",
        "id": "c2",
    }
    pos_chart = {
        "name": "Positions",
        "file": "json_pps.json",
        "filter": "POS",
        "id": "c1",
    }
    shift_chart = {
        "name": "Shift Length",
        "file": "json_pps.json",
        "filter": "hours",
        "id": "c9",
        "secondary": "Total Hours: ",
    }

    hours_chart = {
        "name": "Hours",
        "file": "json_pps.json",
        "filter": "tothours",
        "id": "c9",
        "secondary": "Average Hours: ",
    }

    ot_chart = {
        "name": "OT Hours",
        "file": "json_pps.json",
        "filter": "otH",
        "id": "c10",
    }

    day_chart = {
        "name": "Days",
        "file": "json_pps.json",
        "filter": "ot",
        "id": "c11",
    }

    time_chart = {
        "name": "Start Time",
        "file": "json_pps.json",
        "filter": "start",
        "id": "c12",
    }

    def do_graphOrder(self):
        self.root.push("graphOrder")
        chart_list = []
        chart_list.append(self.paycheck_amount_chart)
        chart_list.append(self.pos_chart)
        chart_list.append(self.type_chart)

        chart_list.append(self.client_chart)
        chart_list.append(self.venue_chart)
        chart_list.append(self.future_pos)
        chart_list.append(self.future_venue)
        chart_list.append(self.future_type)

        chart_list.append(self.shift_chart)
        chart_list.append(self.ot_chart)

        logging.info("graph order")
        pass

        for z in range(len(chart_list)):
            logging.info(chart_list[z])

            self.root.current_screen.ids["box"].add_widget(
                CustomOneLineListItem(
                    # MDListItem(
                    text=chart_list[z]["name"],
                    id="7",
                    # IconRightWidget="lock",
                    # bg_color=self.theme_cls.primary_dark,
                    on_release=lambda x, y=(chart_list[z]["name"],): self.view_chart(y),
                )
            )
            # logging.info(dir(self.root.current_screen.ids.values()), "icons!!!")
            logging.info(dir(self.root.current_screen.ids["container"]), "icons!!!")
            self.root.current_screen.ids["container"].icon = "account"

    def view_chart(self, y):
        logging.info("view chart y", y)

    def do_new_stats(self, fdate, ldate, rng):
        global x
        # import kivymd_extensions.akivymd
        import libs.charts

        logging.info("omg")
        # self.root.current_screen.ids["newstats"].clear_widgets()
        self.root.push("newstats")
        import libs.lib_makegraphs
        import libs.lib_parse2

        bu = ["YTD", "Year", "All", "Custom"]

        App.get_running_app().root.current_screen.ids["dstart"].text = (
            self.format_date(fdate, "full") + "     to"
        )

        App.get_running_app().root.current_screen.ids["dend"].text = self.format_date(
            ldate, "full"
        )

        libs.lib_makegraphs.make_full_json_pp(ad, fdate, ldate, False)

        chart_list = []
        chart_list.append(self.paycheck_amount_chart)
        chart_list.append(self.pos_chart)
        chart_list.append(self.type_chart)

        chart_list.append(self.client_chart)
        chart_list.append(self.venue_chart)
        chart_list.append(self.future_pos)
        chart_list.append(self.future_venue)
        chart_list.append(self.future_type)

        chart_list.append(self.shift_chart)
        chart_list.append(self.ot_chart)
        # chart_list.append(self.venue_chart)

        # chart_list.append(self.day_chart)

        # chart_list.append(self.time_chart)
        logging.info(len(chart_list), "chartlist")

        # logging.info (len(chart_list),'LENGTH OF CHART LIST')
        for i in range(len(chart_list)):
            chart = [0] * len(chart_list)
            # logging.info ("LOAD BUILDING AUTOMATIC",i,x['hidden'],chart_list[i]["name"],chart)

            if x["hidden"] == False:
                if chart_list[i]["name"] == "Shift Length":
                    logging.info("WOWOWOW2")
                    pos_k2, pos_v2, pos_v3, tot = libs.lib_parse2.load_full_pp(
                        ad, chart_list[i]["file"], chart_list[i]["filter"]
                    )
                else:
                    logging.info("nownwo")
                    pos_k2, pos_v2, pos_v3 = libs.lib_parse2.load_full_pp(
                        ad, chart_list[i]["file"], chart_list[i]["filter"]
                    )
            if x["hidden"] == True:
                # logging.info ('yahoo!')
                pos_k2 = [
                    0,
                ]
                pos_v2 = [
                    0,
                ]

            chart[i] = App.get_running_app().root.current_screen.ids[
                chart_list[i]["id"]
            ]
            # logging.info(pos_v3, "posv3")

            if chart_list[i]["name"] == "Shift Length":
                logging.info(chart_list[i]["secondary"], "SECONDARY2")
                # sec = App.get_running_app().root.current_screen.ids[chart_list[i]["id"+'d']]
                # sec.secondary_text = chart_list[i]["secondary"]
                try:
                    # logging.info(((pos_v3)), "sumsum")
                    what = "Total Hours: " + str(sum(pos_v3))
                    what2 = (sum(pos_v3)) / tot
                    what2 = f"{what2:.2f}"
                    what2 = "Total/Paycheck: " + what2
                    # logging.info(App.get_running_app().root.current_screen.ids["c9d"].secondary_text)
                    # logging.info(pos_v3, "POSV#")
                    # try:
                    #     logging.info(sum(pos_v3), "wowowowow")
                    # except:
                    #     logging.info("cant logging.info tot")
                    App.get_running_app().root.current_screen.ids[
                        chart_list[i]["id"] + "d"
                    ].secondary_text = what
                    App.get_running_app().root.current_screen.ids[
                        chart_list[i]["id"] + "d"
                    ].tertiary_text = what2
                    # logging.info (pos2,'WHATTT222')
                    # pos2='wows'
                except:
                    logging.info("why are you trying to do this")

            App.get_running_app().root.current_screen.ids[chart_list[i]["id"]].width = (
                dp(80) * len(pos_v2)
            )

            App.get_running_app().root.current_screen.ids[
                chart_list[i]["id"] + "d"
            ].text = chart_list[i]["name"]
            if 1 == 1:
                chart = [0] * len(chart_list)
                "LOAD BUILDING AUTOMATIC"
                if chart_list[i]["name"] == "Paycheck Amount":
                    pos_k2, pos_v2, pos_v3 = libs.lib_parse2.load_full_pp(
                        ad, chart_list[i]["file"], chart_list[i]["filter"]
                    )
                chart[i] = App.get_running_app().root.current_screen.ids[
                    chart_list[i]["id"]
                ]
                if x["hidden"] == True and i == 0:
                    logging.info("yahoo!", chart_list[i]["name"])
                    pos_k2 = []
                    pos_v2 = []
                chart[i].x_values = pos_v2
                chart[i].y_values = pos_v2
                chart[i].x_labels = pos_k2
                # logging.info (pos_v2,'POSV3')

                App.get_running_app().root.current_screen.ids[
                    chart_list[i]["id"] + "d"
                ].text = chart_list[i]["name"]
                try:
                    """"""
                    chart[i].update()
                except:
                    # return
                    toast("chart5 fail")
                    logging.info("chart fail")
            # except:
            # logging.info ('fail all charts')
            if chart_list[i]["name"] == "Paycheck Amount":
                check = App.get_running_app().root.current_screen.ids["c3d"]
                try:
                    ave, tot, ot2, tot2 = self.check_stats(pos_v2)
                    check.secondary_text = "Total: $" + str(self.hide(ave))
                    check.tertiary_text = "Average:  $" + str(self.hide(tot))
                except:
                    # check.text ="***HIDDEN***"
                    check.secondary_text = "***HIDDEN***"
                    logging.info("hidden***")
                check.text = "Paychecks: " + str(len(pos_v2))
            if chart_list[i]["name"] == "OT Hours":
                (
                    ave,
                    tot,
                ) = self.check_stats(pos_v2)
                check2 = App.get_running_app().root.current_screen.ids["ex3"]
                check2.secondary_text = "Total: $" + str(self.hide(ave))
                check2.tertiary_text = "Average:  $" + str(self.hide(tot))

    def add_message_to_chat(self, message):
        import libs.lib_firefriend

        import libs.lib_new

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][today_index]
        import libs.lib_firefriend

        logging.info(message, "sending message")

        libs.lib_firefriend.try_add_chat(self, gg, x, message)
        toast("Success!")
        self.do_chat(0)

    def do_chat(self, show):
        # logging.info(show)

        self.root.push("chat")
        self.root.current_screen.ids["history_list"].clear_widgets()
        # test_message = "hello w2orld with a super long random string and stuff attached to it to make it seem longer"

        import libs.lib_new
        from kivymd.uix.dialog import MDDialog as md33

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][today_index]
        import libs.lib_firefriend

        App.get_running_app().root.current_screen.ids["show_info"].text = gg["show"]
        App.get_running_app().root.current_screen.ids["show_info"].secondary_text = gg[
            "date"
        ]
        z = libs.lib_firefriend.view_chat(self, gg, x)
        # logging.info(z)

        # logging.info(gg)

        for i in range(len(z)):
            try:
                # t = z[i]["name"] + " " + z[i]["message"] + "[size=1 sp]***" + str(i)
                self.root.current_screen.ids["history_list"].add_widget(
                    ThreeLineListItem(
                        text=z[i]["message"],
                        secondary_text="[size=15dp]" + z[i]["name"],
                        tertiary_text="[size=15dp]" + z[i]["date"],
                    )
                )
            except:
                logging.info(z[i], "failure")

    def update_profile(self):
        bio = App.get_running_app().root.current_screen.ids["bio"].text
        phone = App.get_running_app().root.current_screen.ids["phone"].text
        nick = App.get_running_app().root.current_screen.ids["nick"].text
        button4 = App.get_running_app().root.current_screen.ids["button4"].text
        # logging.info(bio, phone, nick, pic)
        x["bio"] = bio
        x["phone"] = phone
        x["nick"] = nick
        x["button4"] = button4
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

        import libs.lib_firefriend

        t = libs.lib_firefriend.update_user_profile(x)
        toast(t)

    def do_profile(self):
        logging.info("profile")
        l = ["bio", "phone", "nick", "button4", "name"]
        self.root.push("profile")
        for i in range(len(l)):
            try:
                App.get_running_app().root.current_screen.ids[l[i]].text = x[l[i]]
            except:
                logging.info(x[l[i]])
        # App.get_running_app().root.current_screen.ids["phone"].text = x["phone"]
        # App.get_running_app().root.current_screen.ids["nnmae"].text = x["nname"]
        # App.get_running_app().root.current_screen.ids["button4"].text = x["button4"]
        # App.get_running_app().root.current_screen.ids["name"].text = x["name"]

    def do_db(self):
        logging.info(
            "db",
        )
        import libs.lib_fire

        libs.lib_fire.idk(App, ad, x)

    def check_att(self, b):
        global x
        global ad

        app = App.get_running_app()
        ad = app.user_data_dir
        # config_file=ad

        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        # x[b] = False
        app = App.get_running_app()
        ad = app.user_data_dir
        import libs.lib_updateuserdata

        try:
            # logging.info("already set")
            return x[b]

        except:
            # logging.info("not set yet")

            x[b] = "False"
            libs.lib_updateuserdata.updateuser(x, ad)
            return x[b]

    def check_pull_refresh(self, view, grid):
        pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.keyboard)

        # self.title = "Kivy - Lazy Load"

        # Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        # Window.softinput_mode = "below_target"

    def build(
        self,
    ):
        self.root = Root()
        self.theme_cls.theme_style_switch_animation = True
        # self.update_internal("opened", 1)

        # from kivy.config import Config

        # Config.set('graphics', 'fullscreen', 'auto')
        # Config.set('graphics', 'window_state', 'maximized')
        # Config.write()
        from kivy.core.window import Window

        # Window.maximize()
        # logging.info ('windowmax')

        # Window.size = (1366, 1366)
        # Window.fullscreen = True

        # rv = self.root.ids.rv
        # self.data = [self.create_random_input(rv, index) for index in range(20)]

        # self.root.push("home")
        # toast("lol")

        zz = False
        if 1 == 1:
            try:
                import libs.lib_readuserdata

                x = libs.lib_readuserdata.readuserdata(App, ad, ios)

                if x.get("backdoor") == False:
                    zz = False
                    logging.info("user11false")
                logging.info("good user read")
                # toast("lol")
                # toast(str(x.get("backdoor")+' test'))
                # logging.info('BACKDOOR')
            except:
                logging.info("bad user read")
                import libs.lib_makeuserdata

                libs.lib_makeuserdata.makeuserdata(App, ad, ios)

                x = libs.lib_readuserdata.readuserdata(App, ad, ios)

                
                #toast('backdoor=unknown')
                # self.snackbar = Snackbar(text="bla", bg_color=self.theme_cls.primary_color)
                # self.snackbar.open()
        logging.info(str(zz) + " BACKDOOR true or false")
        self.theme_cls.primary_palette = x["pcolor"]
        if x["theme"] == "Light":
            logging.info("switching to light mode")
        else:
            self.theme_cls.switch_theme()
        # if zz == True:
        if 1 == 2:
            self.data.update(
                {
                    "Backup": [
                        "backup-restore",
                        "on_press",
                        lambda x: logging.info("backup"),
                        "on_release",
                        lambda x: self.do_gbackup(),
                    ]
                }
            )
            self.data.update(
                {
                    "Export": [
                        "calendar-export",
                        "on_press",
                        lambda x: logging.info("export"),
                        "on_release",
                        lambda x: self.do_google_cal(),
                    ]
                }
            )
            self.data.update(
                {
                    "Search": [
                        "magnify",
                        "on_press",
                        lambda x: logging.info("export"),
                        "on_release",
                        lambda x: self.new_search(),
                    ]
                }
            )
            # self.data.update({'Add Event': ['calendar-plus',"on_press", lambda x: logging.info("export"),"on_release", lambda x: self.add_event()]})
        if 1 == 2:
            self.data.update(
                {
                    "DEV": [
                        "debug",
                        "debug",
                        lambda x: logging.info("debug"),
                        "on_release",
                        lambda x: self.do_dev(),
                    ]
                }
            )
            self.data.update(
                {
                    "delete future": [
                        "debug",
                        "debug",
                        lambda x: logging.info("debug"),
                        "on_release",
                        lambda x: self.delete_future_shows(),
                    ]
                }
            )

        # fdate, ldate = self.get_dates("YTD")
        #            self.do_new_stats(fdate, ldate, "YTD")
        self.today()

    def keyboard(self, window, key, *args):
        if key == 27:
            self.root.push("today")
            return True  # key event consumed by app
        else:
            return False  # key event passed to Android

    def dev(self, x):
        if x == "zero":
            toast("divide by zero GO")
            z = 1 / 0
        if x == "webview":
            toast("webview")
            import libs.lib_custom_views

            x = libs.lib_custom_views.webviews(App, ad, ios, self)
            toast(x)

    def add_event(self):
        logging.info("add_event")
        self.root.push("add_user_show")

    def new_search_bad(self):
        # content_cls=Content(),
        button_ok = MDButton(
            text="what!", font_size=16, on_release=self.logging.info_street2
        )

        self.alert = SweetAlert()
        self.alert.fire(
            input="Input Email",
            buttons=[button_ok],
        )

    def rate_input(self):
        # THIS ONE WORKS!!! OMG
        from kivymd.uix.button import MDIconButton

        toast("Input Rate")
        if not self.dialog:
            self.dialog = MDDialog(
                title="Rate for :",
                type="custom",
                # type="simple",
                content_cls=Content(),
                height=0.5,
                buttons=[
                    MDIconButton(
                        icon="magnify",
                        on_press=self.update_rates,
                    ),
                ],
            )
        self.dialog.open()

        self.set_rate()

    def do_dev(self):
        logging.info("DEV MODE SCREEN")
        self.root.push("dev")

    def do_backdoor(self):
        # logging.info ('bla')
        # toast("bla")
        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        if x.get("demo_count") == None:
            x["demo_count"] = 1
        if type(x.get("demo_count")) == int:
            x["demo_count"] = x["demo_count"] + 1
        if x["demo_count"] == 2:
            self.do_dev()

        if x["demo_count"] == 5:
            self.snackbarx("almost there")
        if x["demo_count"] == 10:
            self.snackbarx("dev mode enabled")
            x["backdoor"] = True
        if x["demo_count"] > 10:
            x["backdoor"] = False
            x["demo_count"] = 1
            self.snackbarx("dev mode disabled")
        logging.info("backdoor: " + x["backdoor"])

        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    def update_rates(self, btn):
        import libs.lib_new

        xx9 = libs.lib_new.just_get_json_schedule(x, ad)

        show = xx9["shows"][idex]
        pos = show["pos"]
        sho = show["date"]
        logging.info(sho, "SHOWEEEEEE,", sho)

        street_name = self.dialog.content_cls.ids.street.text
        logging.info(street_name)

        self.dialog.dismiss()

        App.get_running_app().root.current_screen.ids["moneyinfo"].text = street_name
        pos = App.get_running_app().root.current_screen.ids["moneyinfo"].secondary_text
        pos = str.split(pos, " ")
        # App.get_running_app().root.current_screen.ids["moneyinfordeszxdfxzs"].text="POO"
        # self.root.get_screen("animate").ids["moneyinfo"].text='str(v)'
        # logging.info (App.get_running_app().root.current_screen.ids["moneyinfo"].text)
        import libs.lib_makeuserdata as lib_makeuserdata

        lib_makeuserdata.makeratefile(ad, street_name, pos[0])

    def new_search(self):
        # THIS ONE WORKS!!! OMG
        from kivymd.uix.button import MDIconButton

        self.snackbarx("Search Page")
        if not self.dialog:
            self.dialog = MDDialog(
                title="Search Shows:",
                type="custom",
                # type="simple",
                content_cls=Content(),
                height=0.5,
                buttons=[
                    MDIconButton(
                        icon="magnify",
                        on_press=self.display_search,
                    ),
                ],
            )
        self.dialog.open()

    def display_search(self, btn):
        import libs.lib_archive as lib_archive
        import libs.lib_makegraphs as lib_makegraphs

        ###works
        street_name = self.dialog.content_cls.ids.street.text
        # street_name="VGK"
        logging.info(street_name)
        self.dialog.dismiss()
        self.root.push("newsearch")

        lib_makegraphs.make_full_json_pp(ad, "fdate", "ldate", True)
        # datadir and start and end and term,strict
        success, a, b, gigs = lib_archive.load_archive(
            ad, "False", "False", street_name, False
        )

        from kivymd.uix.list import ThreeLineListItem

        ssort = self.sort_search
        reverse_search = self.reverse_search
        # logging.info(rreverse, "REVERSE")

        self.root.current_screen.ids["search_list"].clear_widgets()
        listofdicks = success
        #### SORT!!!!
        listofdicks = sorted(
            listofdicks, key=lambda i: i[ssort], reverse=reverse_search
        )
        logging.info(ssort, reverse_search, "SSORT WTF MAN")

        bu = ["YTD", "Year", "All", "Custom"]
        bu2 = ["timeIn", "Total", "tot_hours"]
        """
        for i in range(len(bu)):
            if self.date_range_pp == bu[i]:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_dark
            else:
                App.get_running_app().root.current_screen.ids[
                    bu[i]
                ].md_bg_color = self.theme_cls.primary_light
        """
        for i in range(len(bu2)):
            if ssort == bu2[i]:
                App.get_running_app().root.current_screen.ids[
                    bu2[i]
                ].md_bg_color = self.theme_cls.primary_dark
            else:
                App.get_running_app().root.current_screen.ids[
                    bu2[i]
                ].md_bg_color = self.theme_cls.primary_light
        if reverse_search == False:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-descending"
        else:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-ascending"
        """       
        App.get_running_app().root.current_screen.ids["dstart"].text = (
            self.format_date(self.fday, "full") + "     to"
        )

        App.get_running_app().root.current_screen.ids["dend"].text = self.format_date(
            self.lday, "full"
        )
        """

        panel = ThreeLineListItem(
            text="Shows: " + str(gigs),
            secondary_text="Earnings: " + str(self.hide(self.format_money(b))),
            tertiary_text="Hours: " + str(a),
            bg_color=self.theme_cls.bg_dark,
            radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
        )
        self.root.get_screen("newsearch").ids.search_list.add_widget(panel)

        for z in range(len(listofdicks)):
            # logging.info(listofdicks[z])
            time = listofdicks[z]["timeIn"]
            date, time = str.split(time, " ")

            panel = ThreeLineListItem(
                text="Show: " + str(listofdicks[z]["show"]),
                secondary_text="Date: "
                + str(date)
                + " Hours: "
                + str(listofdicks[z]["tot_hours"])
                + " Overtime: "
                + str(listofdicks[z]["otH"]),
                tertiary_text="$"
                + str(self.hide(self.format_money(listofdicks[z]["Total"]))),
                bg_color=self.theme_cls.bg_dark,
                radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
                # on_release=self.do_pay_ind,
            )

            self.root.get_screen("newsearch").ids.search_list.add_widget(panel, z)

    def format_money(self, z):
        import locale

        locale.setlocale(locale.LC_ALL, "")
        try:
            return locale.currency(z, grouping=True)
        except:
            return z

    def hide(self, y):
        # global x
        # toast (x['hidden'],'hidden?')
        try:
            if x["hidden"] == True:
                # toast('hiding stuff')
                return "***"
        except:
            """"""
            # return str(y)
        return str(y)

    def junk2(self, a):
        logging.info("junk2", a)
        z = self.alert.content_cls.ids
        logging.info(z)

    def get_data(self, instance_btn, content_cls):
        tf = content_cls.ids
        logging.info(tf)
        # logging.info ('bla',junk.text,dir(junk))
        # jp=junk.parent

        # logging.info(dir(self.alert))
        # logging.info (self.alert.children,'text')
        # logging.info (dir(self.alert.children),'text')
        # logging.info (self.alert.ids['text'].input)
        # logging.info (self.alert.ids)

    def prep_stats(self):
        fdate, ldate = self.get_dates("YTD")
        if 1 == 1:
            self.do_new_stats(fdate, ldate, "YTD")
        # except:
        #    ''

    def delete_show(self):
        z = App.get_running_app().root.current_screen.ids["rat"].text
        logging.info("DELETE SHOW", z)

        import libs.lib_new

        try:
            show, f = libs.lib_new.load_archive_json(ad, z)
            self.snackbarx("Delete Show")
        except:
            logging.info("old show data")
            self.snackbarx("failed to find show")
            return
        logging.info(f, "DELETESHOW DATA?")
        import os

        os.remove(f)
        self.show_archive()

    import libs.lib_updateuserdata

    def save_current_screen2(self, t):
        logging.info(x, "TV")
        x["current"] = t
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

        # libs.lib_updateuserdata.updateuser(x, ad)
        logging.info("what in the hell")
        return "wow"

    def on_start2(self):
        global x
        global ad
        app = App.get_running_app()
        ad = app.user_data_dir

        if 1 == 1:
            config_file = ad
        logging.info(str(tic - time.perf_counter()) + "on start !!!")
        import libs.lib_readuserdata

        try:
            x = libs.lib_readuserdata.readuserdata(App, config_file, ios)
            logging.info("read user data at begining")
        except:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata(App, config_file, ios)
            x = libs.lib_readuserdata.readuserdata(App, config_file, ios)
            logging.info("made user data at begining!!!!!")
        if 1 == 1:
            # try:
            self.theme_cls.theme_style = x["theme"]
            self.theme_cls.primary_palette = x["pcolor"]
            # self.theme_cls.accent_palette = x["scolor"]
            self.theme_cls.material_style = "M3"
        # except:
        #    pass
        # logging.info(x, "lol")

        # self.do_login("", useold)
        x1 = self.theme_cls.theme_style
        x2 = self.theme_cls.primary_palette
        # x3 = self.theme_cls.accent_palette
        # x4 = self.theme_cls.material_style
        self.theme_cls.update_theme_colors()

        import subprocess

        try:
            asdf = (
                subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
                .decode("ascii")
                .strip()
            )
        except:
            asdf = "1.1"
        logging.info(asdf)

        if 1 == 1:
            if x["today_start"] == False:
                logging.info("oldstart1!!!")
                # self.newstart("", useold)

            if x["today_start"] == True:
                # toast("Success " + asdf)
                logging.info("newstart!@!")
                # self.today()
                # self.md2()
        # except:
        #    self.today()

    def md2(self):
        self.root.push("md2")
        logging.info("md2")

    def callback(self, instance_button):
        logging.info(
            self.alert,
        )
        b = instance_button.text
        nb = int(b[-1])
        self.alert.dismiss()
        if nb < 2:
            self.do_onboarding(nb + 1)
        if nb == 9:
            self.alert.dismiss()
        if nb == 8:
            self.alert.dismiss()
            self.root.push("login")

    def pre_login(self):
        self.menu3.dismiss()
        self.root.push("login")

    def do_onboarding(self, i):
        legal = "While Schedulara is designed to help you stay organized and manage your schedule, we are not responsible for any missed gigs, or other issues that may arise. It is ultimately your responsibility to ensure that you are available for events and to communicate any scheduling conflicts to your team. Use our app at your own risk."
        ee = "wat"
        # legal=legal*5
        gg = "what2"
        self.menu3 = MDDialog(
            # type=simple,
            # ----------------------------Icon-----------------------------
            # MDDialogIcon(
            #    icon=self.find_type(d, "type"),
            # ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Welcome to Schedulara",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="created by Kevin Wulff",
            ),
            MDDialogSupportingText(
                text="@kevlights",
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDTextField(text=legal, multiline=True),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                # MDFabButton(icon="arrow-right-bold", style="small"),
                MDExtendedFabButton(
                    MDExtendedFabButtonText(
                        text="Accept and Continue",
                    ),
                    # MDExtendedFabButtonIcon(
                    #    icon="check-circle",
                    # ),
                    # style="small",
                    # icon="content-copy",
                    # text='View Demo',
                    # MDExtendedFabButtonText(text=)
                    on_release=lambda x, y=(ee): self.pre_login(),
                ),
                MDExtendedFabButton(
                    MDExtendedFabButtonText(
                        text="Demo",
                    ),
                    # icon="close-box",
                    style="small",
                    # text='Accept and Continue',
                    on_release=lambda x, y=(gg): self.menu3.dismiss(),
                ),
                spacing="20dp",
                # cent2er=(50, 0),
                right=False,
                size_hint=(None, None),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                center_y=2100,
            ),
            # -------------------------------------------------------------
        )

        App.get_running_app().root.current_screen.ids["test2"] = self.menu3
        self.menu3.open()

    def do_onboarding2(self, i):
        welcome = "Welcome to our Schedulara! Manage your schedule with ease and view upcoming events Let's get started!"
        demo = """To get started, please select one of the following options:

Login: If you already have an account, please click this button to log in and access your schedule.

Demo: If you are new to our app or would like to see how it works, click this button to access the demo mode. Please note that demo mode is for testing purposes only and does not reflect real event schedules."""
        s = "[size=15dp]"
        title = ["Welcome", "Legal:", "Extras:"]
        text = [
            s + welcome,
            s + legal,
            s + demo,
        ]
        b_b = s + "Next", s + "Next", s + "Login"
        b_b2 = s + "Skip", s + "Skip", s + "Demo"

        button_ok = MDButton(
            text=b_b[i] + "[size=0]" + str(i),
            font_size=dp(16),
            on_release=self.callback,
        )
        button_cancel = MDButton(
            text=b_b2[i] + "[size=0]" + "9",
            font_size=dp(16),
            on_release=self.callback,
        )
        button_login = MDButton(
            # text=b_b[i] + "[size=0]" + "8",
            text="Login" + "[size=0]" + "8",
            font_size=dp(16),
            on_release=self.callback,
        )
        bb = (
            [button_ok, button_cancel, button_login],
            [button_ok, button_cancel],
            [button_login, button_cancel],
        )
        self.alert = SweetAlert()
        # self.alert.fire(title[i], text[i], buttons=bb[i])
        return True

    def soon(self, b):
        toast("Coming Soon!")
        logging.info(b)

    def show_profile(self, name, d, zzl, i):
        from kivymd.uix.dialog import MDDialog as md33
        import libs.lib_firefriend

        cat = "nothing"
        r = "what is r"

        # gg=str(name)

        self.dialog_name = [0] * (int(zzl) + 1)
        # for q in range(len(profile)):
        #    logging.info(profile[q]["name"], q)
        # logging.info(profile[i]["name"], name, i, "why")
        # logging.info(profile[i], "what emails bitch")
        pro = libs.lib_firefriend.get_profile(profile[i]["Email"])
        # logging.info(pro)
        # pro.value
        # (name2) = pro.items()
        # logging.info(
        #    name2,
        # )
        try:
            for key, value in pro.items():
                logging.info(key, value)
            prof = (
                "[size=30]"
                + key
                + "\n[/size]"
                + value["City"]
                + "\n"
                + value["NickName"]
                + "\n"
                + value["Phone"]
                + "\n"
                + value["bio"]
            )
        except:
            logging.info(profile[i])
            prof = profile[i]["name"]
            toast("profile not found :(")

        # logging.info(i, zzl, self.dialog_name, "WHATTTTT")
        if not self.dialog_name[i]:
            self.dialog_name[i] = md33(
                text=str(prof),
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Add Friend",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                    MDFlatButton(
                        text="Hide",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                    MDFlatButton(
                        text="Block",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.soon,
                    ),
                ],
            )

        self.dialog_name[i].open()

    def print_id(
        self,
        a,
        b,
    ):
        # logging.info("bla", type(a), type(b), "\nblabla")
        # logging.info(a, b.index)

        # logging.info("bla222", (data), (b), "\nblabla222")
        name = a.row_data
        name = name[0]
        # logging.info(name)
        # logging.info(dir(b))
        # logging.info("OMG")
        zz = int(b.index) / 5
        zzl = zz * 5
        zz = str(zz)
        # logging.info(zz, "zzzzzz")
        i, r = str.split(zz, ".")
        i = int(i)
        name = name[i * 5]
        self.show_profile(name, 1, zzl, i)

    def check_in(self, gg):
        global profile
        global profile_data
        # logging.info(gg, x)
        self.dialog_close()
        #
        self.root.push("checkin")
        self.root.current_screen.ids["check_id"].clear_widgets()

        import libs.lib_firefriend

        names, t, d = libs.lib_firefriend.try_add_show(App, gg, x)
        toast(t)
        profile = d
        # logging.info(profile, "WHY YOU SUCK)")
        """
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        names = libs.lib_firefriend.add_show(App, gg, x)
        """
        # logging.info(names)

        tables = MDDataTable(
            # size_hint=(0.9, 0.6),
            #
            # background_color_selected_cell=self.theme_cls.primary_light,
            column_data=[
                ("Name", dp(20)),
                ("Pos", dp(20)),
                ("Time", dp(20)),
                ("Stamp", dp(10)),
                ("Type", dp(20)),
            ],
            row_data=[
                names
                # "a","b","c"
                # The number of elements must match the length
                # of the `column_data` list.
            ],
        )
        tables.bind(on_row_press=self.logging.info_id)
        # tables.bind(lambda x, y=d,: self.logging.info_id(y))
        # tables.bind(
        #    on_row_press=(
        #        lambda x, y=(
        #            "x",
        #            "x",
        #            d,
        #        ): self.logging.info_id(names, tables, d)
        #    )
        # )

        # (lambda x, y=d,: self.logging.info_id(y))
        self.root.current_screen.ids["check_id"].add_widget(tables)

    def click_cal(self, info, js):
        self.pop_new([info, js])
        """
        logging.info(type(info), info, "infooooo")
        logging.info(js[info], "full thingy", str(js[info]["date"]))
        title5 = js[info]["show"]
        text55 = (
            str(js[info]["date"])
            + " "
            + str(js[info]["time"])
            + "\n\n"
            + str(js[info]["status"])
            + "   "
            + str(js[info]["pos"])
            + "   "
            + str(js[info]["type"])
            + "\n"
            + str(js[info]["venue"])
            + "\n"
            + str(js[info]["location"])
            + "\n"
            + "\n"
            + str(js[info]["job"])
            + "\n"
            + str(js[info]["client"])
            + "\n\n"
            + str(js[info]["notes"])
        )

        # self.alert2 = SweetAlert()
        # self.alert2.fire(
        #    title5,
        #    text55,
        #    buttons=([button_ok]),
        # )
        i = 0
        welcome = "welcome"
        legal = "bla"
        demo = "demo"
        s = "[size=19dp]"
        title = [title5, "Legal:", "Extras:"]
        text = [
            s + text55,
            s + legal,
            s + demo,
        ]
        b_b = s + "Previous", s + "2", s + "3"
        b_b2 = s + "Close", s + "5", s + "6"

        button_ok = MDButton(
            text=b_b[i] + "[size=0]###" + str(int(info) - 1),
            # theme_font_size=dp(16),
            on_release=self.cal_next,
        )
        button_cancel = MDButton(
            text=b_b2[i] + "[size=0]" + str(int(info) - 1),
            # theme_font_size=dp(16),
            on_release=self.cal_close,
        )

        button_login = MDButton(
            # text=b_b[i] + "[size=0]" + str(int(info-1)),
            text="Next" + "[size=0]###" + str(int(info) + 1),
            # theme_font_size=dp(16),
            on_release=self.cal_next,
        )

        bb = ([button_ok, button_cancel, button_login],)
        # self.alert = SweetAlert()
        # self.alert.window_control_buttons = "close"
        # self.alert.fire(title[i], text[i], buttons=bb[i])

        MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="refresh",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Reset settings?",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="This will reset your app preferences back to their "
                "default settings. The following accounts will also "
                "be signed out:",
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="gmail",
                    ),
                    MDListItemSupportingText(
                        text="KivyMD-library@yandex.com",
                    ),
                    theme_bg_color="Primary",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon="gmail",
                    ),
                    MDListItemSupportingText(
                        text="kivydevelopment@gmail.com",
                    ),
                    theme_bg_color="Primary",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Cancel"),
                    theme_text_color="Hint",
                    md_bg_color=self.theme_cls.transparentColor,
                    style="text",
                ),
                MDButton(
                    MDButtonText(text="Accept"),
                    style="text",
                ),
                spacing="8dp",
            ),
            # -------------------------------------------------------------
        ).open()

        return True
        """

    def pop_new(self, d):
        global today_index
        today_index = d

        import libs.lib_new
        import libs.lib_makeuserdata

        from kivymd.uix.dialog import MDDialog as md33

        import libs.lib_positions

        if isinstance(d, str):
            logging.info(d, "this is ddd")
            junk, d = str.split(d, "#####")
            d = int(d)
        if isinstance(d, list):
            gg = d[1][d[0]]
            d = d[0]
        else:
            js = libs.lib_new.get_json_schedule_1(x, ad)
            gg = js["shows"][d]

        pos = libs.lib_positions.get_position_name(ad, gg["pos"])
        # type = libs.lib_positions.get_position_name(ad, gg["type"])
        logging.info
        self.find_type(d, "type")

        self.menu = MDDialog(
            # type=simple,
            # ----------------------------Icon-----------------------------
            # MDDialogIcon(
            #    icon=self.find_type(d, "type"),
            # ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text=gg["show"],
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text=gg["date"],
            ),
            MDDialogSupportingText(
                text=gg["time"],
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon=self.find_type(d, "type"),
                    ),
                    MDListItemSupportingText(
                        text=gg["venue"],
                    ),
                    MDListItemSupportingText(
                        text=gg["location"],
                    ),
                    MDListItemSupportingText(
                        text=gg["job"],
                    ),
                    MDListItemLeadingIcon(
                        icon=self.find_type(d, "pos"),
                        theme_bg_color="Primary",
                    ),
                    md_bg_color=self.theme_cls.primaryColor,
                ),
                MDListItem(
                    MDListItemLeadingIcon(
                        icon=self.find_type(d, "pos"),
                    ),
                    MDListItemSupportingText(
                        text=gg["status"],
                    ),
                    MDListItemSupportingText(
                        text=gg["client"],
                    ),
                    MDListItemSupportingText(
                        text=gg["type"] + " " + pos,
                    ),
                    theme_bg_color="Primary",
                    # md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                MDTextField(text=gg["notes"], multiline=True),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                # MDFabButton(icon="arrow-right-bold", style="small"),
                MDFabButton(
                    style="small",
                    icon="arrow-left-bold",
                    on_release=lambda x, y=(gg): self.cal_next(d - 1),
                ),
                MDFabButton(
                    icon="content-save",
                    style="small",
                    on_release=lambda x, y=(gg): self.edit_show_details(gg),
                ),
                MDFabButton(
                    style="small",
                    icon="microsoft-xbox-controller-menu",
                    on_release=lambda x, y=(gg): self.open_menu("item", gg),
                ),
                MDFabButton(
                    icon="close-box",
                    style="small",
                    on_release=lambda x, y=(gg): self.menu.dismiss(),
                ),
                MDFabButton(
                    icon="arrow-right-bold",
                    style="small",
                    on_release=lambda x, y=(gg): self.cal_next(d + 1),
                ),
                spacing="20dp",
                # cent2er=(50, 0),
                right=False,
                size_hint=(None, None),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                center_y=2100,
            ),
            # -------------------------------------------------------------
        )

        App.get_running_app().root.current_screen.ids["test"] = self.menu
        self.menu.open()

    def pop_new2(self, d):
        logging.info("pop_new")
        global today_index
        today_index = d

        import libs.lib_new
        import libs.lib_makeuserdata

        from kivymd.uix.dialog import MDDialog as md33

        js = libs.lib_new.get_json_schedule_1(x, ad)
        gg = js["shows"][d]
        # logging.info(gg)
        ngg = (
            gg["show"]
            + "\n"
            + gg["date"]
            + " "
            + gg["time"]
            + " "
            + gg["pos"]
            + "\n"
            + gg["venue"]
            + ""
            + gg["location"]
            + "\n"
            + gg["client"]
            + "\n"
            + gg["status"]
        )
        libs.lib_makeuserdata.makeshowfile(App, gg, ad, False)
        cat = "nothing"
        r = "what is r"
        if not self.dialog2[d]:
            self.dialog2[d] = md33(
                text=str(ngg),
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    # MDFlatButton(
                    #    text="Save Time",
                    #    theme_text_color="Custom",
                    #    text_color=self.theme_cls.primary_color,
                    #    on_release=lambda x, y=(gg): self.add_google_calendar(y),
                    # ),
                    # MDFlatButton(
                    #    text="$",
                    #    theme_text_color="Custom",
                    #    text_color=self.theme_cls.primary_color,
                    #    on_release=lambda x, y=(cat, r, d): self.animate_money_new(y),
                    # ),
                ],
            )

        self.dialog2[d].open()

    def ampm(self, z):
        h, m = str.split(z, ":")
        h = int(h)
        # logging.info(h)
        ppp = " AM"
        h2 = h
        if h == 12 and m == "00":
            ppp = " Noon"

        if h == 24 and m == "00":
            ppp = " Midnight"

        if h > 12:
            h2 = h2 - 12
            ppp = " PM"
        if x["twenty"] == False:
            ntime = str(h2) + ":" + m + "[sup]" + ppp
        if x["twenty"] == True:
            ntime = str(z)
        return ntime

    def build_full_pp(self):
        import json

        toc5 = time.perf_counter()

        import libs.lib_makegraphs as lib_makegraphs
        import libs.lib_parse2

        try:
            with open(ad + "/" + "full_pp.json") as json_file:
                data = json.load(json_file)
        except:
            lib_makegraphs.make_full_json_pp(ad, "fdate", "ldate", True)
        logging.info("build_full_pp")
        toc6 = time.perf_counter()
        t = toc6 - toc5
        # toast(str(round(t, 2)))
        data = libs.lib_parse2.load_full_pp(ad, "full_pp.json", "p_rate")
        logging.info(len(data["shows"]), "mother of data")
        pay_checks = data["shows"]
        tot = 0
        with open(ad + "/position_list.json", "r") as json_file:
            real_list = json.load(json_file)
        real_list_values = real_list["positions"]
        json_file.close()
        for x in range(len(pay_checks)):
            gigs = pay_checks[x]["gigs"]
            # logging.info(gigs,"paychecks sub x",)
            for y in range(len(gigs)):
                # logging.info(gigs[y]["Rate"], gigs[y]["pos"], "gigs")
                tot = tot + 1
                logging.info(len(real_list_values), "realvalues")
                for z in range(len(real_list_values)):
                    # logging.info(real_list_values[z])
                    if real_list_values[z]["abv"] == gigs[y]["pos"]:
                        if real_list_values[z].get("rate") == None:
                            real_list_values[z]["rate"] = 0

                        if gigs[y]["Rate"] > real_list_values[z]["rate"]:
                            real_list_values[z]["rate"] = gigs[y]["Rate"]
        with open(ad + "/position_list.json", "w") as outfile:
            json.dump(real_list, outfile)
        outfile.close()
        logging.info(tot, "tot gigs")

    def find_type(self, a, b):
        import libs.lib_new

        # z=self.root.get_screen("today").ids["first"].text
        js = libs.lib_new.get_json_schedule(x, ad)
        try:
            icon = js["shows"][a][b]
        except:
            return "help"
        # if icon == "IN":
        #    return 'alpha-i'

        icons = libs.lib_positions.get_positions(ad, "")

        # logging.info(icon, "newICON")
        for xx in range(len(icons)):
            if icons[xx]["abv"] == icon:
                return icons[xx]["icon"]
        return "help"

    def piplist(self):
        import pkg_resources

        x = pkg_resources.get_distribution("kivymd").version
        # logging.info(x, "listofkivymd")

        y = pkg_resources.get_distribution("kivy").version
        # logging.info(y, "listofkivy")
        return x, y

    def today(self):
        
        
        import libs.lib_new
        import libs.lib_think

        self.on_start2()

        # toast("today")
        p = self.piplist()

        # toast(str(p))
        # logging.info(str(p), "piplistggggg")

        #  libs.lib_think.login_basic(ad, x, App)

        # self.update_internal("opened", 1)

        
        try:
            self.root.current_screen.ids["drawer"].clear_widgets()
        except:
            print ('cant reset')
        self.root.push("today")
        self.root.get_screen("today").ids["pic"].source = self.get_wall("theme")

        #####hustle error checks
        # logging.info(x, "this is xxx")
        if 1 == 1:
            js = libs.lib_new.get_json_schedule(x, ad)
        # logging.info("js,wtfiswrong", js)
        # except:

        self.root.get_screen("today").ids["pay1"].text = "blue"
        self.root.get_screen("today").ids["pay2"].text = "green"
        self.root.get_screen("today").ids["pay3"].text = "red"

        #    toast("login failed5")
        #    return "fail"
        
        shows = js["shows"]
        li = ["first", "second", "third"]
        li_r = ["1r", "2r", "3r"]
        li_l = ["1l", "2l", "3l"]

        ns = 3
        if len(shows) < 3:
            ns = len(shows)
        for i in range(ns):
            show_date = datetime.datetime.strptime(shows[i]["date"], "%m/%d/%Y")
            show_date = show_date.strftime("%A, %m/%d")
            z = shows[i]["time"]
            ntime = self.ampm(z)
            fvenue = shows[i]["venue"]
            if "las vegas" in fvenue:
                fvenue = str.split(fvenue, "las vegas")

            color = ""
            if shows[i]["canceled"] == True:
                color = "[color=#ff0000]"
            # color = "[color=#ff000055]"
            self.root.get_screen("today").ids[li[i] + "1"].text = (
                color + show_date + " " + ntime
            )
            self.root.get_screen("today").ids[li[i]].text = (
                color + show_date + " " + ntime
            )
            # logging.info(li[i] + str(i + 1), "thisistheid")
            self.root.get_screen("today").ids[li[i] + "2"].text = (
                color + shows[i]["show"]
            )
            self.root.get_screen("today").ids[li[i] + "3"].text = color + fvenue[0]
            self.root.get_screen("today").ids[li[i]].text_color = "Blue"
            z44 = dir(self.root.get_screen("today").ids[li_l[i]])
            self.root.get_screen("today").ids[li_l[i]].icon = self.find_type(i, "type")
            self.root.get_screen("today").ids[li_r[i]].icon = self.find_type(i, "pos")
            # logging.info(z44, "leftwidget")
            fff = self.root.get_screen("today").ids[li[i]].children
            # logging.info(fff, dir(fff), "FFFFFFFF")
            # fff.MDListItemSupportingText.text = "wowwwww"
            # self.root.get_screen("today").ids["first1"].text = ntime
            # self.root.get_screen("today").ids["first2"].text = ntime
            # elf.root.get_screen("today").ids["first3"].text = ntime
        qq = self.root.get_screen("today").ids

        # qq.branding_f.source = "images/logo/logo2.png"
        try:
            if x["branding"] == True:
                qq.branding_f.source = "images/logo/logo.png"

                # qq.name2.text='Schedulara'
                # qq.name2.secondary_text='Schedulara'
                pass
        except:
            qq.branding_f.source = "images/logo/logo2.png"
            # qq.name3.text = "Schedulara"
            logging.info("sch5")
        qq.branding_f.source = "images/logo/logo.png"
        # if x['branding']== False:
        #    qq.name2.text="NOOOOOO"
        # logging.info(qq, "BRANDING")
        numshows = len(shows)
        numconf = js["num_shows"]
        confirmable = numshows - numconf
        # if 1==1:
        print (len(shows),type(shows),'jsshows')
        update = js["updated"]

        old_update = datetime.datetime.strptime(update, "%Y-%m-%d %H:%M:%S.%f")
        now = datetime.datetime.now()
        diff2 = humanize.naturaltime(now - old_update)
        next_show = shows[0]["date"] + " " + shows[0]["time"]
        next_show = datetime.datetime.strptime(next_show, "%m/%d/%Y %H:%M")
        bb = 0
        nns = now - next_show
        # logging.info('asdfasdf',nns,type(nns),shows)

        while (nns) >= timedelta(0):
            next_show = shows[bb]["date"] + " " + shows[bb]["time"]
            next_show = datetime.datetime.strptime(next_show, "%m/%d/%Y %H:%M")
            nns = now - next_show

            bb = bb + 1
        diff3 = humanize.naturaltime(now - next_show)
        if 1==1:
            #diff3,diff2=self.check_update(shows,js)

            

            # except:
            #    diff2 = ""
            #    diff3 = ""
            # logging.info(diff2)

            if numconf == 0:
                stat_text = str(numshows) + " Confirmed"
            if numconf == 1:
                stat_text = str(numconf) + " Show Confirmable.  Click To Confirm"
            if numconf > 1:
                stat_text = str(numconf) + " Shows Confirmable.  Click To Confrim All"
            stat_text2 = "Next show in " + diff3
            stat_text3 = "Last updated " + diff2

            self.root.get_screen("today").ids["s1"].text = stat_text

            self.root.get_screen("today").ids["s2"].text = stat_text2
            self.root.get_screen("today").ids["s3"].text = stat_text3

            self.update_today_pp(pp_index)

            paydate, payperiod = self.find_pay_date(pp_index)

            paylist = self.root.get_screen("today").ids["pay1"]
            paylist.text = "Payday:  " + paydate

        if 1==2:
            self.snackbarx("failed to get times")
            logging.info("failed to get times")
            self.root.get_screen("today").ids["stats"].text = "Invalid Show Data. "
            self.root.get_screen("today").ids[
                "stats"
            ].secondary_text = "Please Delete Data and try again"
        try:
            paylist.tertiar_text = "Saved Gigs: 5/7"
        except:
            # paylist.tertiary_text = "third" + payperiod
            1
        paylist2 = self.root.get_screen("today").ids["pay2"]
        try:
            paylist2.text = "Payperiod: " + payperiod
        except:
            logging.info("payperiod not found")
        #####ALWAYS ONBOARD
        # self.do_onboarding(0)
        if x.get("onboarding") == None:
            b = self.do_onboarding(0)
            x["onboarding"] = True
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser(x, ad)
        ###make calendar
        self.reset_cal()
        
        #Clock.schedule_interval(self.update_label, 0.20)
        Clock.schedule_interval(partial(self.update_label,js), 3)
        #stats={"name":'Stats',"func":self.prep_stats(),'icon':'chart-areaspline','order':3}

        #stats={"name":'Login',"func": ( lamda x:self.change_screen('login', 'left')),'icon':'account-circle','order':2}

        menu_items=libs.lib_new.make_menu(self)
        for m in range(len(menu_items)):
            y='yolo'
            if menu_items[m]['disabled']==True:
                bla=lambda x:self.snackbarx('not yet')
                #bla=''
            if menu_items[m]['disabled']==False:
                bla=menu_items[m]['func']
            self.root.get_screen("today").ids["drawer"].add_widget(
            
                MDNavigationDrawerItem(

                    MDNavigationDrawerItemLeadingIcon(
                        icon=menu_items[m]['icon'],
                    ),
                    MDNavigationDrawerItemText(
                        text=str((menu_items[m]['name'])),
                    
                    ),

                    #on_release=lambda x: self.close_menu(),
                    on_release=bla
                    
                    
                    
                ))

    def check_update(self,js):
        shows=js['shows']

        update = js["updated"]

        old_update = datetime.datetime.strptime(update, "%Y-%m-%d %H:%M:%S.%f")
        now = datetime.datetime.now()
        diff2 = humanize.naturaltime(now - old_update)
        next_show = shows[0]["date"] + " " + shows[0]["time"]
        next_show = datetime.datetime.strptime(next_show, "%m/%d/%Y %H:%M")
        bb = 0
        nns = now - next_show
        # logging.info('asdfasdf',nns,type(nns),shows)

        while (nns) >= timedelta(0):
            next_show = shows[bb]["date"] + " " + shows[bb]["time"]
            next_show = datetime.datetime.strptime(next_show, "%m/%d/%Y %H:%M")
            nns = now - next_show

            bb = bb + 1
        diff3 = humanize.naturaltime(now - next_show)
        diff2="Updated "+diff2
        diff3="Next Show: "+diff3
        if now.second%2==0:
            diff2=diff2+str("...")
    

        
        return diff2,diff3

    
    def update_label(self,dt,u):
        
        diff3,diff2=self.check_update(dt)
        #print (diff2,diff3)
        try:
            self.root.get_screen("today").ids["s3"].text=str(diff3)
            self.root.get_screen("today").ids["s2"].text=str(diff2)
        except:
            print ('today does not exist')
        #callist = self.root.get_screen("today").ids["cal_month_text"]
        
        

        #label.text = temp_text[index:index+15]
        #index += 1
        
        #if index >= text_length:
        #    index = 0
    def reset_cal(self):
        print ('lol')
        self.close_menu()
        from datetime import date

        now = date.today()
        month = now.strftime("%m")
        year = now.strftime("%Y")
        mmonth = now.strftime("%B")
        # logging.info(now, "NOW NOW NOW")
        self.make_calendar_today(month, year, mmonth)
        self.do_pp_sum(0, "cal")

    def share_calendar(self):
        import libs.lib_pdf

        js = libs.lib_new.get_json_schedule(x, ad)
        day = self.root.get_screen("today").ids["cal_month_text"].text
        # %B
        dd = datetime.datetime.strptime(day, "%B %Y")
        di = {}
        import libs.lib_archive

        z, z1, f1, f2 = self.find_pay_date(dd.date())

        listofdicks = libs.lib_archive.load("/future_shows", ad, f1, f2)

        for z in range(31):
            status, info = self.check_working(z, dd.month, dd.year, js["shows"])
            status_old, info_old = self.check_working(z, dd.month, dd.year, listofdicks)
            # logging.info(status, info_old, z)
            di.update(info)
        name=libs.lib_pdf.alt(x["name"], ad, di, dd.month, dd.year)
        data= ad + "/blog_calendar.pdf"
        self.do_share_ios(data,name)

    def make_calendar_today(self, month, year, mmonth):
        ###do calendar!!
        import libs.lib_archive

        z, z1, f1, f2 = self.find_pay_date(month + "-" + year)
        listofdicks = libs.lib_archive.load("/future_shows", ad, f1, f2)

        js = libs.lib_new.get_json_schedule(x, ad)

        from datetime import date

        now = date.today()
        now_month = now.strftime("%m")
        now_year = now.strftime("%Y")
        now_day = now.strftime("%d")
        from kivy.uix.button import Button

        # t_color = self.theme_cls.backgroundColor

        for z in range(6):
            self.root.current_screen.ids["cal" + str(z)].clear_widgets()
        self.root.current_screen.ids["calm"].clear_widgets()
        c = libs.lib_cal.basic_cal(month, year)
        # yyy = self.theme_cls
        # logging.info(dir(yyy))

        week_l = ["S", "M", "T", "W", "T", "F", "S"]
        for we in range(len(week_l)):
            self.root.get_screen("today").ids["calm"].add_widget(
                # MDRectangleFlatIconButton(
                # MDRectangleFlatButton(
                Button(
                    # MDIconButton(
                    size_hint=(None, None),
                    size=(dp(50), dp(50)),
                    # icon=ic,
                    # icon_size=dp(6),
                    font_size=dp(15),
                    text=str(week_l[we]),
                    # width=500,
                    # type=type_button,
                    # theme_icon_color="Custom",
                    # text_color=t_color,
                    # md_bg_color=b_color,
                    # background_color=b_color,
                    # color=t_color
                    # size_hint_max=(5, 5),
                    # primary_dark
                    # icon_color=data[type_button]["text_color"],
                )
            )
        for week in range(len(c)):
            for day in range(len(c[1])):
                dd = c[week][day]

                # logging.info(dd, type(dd), dd.day, "c sub week")
                b_color = "black"
                # t_color = "white"
                status = "false"

                ic = ""
                gray = "EEEEEE"
                if dd.day < int(c[week][0].day):
                    b_color = gray
                if dd.day % 4 == 0:
                    ic = "pencil"
                    # t_color = self.theme_cls.bg_dark
                if week == 0:
                    if dd.day <= int(c[week][6].day):
                        b_color = "black"
                        # logging.info("changing it to primamary")
                    else:
                        b_color = gray
                        # logging.info("changing it to black")
                if (
                    int(dd.day) == int(now_day)
                    and int(dd.month) == int(now_month)
                    and int(dd.year) == int(now_year)
                ):
                    b_color = self.theme_cls.primaryColor
                    # t_color = self.theme_cls.secondaryColor

                try:
                    status, info = self.check_working(
                        dd.day, dd.month, dd.year, js["shows"]
                    )
                except:
                    status=False
                try:
                    status_old, info_old = self.check_working(
                        dd.day, dd.month, dd.year, listofdicks
                    )
                except:
                    status_old=False

                # rint(status, "STATUSSSSS")
                t_color = "gray"
                if status_old == True:
                    t_color = self.theme_cls.secondaryColor
                if status == True:
                    # self.theme_cls.primary_palette = x["pcolor"]
                    ####GIG COLOR
                    t_color = "blue"
                    # t_color = self.theme_cls.primaryColor

                # if status == False:

                self.root.get_screen("today").ids["cal" + str(week)].add_widget(
                    # MDRectangleFlatIconButton(
                    # MDRectangleFlatButton(
                    Button(
                        # MDIconButton(
                        size_hint=(None, None),
                        size=(dp(50), dp(50)),
                        # icon=ic,
                        # icon_size=dp(6),
                        font_size=dp(15),
                        text=str(dd.day),
                        # + "[size=0]"
                        # + str(dd.day)
                        # + "-"
                        # + str(dd.month),
                        # width=500,
                        # type=type_button,
                        # theme_icon_color="Custom",
                        # text_color=t_color,
                        # md_bg_color=b_color,
                        background_color=b_color,
                        color=t_color,
                        # size_hint_max=(5, 5),
                        # primary_dark
                        # icon_color=data[type_button]["text_color"],
                        on_release=self.find_cal,
                    )
                )
        callist = self.root.get_screen("today").ids["cal_month_text"]
        callist.text = mmonth + " " + year

    def find_cal(self, y):
        import libs.lib_archive

        from dateutil.relativedelta import relativedelta

        # logging.info(y.background_color, y.color, "bg color")
        # logging.info(self.theme_cls.bg_dark[0], self.theme_cls.bg_dark, "colors")
        bg = "black"
        offset = 0
        if y.background_color[0] == 0.9333333333333333:
            # logging.info(".933")
            bg = "gray"
            if int(y.text) > 20:
                offset = -1
            if int(y.text) < 10:
                offset = 1

        if y.background_color[0] == 0.0:
            logging.info(".0")
        if y.background_color[0] == self.theme_cls.primaryColor[0]:
            logging.info("red.primary")
            bg = "red"

        callist = self.root.get_screen("today").ids["cal_month"].text
        # callist = callist + " " + str(y.text)

        cur_month = datetime.datetime.strptime(callist, "%B %Y").date()
        cur_month = cur_month + relativedelta(months=+offset)
        y1, m1, d1 = str.split(str(cur_month), "-")
        cur_month = y1 + "-" + m1
        cur_month = datetime.datetime.strptime(
            str(cur_month) + " " + str(y.text), "%Y-%m %d"
        ).date()
        z, z1, f1, f2 = self.find_pay_date(cur_month)
        listofdicks = libs.lib_archive.load("/future_shows", ad, f1, f2)

        dd = cur_month
        import libs.lib_new

        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        js = libs.lib_new.get_json_schedule(x, ad)
        try:
            status, info = self.check_working(dd.day, dd.month, dd.year, js["shows"])
            # logging.info(status, "NEW STATUS")
        except:
            status = False
        try:
            status_old, info_old = self.check_working(
                dd.day, cur_month.month, dd.year, listofdicks
            )
            # logging.info(str(status_old), "oldstatus")
        except:
            status_old = False
        js = js["shows"]
        pops = []
        done = False
        for x4 in range(len(js)):
            # logging.info(js[x4]["date"], "jsdate")
            show_date = datetime.datetime.strptime(js[x4]["date"], "%m/%d/%Y").date()
            # logging.info(show_date, cur_month, "asdfasdf")
            if show_date == cur_month and done == False:
                # logging.info("omg you found a real date", js[x4]["show"])
                pops.append(x4)
                if len(pops) > 0:
                    done = True
                    self.click_cal(pops[0], js)
        for x5 in range(len(listofdicks)):
            show_date = datetime.datetime.strptime(
                listofdicks[x5]["date"], "%m/%d/%Y"
            ).date()
            # logging.info(show_date, cur_month, "showandmonth")
            if show_date == cur_month and done == False:
                # logging.info("omg you found an old date", listofdicks[x5]["show"])
                pops.append(x5)
                if len(pops) > 0:
                    done = True
                    self.click_cal(pops[0], listofdicks)

    def cal_next(self, instance):
        # logging.info("cal next")
        import libs.lib_new

        # info = instance.text
        # junk, info = str.split(info, "###")
        info = int(instance)

        js = libs.lib_new.get_json_schedule(x, ad)
        # logging.info(js[info])
        js = js["shows"]

        if info > -1 and info < len(js):
            self.menu.dismiss()
            self.click_cal(info, js)

    def cal_close(self, instance):
        logging.info("cal close", instance.text)
        self.alert.dismiss()

    def check_working(self, day, month, year, js):
        # logging.info(day, month, year, "daymonthyear!")
        found = False
        data = {}
        data2 = {}
        dlist = []
        multi = 0
        vlist = []
        tlist = []
        slist = []
        olist = []
        for xy in range(len(js)):
            d = js[xy]["date"]
            # logging.info (d,'listofdates for shows','checkworkikng')
            smonth, sdate, syear = str.split(d, "/")
            smonth = int(smonth)
            sdate = int(sdate)
            syear = int(syear)
            if smonth == month and sdate == day and syear == year:
                # multi = multi + 1
                # logging.info("OMG YOU FOUND IT on ", js[xy])
                found = True
                show = js[xy]["show"]
                show = str.replace(show, "\n", "")
                if len(show) > 31:
                    show = show[:31]
                    show = show + "..."
                venue = str.split(js[xy]["venue"], "\n")
                try:
                    venue = venue[1]
                except:
                    venue = venue[0]
                data = {
                    day: {
                        "venue" + str(multi): venue,
                        "show" + str(multi): show,
                        "time" + str(multi): js[xy]["time"],
                        "out" + str(multi): js[xy]["endtime"],
                    }
                }

                vlist.append(venue)
                slist.append(show)
                tlist.append(js[xy]["time"])
                olist.append(js[xy]["endtime"])

                # dlist.append(data)
        # logging.info(len(vlist), "lenvlist")
        if len(vlist) > 1:
            for i in range(len(vlist)):
                data[day]["venue" + str(i)] = vlist[i]
                data[day]["show" + str(i)] = slist[i]
                data[day]["time" + str(i)] = tlist[i]
                data[day]["out" + str(i)] = olist[i]

        # logging.info(data, "multi")
        from datetime import datetime, timedelta

        return (found, data)

    def update_today_pp(self, pp):
        # logging.info(pp, "update_today_pp")
        tot_shows = 0
        complete_shows = 0
        from datetime import datetime, timedelta

        if 1 == 1:
            # try:
            js = libs.lib_new.get_json_schedule(x, ad)
        # except:
        #    toast("login failed")
        #    return "fail"
        shows = js["shows"]

        paydate, payperiod = self.find_pay_date(pp)
        # logging.info(shows, "shows")
        pd = datetime.strptime(paydate, "%m/%d/%Y")
        for i in range(len(shows)):
            show_date = datetime.strptime(shows[i]["date"], "%m/%d/%Y")

            min_date = pd.date() + timedelta(days=-21)
            max_date = pd.date() + timedelta(days=-7)

            if show_date.date() >= min_date and show_date.date() < max_date:
                tot_shows = tot_shows + 1
                # if 1 == 1:
                bb = libs.lib_new.get_archive_json(ad, shows[i])
                # logging.info(bb, "bb")
                # logging.info(bb.get("earnings"))
                if (bb.get("earnings")) != None:
                    logging.warning(str(bb["earnings"]) + "         earnings!@!!")
                    complete_shows = complete_shows + 1
                # if shows[i].get("earnings") != None:
                # logging.info(shows[i]["earnings"], "endtime")

            # logging.info(min_date, show_date.date(), max_date)
            paylist = self.root.get_screen("today").ids["pay3"]
        paylist.text = "Saved Times: " + str(complete_shows) + " / " + str((tot_shows))

    def update_fieldnotes(self):
        import libs.lib_fieldnotes

        a = libs.lib_fieldnotes.make_notes(ad, x)

    def view_fieldnotes(self, term):
        logging.info("view_fieldnotes", term)
        global note_index
        self.root.push("allfieldnotes")
        # self.update_fieldnotes()

        import libs.lib_fieldnotes

        pos = libs.lib_fieldnotes.get_notes(x, ad, term)
        # self.load_positions()

        # self.clear_widgets()
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()
        # App.get_running_app().root.current_screen.ids["payperiod_list"].clear_widgets()
        # self.root.current_screen.clear_widgets()
        lpos = pos
        # logging.info(lpos, "lpos")
        # self.root.push("icons")
        self.root.current_screen.ids["payperiod_list"].clear_widgets()

        for z in range(0, len(lpos)):
            show = True
            # logging.info(lpos[z], "lpoz")
            third = ""
            if lpos[z].get("rate") != None:
                if x["pp_hidden"] == True:
                    third = "$" + str(lpos[z]["rate"])
                else:
                    third = "Rate Hidden"
            # logging.info(lpos[z].get("rate"), "get_rate")
            # try:
            #    gg = int(lpos[z]["rate"])
            #    logging.info (gg)
            # except:
            #    if x["pp_all"] == False:
            #        show = False
            y = (
                lpos[z]["title"],
                lpos[z]["url"],
                lpos[z]["num"],
            )
            note_index = y
            if lpos[z].get("rate") == None:
                # logging.info(third, "thirddddd", x["pp_all"])
                # if x["pp_all"] == False:
                #    show = False
                pass

            if show == True:
                # self.root.current_screen.ids["payperiod_list"].add_widget(
                self.root.current_screen.ids["payperiod_list"].add_widget(
                    #    MDListItem(
                    #        text=lpos[z]["title"] + "[size=0]@#$" + lpos[z]["num"],
                    #        on_release=lambda x,
                    #        y=(
                    #            lpos[z]["title"],
                    #            lpos[z]["url"],
                    #            lpos[z]["num"],
                    #        ): self.view_fieldnote(y),
                    #    )
                    MDListItem(
                        MDListItemTrailingIcon(
                            # icon=self.find_type(i, "pos"),
                            icon_color=self.theme_cls.errorColor,
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        MDListItemHeadlineText(
                            text=lpos[z]["title"] + "[size=0]@#$" + lpos[z]["num"],
                            # MDListItemSupportingText(
                            #    text=color + shows[i]["show"],
                            # ),
                            # MDListItemTertiaryText(
                            #    text=color + fvenue,
                            # ),
                        ),
                        on_release=lambda x, y=(y): self.view_fieldnote(y),
                    )
                )

    def view_picture2(self):
        logging.info("view picture2")

    def view_picture(self):
        logging.info("view picture")

    def toggle_star(self):
        pass

        logging.info("toggle")
        text = self.root.current_screen.ids["box"].text
        # logging.info(text, text)
        junk, text = str.split(text, "asdfzxcv")
        note = int(text)

        import libs.lib_fieldnotes

        libs.lib_fieldnotes.toggle_fav_note(ad, note)
        # self.root.current_screen.ids["what"].clear_widgets()
        rai = self.root.current_screen.ids["what"]
        # logging.info(rai.right_action_items[2][1], "whatisths")
        if rai.right_action_items[2][0] == "star":
            rai.right_action_items[2] = (
                "star-outline",
                rai.right_action_items[2][1],
                "help",
            )

        else:
            rai.right_action_items[2] = (
                "star",
                rai.right_action_items[2][1],
                "help",
            )

        logging.info(
            text,
            "toggle it you nerd",
        )
        y = ("", "", note)
        # logging.info(
        #    self.root.current_screen.ids["what"].left_action_items[0], "leftactioinitms"
        # )
        # self.view_fieldnote(y)

    def check_fav(self):
        # logging.info("check star")

        # logging.info("check")
        text = self.root.current_screen.ids["box"].text
        # logging.info(text, text)
        junk, text = str.split(text, "asdfzxcv")
        note = int(text)

        import libs.lib_fieldnotes

        fav = libs.lib_fieldnotes.check_fav_note(ad, note)
        # logging.info(
        #    fav,
        #    "is it favrite",
        #    self.root.current_screen.ids["what"].right_action_items[2][0],
        """
        if (
            fav == True
            and self.root.current_screen.ids["what"].right_action_items[2][0]
            == "star-outline"
        ):
            self.toggle_star()
            # logging.info("toggled1")
        if (
            fav == False
            and self.root.current_screen.ids["what"].right_action_items[2][0] == "star"
        ):
            self.toggle_star()
            # logging.info("toggled2")
            """

    def view_fieldnote(self, y):
        if y == "no":
            # 799 = cable, 2659=tmobile
            y = ("", "", "799")
        self.root.push("fieldnote")
        # self.root.current_screen.ids["what"].clear_widgets()

        logging.info(y, "view single fieldnote")
        import libs.lib_fieldnotes
        import libs.lib_readuserdata
        from kivymd.uix.card import MDCard
        from kivymd.uix.fitimage import FitImage

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        global browser

        nb, text, picture_url, picture, toast_status = libs.lib_fieldnotes.get_single(
            x, ad, y[0], y[1], y[2], browser
        )
        if toast_status != "":
            toast(toast_status)
        if picture != "":
            logging.info(picture, picture_url, "picture stuff")
            try:
                a = open(ad + "/note_pictures/" + picture)
                logging.info("found picture")
            except:
                try:
                    os.mkdir(ad + "/note_pictures")
                except:
                    logging.info("note pictures already exists")

                urllib.request.urlretrieve(
                    picture_url, ad + "/note_pictures/" + picture
                )
                logging.info("downloaded picture")
            browser = nb
            loaded = ad + "/note_pictures/" + picture
            # self.root.current_screen.ids["pic"].source = ad + "/note_pictures/" + picture
            self.root.current_screen.ids["box"].add_widget(
                MDCard(
                    FitImage(
                        source=ad + "/note_pictures/" + picture,
                        # size_hint_y=0.35,
                        # pos_hint={"top": 0},
                        radius=self.cradius4,
                    ),
                    radius=self.cradius,
                    md_bg_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.8},
                    size_hint=(
                        None,
                        None,
                    ),
                    height=dp(250),
                    width=dp(250),
                    on_release=lambda x, y=(loaded): self.do_zoom(y),
                ),
            )
        if picture == "":
            self.root.current_screen.ids["box"].add_widget(
                MDCard(
                    FitImage(
                        source="images/cartoon.png",
                        # size_hint_y=0.35,
                        # pos_hint={"top": 0},
                        radius=self.cradius4,
                    ),
                    radius=self.cradius,
                    md_bg_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.8},
                    size_hint=(
                        None,
                        None,
                    ),
                    height=dp(250),
                    width=dp(250),
                ),
            )

            #
            # logging.info(text, "HOLY GOD ITS TEXT")

            # logging.info(text)

        ss = "[size=" + str(x["text_size"]) + "sp]"
        # logging.info(ss, "this is the text")
        self.root.current_screen.ids["box"].text = (
            ss + str(text) + "[size=0sp]asdfzxcv" + str(y[2])
        )

        self.check_fav()

    def do_wallpaper_screen(self, i):
        import libs.lib_readuserdata

        walls = libs.lib_readuserdata.get_wallpapers()
        logging.info("wallpaper screen")
        self.root.push("wallpaper")
        # logging.info(walls, "list of walls")
        if i < 0:
            i = len(walls) - 1
        if i > len(walls) - 1:
            i = 0
        image = AsyncImage(source="images/walls/" + walls[i])
        self.root.current_screen.ids["sbox"].clear_widgets()
        self.root.current_screen.ids["sbox"].add_widget(image)
        self.root.current_screen.ids["p"].text = "previous[size=0]$$$" + str(i)
        self.root.current_screen.ids["n"].text = "next[size=0]$$$" + str(i)
        self.root.current_screen.ids["i"].text = str(walls[i])

    def change_wall_select(self):
        x["wall"] = self.root.current_screen.ids["i"].text
        self.root.get_screen("theme").ids["pic"].source = self.get_wall("theme")
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

    def change_wall(self, i):
        t = self.root.current_screen.ids["n"].text
        logging.info(t, "tbutton")
        junk, t = str.split(t, "$$$")

        self.do_wallpaper_screen(i + int(t))

    def do_zoom(self, pic):
        self.root.push("zoom")

        logging.info(pic, "PIC")

        scatter = Scatter(
            do_translation=True,
            do_rotation=True,
            size_hint=(None, None),
            height=500,
            width=500,
        )
        logging.info(pic)

        image = AsyncImage(source=pic)
        self.root.current_screen.ids["sbox"].add_widget(image)

    def set_text_size(self, s):
        # logging.info("set text size")
        logging.info(note_index, "this is the note index")

        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        if x.get("text_size") == None:
            x["text_size"] = 15

        x["text_size"] = x["text_size"] + s
        logging.info(x["text_size"], " TEXT SIZE")

        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)
        # logging.info(note_index, "note_indexxxx")
        #
        p = self.root.current_screen.ids["box"].text
        junk, p = str.split(p, "asdfzxcv")
        p = ("", "", p)
        self.view_fieldnote(p)
        # logging.info(p, "all text")

    def search_fieldnotes(self):
        wow = App.get_running_app().root.get_screen("allfieldnotes").ids["search"].text
        # wow = App.get_running_app().root.current_screen.ids["search"].text

        logging.info(wow, "search_icons")
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()
        App.get_running_app().root.get_screen("allfieldnotes").ids[
            "payperiod_list"
        ].clear_widgets()
        self.view_fieldnotes(wow)

    def search_icons(self):
        wow = App.get_running_app().root.current_screen.ids["search"].text

        logging.info(wow, "search_icons")
        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        self.view_icons(wow)

    def view_icons(self, term):
        pos = libs.lib_positions.get_positions(ad, term)
        # self.load_positions()

        from kivymd.uix.list import (
            ThreeLineAvatarIconListItem,
            IconLeftWidget,
        )

        # self.clear_widgets()
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()
        # App.get_running_app().root.current_screen.ids["payperiod_list"].clear_widgets()
        # self.root.current_screen.clear_widgets()
        lpos = pos
        self.root.push("icons")
        self.root.current_screen.ids["payperiod_list"].clear_widgets()

        for z in range(0, len(lpos)):
            show = True
            # logging.info(lpos[z], "lpoz")
            third = ""
            if lpos[z].get("rate") != None:
                if x["pp_hidden"] == True:
                    third = "$" + str(lpos[z]["rate"])
                else:
                    third = "Rate Hidden"
            # logging.info(lpos[z].get("rate"), "get_rate")
            # try:
            #    gg = int(lpos[z]["rate"])
            #    logging.info (gg)
            # except:
            #    if x["pp_all"] == False:
            #        show = False

            if lpos[z].get("rate") == None:
                # logging.info(third, "thirddddd", x["pp_all"])
                if x["pp_all"] == False:
                    show = False

            if show == True:
                self.root.current_screen.ids["payperiod_list"].add_widget(
                    ThreeLineAvatarIconListItem(
                        IconLeftWidget(icon=lpos[z]["icon"]),
                        text=lpos[z]["abv"],
                        secondary_text=lpos[z]["description"],
                        tertiary_text=third,
                    )
                )
            # logging.info(z, "icons!!")

    def find_pay_date(self, c):
        import calendar

        # logging.info (c,'find pay date')
        firstdate = datetime.date(2022, 10, 3)
        #:
        # now = datetime.datetime.now()
        now = datetime.date.today()
        flag = False
        z = 0
        # while flag == False or z < 50:
        # while z < 50:
        while flag == False:
            nextdate = firstdate + datetime.timedelta(days=14)
            # logging.info(nextdate,'lolnextdate')
            lastdate = nextdate + datetime.timedelta(days=13)
            # logging.info(type(nextdate), type(now), lastdate, flag, z)
            # logging.info(nextdate - now)
            if nextdate >= now:
                flag = True
                # logging.info("omg", flag)
            firstdate = nextdate
            z = z + 1
        lastdate = nextdate - datetime.timedelta(days=7)
        lastdate1 = lastdate - datetime.timedelta(days=13)
        if type(c) == int:
            lastdate = lastdate + datetime.timedelta(days=14 * pp_index)
            lastdate1 = lastdate1 + datetime.timedelta(days=14 * pp_index)
            firstdate = firstdate + datetime.timedelta(days=14 * pp_index)

        if c == "Last":
            lastdate = lastdate - datetime.timedelta(days=14)
            lastdate1 = lastdate1 - datetime.timedelta(days=14)
            firstdate = firstdate - datetime.timedelta(days=14)
        if c == "Next":
            lastdate = lastdate + datetime.timedelta(days=14)
            lastdate1 = lastdate1 + datetime.timedelta(days=14)
            firstdate = firstdate + datetime.timedelta(days=14)
        if type(c) == str:  # noqa: E721
            if "-" in c:
                m, y = str.split(c, "-")
                # logging.info (c,'find paydate!!!')
                junk, end = calendar.monthrange(int(y), int(m))
                first = "1-" + c
                last = str(end) + "-" + c
                f = datetime.datetime.strptime(first, "%d-%m-%Y")
                l = datetime.datetime.strptime(last, "%d-%m-%Y")
                # logging.info (f,l,'dates short')
                return (" ", " ", l.date(), f.date())
        if type(c) == datetime.date:
            junk, end = calendar.monthrange(c.year, c.month)
            # logging.info(junk,end,'junkend')
            first = "1-" + str(c.month) + "-" + str(c.year)
            last = str(end) + "-" + str(c.month) + "-" + str(c.year)
            f = datetime.datetime.strptime(first, "%d-%m-%Y")
            l = datetime.datetime.strptime(last, "%d-%m-%Y")
            # logging.info (f,l,'dates short')
            logging.info("DATETIME>DATE")
            return (" ", " ", l.date(), f.date())
        # logging.info (type(c),'TYPEC')

        l = self.format_date(lastdate, "short")
        l2 = self.format_date(lastdate1, "short")
        a = self.format_date(firstdate, "full")
        # logging.info (c,'TRIM')
        # logging.info(l2, l, lastdate, lastdate1, "dates and stuff")
        if c == "All":
            return ("All", "", "", "")
        if type(c) != int:
            return l2, l, lastdate, lastdate1
        # logging.info(a)

        return a, l2 + " - " + l

    def check_confirm(self):
        import libs.lib_new

        app = App.get_running_app()
        ad = app.user_data_dir
        # logging.info(x, "BLABLABLA", ad)
        xx9 = libs.lib_new.just_get_json_schedule(x, ad)
        # logging.info("check confirm", xx9)
        logging.info(xx9["num_shows"], "NUMSHOWS")
        if xx9["num_shows"] > 0 and x["usecache"] == False:
            logging.info(x, "thisisx")
            logging.info(xx9["num_shows"])
            self.new_confirm("all")
            toast("Success")
            self.update_internal("confirm", "1")
            self.update()
        if x["usecache"] == True:
            toast("You are in demo mode")

    def update_global_all(self, ex):
        import libs.lib_firefriend

        logging.info("update_global ALLL")
        # libs.lib_updateuserdata.updateuser_extra(ex, ad)
        z = libs.lib_firefriend.dl_stats(self, ex, x, "global")
        vals = [
            "confirm",
            "update",
            "streak",
            "positions",
            "opened",
        ]
        vals2 = [
            "tot_confirm",
            "tot_update",
            "tot_lstreak",
            "tot_hats",
            "tot_opened",
        ]
        for tots in range(len(vals2)):
            ex[vals2[tots]] = 0
            # logging.info(ex[vals2[tots]], "jesus")
        # logging.info(ex, "jesus2")
        # logging.info(z, "global firebase", len(z), type(z))
        ex["tot_confirm"] = 0
        ex["users"] = 0
        ex["gmax_g"] = 0
        for key, value in z.items():
            # logging.info(key,value, "keyvalue")
            for key2, value2 in value.items():
                # logging.info(value2, "VALUE2")
                ex["users"] = ex["users"] + 1
                logging.info(value2["max_shows"], "maxxxxxx")
                if (value2["max_shows"]) > ex["gmax_g"]:
                    ex["gmax_g"] = value2["max_shows"]

                for tots in range(len(vals)):
                    # logging.info(ex[vals2[tots]], "wowowowow55")
                    # ex[vals2[tots]] = ex[vals2[tots]]
                    ex[vals2[tots]] = ex[vals2[tots]] + (value2[vals[tots]])

                # logging.info(value2, "plist")
        ex["tot_confirm"]

        # logging.info(ex, "totconfirm1111")

        return ex

    def update_global(self):
        logging.info("update_global")
        import libs.lib_readuserdata

        try:
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)
        except:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata_extra(App, ad, ios)
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)

        import libs.lib_firefriend

        os.chdir(cwd)
        z = libs.lib_firefriend.dl_stats(self, ex, x, "single")
        # logging.info((z), z_all, "TYPEZ")
        update = False
        if (z) != None:
            for key, value in z.items():
                # logging.info(value, "keyvalue")
                fb_confirm = value["confirm"]
                fb_streak = value["streak"]
                fb_update = value["update"]
                logging.info(fb_confirm, fb_streak, fb_update, "fbbbbbb")
                if fb_confirm < ex["confirm"]:
                    fb_confirm = ex["confirm"]
                else:
                    ex["confirm"] = fb_confirm
                if fb_streak < ex["streak"]:
                    fb_streak = ex["streak"]
                else:
                    ex["streak"] = fb_streak
                if fb_update < ex["update"]:
                    fb_update = ex["update"]
                else:
                    ex["fb_update"] = fb_update
                if (
                    fb_streak == value["streak"]
                    and fb_confirm == value["confirm"]
                    and fb_update == value["update"]
                ):
                    logging.info("nothing to update")
                else:
                    logging.info("updating fb")
                    z = libs.lib_firefriend.send_stats(self, ex, x)
                    update = True

        if (z) == None:
            z = libs.lib_firefriend.send_stats(self, ex, x)
            update = True
        # libs.lib_updateuserdata.updateuser_extra(ex, ad)

        ex = self.update_global_all(ex)
        if update == False or update == True:
            import libs.lib_updateuserdata

            libs.lib_updateuserdata.updateuser_extra(ex, ad)

    def check_streak(self, ex):
        from datetime import datetime, timedelta

        logging.info("checking streak")

        now = datetime.now().date()
        if ex.get("streak") == None:
            ex["streak"] = 1
        if ex.get("lstreak") == None:
            logging.info("GGGG")
            ex["lstreak"] = 1
        if ex.get("previous_update") == None:
            zz = datetime.now() + timedelta(
                days=-5,
            )
            # logging.info(zz)
            previous = zz.date()
            logging.info("did the update, and checking zzzzz")
            ex["previous_update"] = str(zz.date())
            ex["streak"] = 1
            ex["lstreak"] = 1
            # previous = zzs
            logging.info("exxx", ex)
            return ex
        else:
            previous = datetime.strptime(ex["previous_update"], "%Y-%m-%d").date()
            logging.info("found previous date", previous)
        diff = now - previous
        # logging.info(diff.days, "NOW", dir(diff))
        if diff.days == 1:
            ex["previous_update"] = str(now)
            ex["streak"] = ex["streak"] + 1

        if ex["streak"] > ex["lstreak"]:
            ex["lstreak"] = ex["streak"]
        logging.info
        try:
            zz = str(zz)
        except:
            logging.info("fail to do something")

        # import libs.lib_updateuserdata

        # libs.lib_updateuserdata.updateuser_extra(ex, ad)
        return ex

    def check_internal(self, ex, internal_stat):
        import libs.lib_ach

        if ex.get(internal_stat) == None:
            ex[internal_stat] = 0
        if internal_stat == "hats":
            s, junk = libs.lib_ach.check_hats(self, ad)
            logging.info(s, "slober")
            # ex["positions"] = s
            logging.info(s, "numberofpositions")
            if ex.get("positions") == None:
                ex["positions"] = s
            if ex.get(internal_stat) == None:
                ex[internal_stat] = len(s)

            if ex["hats"] < len(s):
                ex["positions"] = s

            if ex[internal_stat] < len(s):
                ex[internal_stat] = len(s)
        # logging.info(ex[internal_stat], internal_stat, "blablabla)")

        # libs.lib_updateuserdata.updateuser_extra(ex, ad)
        return ex

    def do_internal_stats(self):
        import libs.lib_updateuserdata
        import libs.lib_readuserdata
        import libs.lib_ach

        # if 1 == 1:
        try:
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)
        except:
            # if 1 == 2:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata_extra(App, ad, ios)
            logging.info("Making new extra data")
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)

        ###

        self.root.push("internal_stats")
        logging.info("internal stats")
        # self.update_internal("update", "1")

        import libs.lib_new

        js = libs.lib_new.get_json_schedule(x, ad)
        if useold == False:
            shows = js["shows"]
        if useold == True:
            shows = js["old_shows"]

        rshows = (len(shows)) - (js["num_shows"])
        current_shows = len(js["shows"])

        if ex.get("max_shows") == None:
            # logging.info(ex, "exwtf22")

            ex["max_shows"] = current_shows
            max = current_shows
        if ex.get("min_shows") == None:
            ex["min_shows"] = current_shows
            min = current_shows
        if ex.get("max_shows") != None:
            if current_shows > ex["max_shows"]:
                ex["max_shows"] = current_shows
        if ex.get("min_shows") != None:
            if current_shows < ex["min_shows"]:
                ex["min_shows"] = current_shows

        logging.info("check streak")
        ex = self.check_streak(ex)
        logging.info("checkh hats")
        ex = self.check_internal(ex, "hats")

        libs.lib_updateuserdata.updateuser_extra(ex, ad)
        # logging.info(ex, "exwtf22")
        self.root.get_screen("internal_stats").ids["update"].secondary_text = str(
            ex["update"]
        )
        self.root.get_screen("internal_stats").ids["streak"].secondary_text = str(
            ex["streak"]
        )

        self.root.get_screen("internal_stats").ids["confirm"].secondary_text = str(
            ex["confirm"]
        )
        self.root.get_screen("internal_stats").ids["max"].secondary_text = str(
            ex["max_shows"]
        )

        self.root.get_screen("internal_stats").ids["min"].secondary_text = str(
            ex["min_shows"]
        )
        self.root.get_screen("internal_stats").ids["lstreak"].secondary_text = str(
            ex["lstreak"]
        )
        self.root.get_screen("internal_stats").ids["poses"].secondary_text = str(
            ex["hats"]
        )

        self.root.get_screen("internal_stats").ids["gopened"].secondary_text = str(
            ex["opened"]
        )

        self.root.get_screen("internal_stats").ids["gconfirm"].secondary_text = str(
            ex["tot_confirm"]
        )

        self.root.get_screen("internal_stats").ids["gupdate"].secondary_text = str(
            ex["tot_update"]
        )

        self.root.get_screen("internal_stats").ids["users"].secondary_text = str(
            ex["users"]
        )
        # self.root.get_screen("internal_stats").ids["gstreak"].secondary_text = str(
        #    ex["tot_lstreak"]
        # )
        try:
            self.root.get_screen("internal_stats").ids["gmax"].secondary_text = str(
                ex["gmax_g"]
            )
        except:
            logging.info("failg")

    def update_internal(self, kind, value):
        import libs.lib_updateuserdata
        import libs.lib_readuserdata

        # libs.lib_updateuserdata.updateuser_extra(x, ad)

        try:
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)
        except:
            import libs.lib_makeuserdata

            libs.lib_makeuserdata.makeuserdata_extra(App, ad, ios)
            ex = libs.lib_readuserdata.readuserdata_extra(App, ad, ios)
        logging.info(str(ex) + "EXTRA EXTRA111" + str(kind))
        if (
            kind == "update"
            or kind == "confirm"
            or kind == "streak"
            or kind == "cstreak"
            or kind == "opened"
        ):
            if ex.get(kind) == None:
                logging.info("update not found")
                ex[kind] = 1
                libs.lib_updateuserdata.updateuser_extra(ex, ad)
            if ex.get(kind) > -1:
                ex[kind] = ex[kind] + 1
                libs.lib_updateuserdata.updateuser_extra(ex, ad)
        # logging.info(ex, "EXTRA EXTRA")

    def make_toast(self, b):
        logging.info(x, b)

    def update(self):
        logging.info("only updating schedule")
        import libs.lib_new

        # try:
        if 1 == 1:
            libs.lib_new.make_json_schedule(x, ad)
            logging.info("updated schedule")
            self.update_internal("update", 1)
            self.snackbarx("Success")

        # except:
        ##    logging.info("login failed")
        #   toast("login failed")
        self.today()

    def open_panel2(self, xx, i, l, junk, z):
        logging.info("adf", xx, i, l)

        global i9
        global xx9

        xx9 = xx
        i9 = i

    def open_panel(self, xx, i, l, junk, z):
        try:
            global i9
            global xx9
            global s_index

            s_index = z

            xx9 = xx
            i9 = i
            logging.info("asdfasdf", xx9, i, l, z)

            rw = RecipeLine(text=(str("loll")))
            # rw = IngredientDialog(text=("lol"))
            # for x in range(10):
            # self.root.current_screen.ids["rlist"].clear_widgets()
            if junk == False:
                self.root.get_screen("newhome").ids.rlist.children[
                    0
                ].content.clear_widgets()
                self.root.get_screen("newhome").ids.rlist.children[0].content.ids[
                    "pos"
                ].text = xx9["pos"]

                self.root.get_screen("newhome").ids.rlist.children[0].content.ids[
                    "pos"
                ].secondary_text = xx9["pos"] + str(z)

                pp = (
                    self.root.get_screen("newhome")
                    .ids.rlist.children[0]
                    .content.ids["pos"]
                    .text
                )
                try:
                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos"].text = (
                        xx9["pos"] + " " + xx9["type"] + " " + xx9["status"]
                    )
                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos"].secondary_text = xx9["venue"] + " " + " "

                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos2"].text = (
                        xx9["client"] + " \n" + xx9["job"] + " \n"
                    )

                    self.root.current_screen.ids["rlist"].children[
                        (l - i9) - 1
                    ].content.ids["pos2"].secondary_text = xx9["notes"]
                    logging.info("old stuff,", l, i9)
                except:
                    logging.info(l, i9, "failed to open")

            if junk == True and x["usecache"] == False:
                self.root.current_screen.ids["rlist"].children[(l)].content.ids[
                    "pos"
                ].text = str(i) + " " + str(l)
                logging.info("newconfirm you nuts")
                self.new_confirm("all")

            # logging.info(pp)
            # logging.info(x)
            # App.get_running_app().root.current_screen.ids["rlist"].text = "posss"
            # logging.info(App.get_running_app().root.current_screen.ids)
            # zz = dir(self.root.get_screen("newhome").ids.rlist.children[0])
            pass
        except:
            toast("failed to make list")
            self.newstart("", False)

    def close_panel(self, what):
        Pass
        logging.info(what)

    def newstart(self, search, useold):
        import libs.lib_bonus
        from datetime import datetime, timedelta

        self.root.push("newhome")
        self.root.current_screen.ids["rlist"].clear_widgets()

        import libs.lib_new

        js = libs.lib_new.get_json_schedule(x, ad)
        if useold == False:
            shows = js["shows"]
        if useold == True:
            shows = js["old_shows"]
        rshows = (len(shows)) - (js["num_shows"])
        """
        self.root.get_screen("today").ids[li[i] + "1"].text = (
                color + show_date + " " + ntime
            )
            self.root.get_screen("today").ids[li[i]].text = (
                color + show_date + " " + ntime
            )
            logging.info(li[i] + str(i + 1), "thisistheid")
            self.root.get_screen("today").ids[li[i] + "2"].text = (
                color + shows[i]["show"]
            )
            self.root.get_screen("today").ids[li[i] + "3"].text = color + fvenue[0]
        
        """

        for i in range(len(shows)):
            show_date = datetime.strptime(shows[i]["date"], "%m/%d/%Y")
            show_date = show_date.strftime("%A, %m/%d")
            z = shows[i]["time"]
            ntime = self.ampm(z)
            fvenue = shows[i]["venue"]
            color = ""
            if shows[i]["canceled"] == True:
                color = "[color=#ff0000]"
            # color = "[color=#ff000055]"

            # if "las vegas" in fvenue:
            #   fvenue = str.split(fvenue, "las vegas")
            self.root.get_screen("newhome").ids.rlist.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        icon=self.find_type(i, "type"),
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        icon_color=self.theme_cls.primaryColor,
                    ),
                    MDListItemTrailingIcon(
                        icon=self.find_type(i, "pos"),
                        icon_color=self.theme_cls.errorColor,
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    ),
                    MDListItemHeadlineText(text=color + show_date + " " + ntime),
                    MDListItemSupportingText(
                        text=color + shows[i]["show"],
                    ),
                    MDListItemTertiaryText(
                        text=color + fvenue,
                    ),
                    on_release=lambda x, y=(i): self.pop_new(y),
                )
            )

        """
        if useold == False:
            if js["num_shows"] > 0:
                ttt = str(rshows) + "/" + str(len(shows)) + " shows 1confirmed"
            else:
                ttt = str(len(shows)) + " shows 1confirmed"

            panel = MDExpansionPanel(
                # icon="recipe.png",
                content=Content(),
                panel_cls=MDExpansionPanelThreeLine(
                    text=ttt,
                    # content=Content(),
                    # secondary_text=shows[z]["show"],
                    # tertiary_text=shows[z]["venue"],
                    text_color=(1, 0, 1, 0),
                    on_open=lambda x, y=js, q=0,: self.open_panel(y, q),
                    on_close=self.close_panel,
                ),
            )
            panel.bind(
                on_open=lambda x, y=js, q="Click to Confirm All", l=js[
                    "num_shows"
                ], p=True: self.open_panel(y, q, l, p),
                on_close=self.close_panel,
            )

            self.root.get_screen("newhome").ids.rlist.add_widget(panel)
            canned = -1

            for z in range(len(shows)):
                color = ""
                # logging.info(shows[z])
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    canned = canned + 1
                if shows[z]["status"] != "Confirmed":
                    color = "[color=#00ff00]"
                if shows[z]["canceled"] == True:
                    color = "[color=#ff0000]"
                if shows[z]["old"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#555555]"
                if shows[z]["old"] == True and shows[z]["canceled"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#550000]"

                panel = MDExpansionPanel(
                    # icon="recipe.png",
                    content=Content(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text=color
                        + shows[z]["date"]
                        + "\n"
                        + self.ampm(shows[z]["time"])
                        + " [/sup]         "
                        + shows[z]["pos"],
                        # content=Content(),
                        text_color=(1, 0, 1, 0),
                        secondary_text=color + shows[z]["show"],
                        tertiary_text=color + shows[z]["venue"],
                        on_open=lambda x, y=shows[z], q=canned: self.open_panel(y, q),
                        on_close=self.close_panel,
                    ),
                )

                panel.bind(
                    on_open=lambda x, y=shows[z], q=canned, l=len(
                        shows
                    ), junk=False, bb=z: self.open_panel(y, q, l, junk, z),
                    on_close=self.close_panel,
                )
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    self.root.get_screen("newhome").ids.rlist.add_widget(panel)
                # libs.lib_bonus.create_notification(shows[z], x, True, ad)
        if useold == True:
            canned = -1
            for z in range(len(shows)):
                color = ""
                # logging.info(shows[z])
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    canned = canned + 1
                if shows[z]["status"] != "Confirmed":
                    color = "[color=#00ff00]"
                if shows[z]["canceled"] == True:
                    color = "[color=#ff0000]"
                if shows[z]["old"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#555555]"
                if shows[z]["old"] == True and shows[z]["canceled"] == True:
                    color = color + "[size=3sp]"
                    color = "[color=#550000]"

                panel = MDExpansionPanel(
                    # icon="recipe.png",
                    content=Content3(),
                    panel_cls=ThreeLineListItem(
                        text=color + shows[z]["date"] + "\n" + shows[z]["time"],
                        # content=Content(),
                        text_color=(1, 0, 1, 0),
                        secondary_text=color + shows[z]["show"],
                        tertiary_text=color + shows[z]["venue"],
                        on_open=lambda x, y=shows[z], q=canned: self.open_panel2(y, q),
                        on_close=self.close_panel,
                    ),
                )
                panel.bind(
                    on_open=lambda x, y=shows[z], q=canned, l=len(
                        shows
                    ), junk=False, z=z: self.open_panel2(y, q, l, junk, z),
                    on_close=self.close_panel,
                )
                # if shows[z]["canceled"] == True:
                if 1 == 1:
                    self.root.get_screen("newhome").ids.rlist.add_widget(panel)
        # toast(str(tic - time.perf_counter()))
        '''"""

    def showinfo(self, cat, r, d):
        from kivymd.uix.dialog import MDDialog as md33

        # for ingredient in ingredients:
        #    ingredients_text += ingredient + "\n"
        # self.dialog = IngredientDialog(text=ingredients_text)
        # self.dialog.open()
        logging.info(cat, r, d)
        # r = ""
        if not self.dialog2[d]:
            self.dialog2[d] = md33(
                text=r,
                type="custom",
                #
                # content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="Email Times,",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x, y=(cat, r, d): self.email_time(y),
                    ),
                    # MDFlatButton(
                    #    text="Save Time",
                    #    theme_text_color="Custom",
                    #    text_color=self.theme_cls.primary_color,
                    #    # on_release=self.email_time,
                    # ),
                    # MDFlatButton(
                    #    text="Confirm",
                    #    theme_text_color="Custom",
                    #    text_color=self.theme_cls.primary_color,
                    #    on_release=lambda x, y=(cat, r, d): self.new_confirm(y),
                    # ),
                ],
            )

        self.dialog2[d].open()

    def new_confirm(self, asdf):
        import libs.lib_new

        xx9 = libs.lib_new.get_json_schedule(x, ad)
        # logging.info("save_time", xx9, x)

        try:
            logging.info(asdf, str(xx9["confirmables"]), "OMG ITS CONFIRMING ITSELF")
        except:
            logging.info("one?", asdf)
        if asdf == "all":
            for xxx in range(int(xx9["num_shows"])):
                fail = self.confirm_real(xx9["confirmables"][xxx])
                logging.info((xx9["confirmables"][xxx]), "whattttttttt")
        if asdf != "all":
            if xx9.get("confirable"):
                logging.info(xx9["confirable"], "DO CONFIRM THIS")
                fail = self.confirm_real(asdf)
                logging.info(fail)
                toast("Confirmed")
                self.update()
                self.newstart("", False)
                for u in range(len(self.dialog2)):
                    try:
                        self.dialog2[u].dismiss(force=True)
                    except:
                        logging.info(u)

        else:
            logging.info(
                "one",
                profile,
            )
            # fail = self.confirm_real(asdf)

    def email_time(self, gg):
        # logging.info("save_time", x)

        try:
            endtime = str(x["endtime"])
        except:
            endtime = "??"
            ##TODO make clock thing

        try:
            lunches = str(x["lunches"])
            if lunches > 1:
                es = "es"
        except:
            lunches = "??"
            ##TODO MAKE LUNCHES
            es = ""
        xx9 = gg
        # ee = f"Hi,\nI worked {str(xx9["show"])}  {str(xx9["job"])} at {str(xx9["venue"])} on {str(xx9["date"])} from {str(xx9["venue"])} to {str(xx9["endtime"])}\n Thanks,\n{str(x["name"])}"
        ee = f"Hi,\nI worked {str(xx9['show'])}  ({str(xx9['job'])}) at {str(xx9['venue'])} on {str(xx9['date'])} from {str(xx9['time'])} to {endtime} with {lunches} walkaway lunch{es}\nThanks, {str(x['name'])}"
        # logging.info(ee)
        from kivymd.uix.dialog import MDDialog as md33
        from kivy.core.clipboard import Clipboard

        self.menu.dismiss()

        self.menu2 = MDDialog(
            # type=simple,
            # ----------------------------Icon-----------------------------
            # MDDialogIcon(
            #    icon=self.find_type(d, "type"),
            # ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text=gg["show"],
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text=gg["date"],
            ),
            MDDialogSupportingText(
                text=gg["time"],
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDTextField(text=ee, multiline=True),
                orientation="vertical",
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                Widget(),
                # MDFabButton(icon="arrow-right-bold", style="small"),
                MDFabButton(
                    style="small",
                    icon="content-copy",
                    on_release=lambda x, y=(ee): self.grabText(ee),
                ),
                MDFabButton(icon="share", style="small"),
                MDFabButton(
                    icon="close-box",
                    style="small",
                    on_release=lambda x, y=(gg): self.menu.dismiss(),
                ),
                spacing="20dp",
                # cent2er=(50, 0),
                right=False,
                size_hint=(None, None),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                center_y=2100,
            ),
            # -------------------------------------------------------------
        )

        App.get_running_app().root.current_screen.ids["test2"] = self.menu2
        self.menu2.open()

    def copy_email(self, eee):
        logging.info("email_times", eee)

    def ingredients_list(self, selected_cat, selected_r):
        for category in self.card_file:
            if category["Category"] == selected_cat:
                for recipe in category["Recipes"]:
                    if recipe["title"] == selected_r:
                        return recipe["shopping list"]

    def do_login(self, search, useold):
        logging.info("do_login")

        # if pf[0]!='W':
        # if 1==1:
        # from lib_test import n22
        # n22()

        global xxx
        global mjds
        global config_file
        global plus_search
        good_login = False
        from datetime import datetime, date

        now = datetime.now()
        app = App.get_running_app()
        config_file = app.user_data_dir

        self.root.current = "home"
        self.root.current_screen.ids["users_lst"].clear_widgets()
        # logging.info(x, "USECACHETEST")

        if x["usecache"] == "True" or x["usecache"] == True:
            logging.info("Using Cache2")
            import libs.lib_createcache as lib_createcache
            from random import randrange

            lib_createcache.createcache(ad, randrange(1, 40, 10))
        sch = ad + "/conf.html"

        if x["usecache"] == "False" or x["usecache"] == False:
            logging.info("Using Live Data")
            if useold == False:
                if x["refreshreload"] == True:
                    good_login = lib_think.login(ad, x, ios, App)
                    good_login = True

                if good_login == True:
                    logging.info("GOOD LOGIN SIR")
                    sch = ad + "/realdata.html"
                if x["refreshreload"] == False:
                    try:
                        sch = ad + "/realdata.html"
                    except:
                        logging.info("realdata not found")

        import libs.lib_parse

        # logging.info(ad, "ADADAD")

        xxx, mjds, name = libs.lib_parse.parse(sch, ad, x["usecache"], x)

        logging.info(x, "XXXXXXX")
        x["name"] = name
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

        try:
            cf, week, tot = libs.lib_tinyfs.stats(xxx, now, search)
        except:
            import libs.lib_tinyfs

            cf, week, tot = libs.lib_tinyfs.stats(xxx, now, search)

        founddates = ""
        if len(search) > 0:
            founddates = (
                str(tot)
                + "/"
                + str(len(xxx) - 1)
                + "dates matching: "
                + str(search)
                + "\n"
            )

        texta = (
            "[size=18 sp]"
            + founddates
            + str(cf)
            + "/"
            + str(tot)
            + " confirmed dates\n"
            + str(week)
            + " gigs this week[size=1 sp]***0"
        )

        indexnumber = 0
        indexnumber_real = -1
        self.root.current_screen.ids["users_lst"].add_widget(
            SwipeToDeleteItem(text=texta)
        )
        toc3 = time.perf_counter()
        logging.info(tic - toc3, "toc3time")
        if cf < tot:
            indexnumber = indexnumber + 1
            texta = (
                "Click To Confirm"
                + str(tot - cf)
                + " gigs [size=1 sp]***"
                + str(indexnumber)
            )
            self.root.current_screen.ids["users_lst"].add_widget(
                SwipeToDeleteItem(text=texta)
            )

        plus_search = 0
        for i in range(len(mjds)):
            # lib_bonus.create_notification(mjds[i],x)
            texta = libs.lib_tinyfs.format_text(i, mjds, now, "index")
            indexnumber = indexnumber + 1
            indexnumber_real = indexnumber_real + 1
            texta = texta + str(indexnumber_real)
            if search.lower() in str(xxx[i]).lower() or len(search) == 0:
                # logging.info("omg its working")
                plus_search = plus_search + 1

                self.root.current_screen.ids["users_lst"].add_widget(
                    SwipeToDeleteItem(text=texta)
                )

        logging.info(
            plus_search,
            "plussearch",
            len(mjds),
            (tic - time.perf_counter(), "after schedule"),
        )
        # toast("lol" + str(tic - time.perf_counter()))
        return good_login

    def do_settings(self):
        global x
        # logging.info(x)
        os.chdir(cwd)
        self.close_menu()
        # logging.info(os.getcwd(), "logging.info OMGOMG")
        self.root.push("settings")
        # sm.set_current("settings")
        try:
            self.root.get_screen("notification").ids["slider2"].value = x["not2time"]
            self.root.get_screen("notification").ids["slider1"].value = x["not1time"]

            self.root.get_screen("notification").ids["disable1"].active = x["not1"]
            self.root.get_screen("notification").ids["disable2"].active = x["not2"]

            if x["not"] == True:
                App.get_running_app().root.current_screen.ids[
                    "switchnotify"
                ].active = True

            tog1 = App.get_running_app().root.current_screen.ids["switchnotify"].active
        except:
            x["not2time"] = 0
            x["not1time"] = 0
            x["not1"] = False
            x["not2"] = False
            x["not"] = False
        # logging.info (tog1)
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)
        print ('wtf man')

    """
    class Demo3App2(MDApp):
        scale = 2
        if platform[0] == "w":
            scale = 1
            notch = False
        # def __init__(self, **kwargs):
        #    self.snackbar = None
        global idex
        iii = idex
        bud2 = "65"
        global x
        x = x

        
        newercolor = newcolor
        xxxx = xxx + "wtf" + str(idex)
        

        cpadding = 20
        cspacing = 10
        mtype = "top"
        bradius = 10 * scale
        radius = 10 * scale
        # mfontel='fonts/SourceSansPro-ExtraLight.ttf'
        # mfontb='fonts/SourceSansPro-Bold.ttf'
        # mfont='fonts/SourceSansPro-Regular.ttf'
        


        notheight = 200 * scale
        

        angle = NumericProperty(0)
        startCount = NumericProperty(20)
        Count = NumericProperty()
        """
        
    notheight = 200 * scale
    ot = ["8", "10", "0", "1", "2", "3", "4", "5", "6", "7", "9"]
    lunch = ["0", "1", "2"]
    dialog = None
    dialog2 = [None, None, None, None, None, None]
    dialog_name = None
    dialog3 = None

    snackbar = None
    rreverse = True

    archive_reverse = True
    archive_sort = "date"
    archive_trim = "Current"
    menurotate = 10
    menuscale = 0.5, 0.5
    

    def update_hi_score_keys(self):
        logging.info("updating scores")
        import libs.lib_ach

        win = libs.lib_ach.download_ach(ad)
        toast(win)

    def update_hi_score_data(self, ach):
        logging.info("updating scores")
        import libs.lib_score

        win = libs.lib_score.dl_score(x["name"], ach, ad)
        toast(win)
        self.ach_top(ach)

    def set_Circle(self, dt):
        self.angle = self.angle + dt * 360
        if self.angle >= 360:
            self.angle = 0
        Clock.schedule_once(self.set_Circle, 0.1)

    def set_Count(self):
        self.Count = self.Count - 1

    def callback_for_menu_items(self, text):
        self.menu.dismiss()
        toast(text)

    def get_wall(self, page):
        # self.root.set_current(page)

        # logging.info(x, "assert")
        try:
            b = "images/walls/" + x["wall"]
        except:
            b = "images/walls/" + "rhino" + ".jpg"
        try:
            self.root.get_screen(page).ids["pic"].source = b
            self.root.get_screen("theme").ids["pic"].source = b
            logging.info("success set image")
        except:
            logging.warning("fail to set image")
            pass
        try:
            self.root.get_screen("theme").ids["pic"].source = b
        except:
            logging.warning("coundnt find the theme page")

        return b

        # self.root.current = "settings"

    def menu_callback(self, text_item, v, v2):
        # logging.info(location[text_item])
        # logging.info (text_item,type(text_item))
        # logging.info(v[text_item], "v[text")
        # logging.info(text_item, v2, v, "dumbass")
        if v2 == "name":
            # toast(str(v[text_item][v2]))
            App.get_running_app().root.current_screen.ids[
                "last_restore"
            ].secondary_text = str(v[text_item][v2])
        if v2 == "city":
            App.get_running_app().root.current_screen.ids["lol"].text = str(
                v[text_item]
            )
        if v2 == "pcolor":
            App.get_running_app().root.current_screen.ids["button_t"].text = str(
                v[text_item]
            )
            self.theme_cls.primary_palette = v[text_item]

        if v2 == "wall":
            App.get_running_app().root.current_screen.ids["button5"].text = str(
                v[text_item]
            )
            self.root.push("theme")
            self.root.get_screen("theme").ids["pic"].source = self.get_wall("theme")

        if v2 == "lunches":
            App.get_running_app().root.current_screen.ids["button4"].text = str(
                v[text_item]
            )
            self.update_show()
        if v2 == "oth":
            App.get_running_app().root.current_screen.ids["button5"].text = str(
                v[text_item]
            )
            self.update_show()
            # self.edit_show_details(App.get_running_app().root.current_screen.ids["button2"])
            # self.root.push("theme")
            # self.root.get_screen("editShow").ids["lnch"].text=str(v)

        # self.root.get_screen(v2).ids["button4"].text = v[text_item]
        if v2 == "range":
            App.get_running_app().root.current_screen.ids["button4"].text = str(
                v[text_item]
            )
        global x
        x[v2] = v[text_item]
        # logging.info(x)
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)
        self.menu.dismiss()

    drop_item_menu: MDDropdownMenu = None

    def open_menu(self, item, gg):
        it = ["Email", "Field Guide", "Save Times", "Share", "Other?"]
        menu_items = [
            {
                "text": it[i],
                "on_release": lambda x=it[i]: self.menu_callback2(x, gg),
            }
            for i in range(len(it))
        ]
        self.menu_items = MDDropdownMenu(
            caller=App.get_running_app().root.current_screen.ids["test"],
            items=menu_items,
        )
        self.menu_items.open()

    def menu_callback2(self, item, gg):
        # self.root.ids.drop_text.text = text_item
        self.menu_items.dismiss()
        if item == "Email":
            self.email_time(gg)

    def open_drop_item_menu(self, v, v2):
        # v2 = "wow"
        logging.info(str(v) + "what is v")

        # menu_items = [
        #     {
        #         "text": f"{v[i]}",
        #         "on_release": lambda x=f"Item {i}": self.menu_callback(x, v, v2),
        #     }
        #     for i in range(len(v) - 1)
        # ]
        menu_items = [
            {
                "text": f"{v[i]}",
                "on_release": lambda x=i: self.menu_callback(x, v, v2),
            }
            for i in range(len(v) - 1)
        ]
        self.menu = MDDropdownMenu(
            caller=App.get_running_app().root.current_screen.ids["button4"],
            items=menu_items,
            max_height=dp(4000),
            height=dp(154),
            ##position="center",
            width_mult=4,
        )
        self.menu.open()

    def choose_drop(self, v, v2):
        "oll"
        logging.info(v2, v, "THISISTHETHING2")

        if v2 == "city":
            menu_items = [
                {
                    "text": f"{v[i]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "name":
            menu_items = [
                {
                    "text": f"{v[i][v2]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "pcolor":
            menu_items = [
                {
                    "text": "[color=" + webcolors.name_to_hex(v[i]) + "]" + v[i],
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "wall":
            menu_items = [
                {
                    "text": v[i],
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "lunches":
            menu_items = [
                {
                    "text": f"{v[i]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "oth":
            menu_items = [
                {
                    "text": f"{v[i]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=i: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]
        if v2 == "range":
            # presets
            menu_items = [
                {
                    "text": f"{v[i]}",
                    # "scroll_type": ['bars'],
                    # "effect_cls": "ScrollEffect",
                    "viewclass": "MDListItem",
                    "on_release": lambda x=v[i]: self.set_range(x, v, v2),
                    # "on_release": lambda x=1: self.menu_callback(x, v, v2),
                }
                for i in range(len(v) - 1)
            ]

            self.menu = MDDropdownMenu(
                # header_cls=MenuHeader(),
                # caller=self.screen.ids.button,
                # items=menu_items,
            )
            # self.root.
            self.send_dates([x, v, v2])
        # logging.info(self.root.get_screen("notification").ids)
        self.menu = MDDropdownMenu(
            # caller=self.root.get_screen("notification").ids["button4"],
            caller=App.get_running_app().root.current_screen.ids["button4"],
            items=menu_items,
            max_height=dp(4000),
            height=dp(154),
            # position="center",
            width_mult=4,
        )
        # self.menu.caller = button4
        self.menu.open()

    def set_range(self, x, y, z):
        logging.info("set_range", x, y, z)
        logging.info(self.root.current_screen.name, "WHATSCREEN")
        if self.root.current_screen.name == "newstats":
            logging.info("NEWSTATS!!!")

            b = datetime.datetime.now().date().replace(month=1, day=1, year=int(x))
            b = datetime.datetime.combine(b, datetime.datetime.min.time())
            now = (
                datetime.datetime.now().date().replace(month=12, day=31, year=(int(x)))
            )
            e = datetime.datetime.combine(now, datetime.datetime.min.time())

            self.do_new_stats(b, e, "Custom")

        if self.root.current_screen.name == "pay":
            (
                b,
                e,
            ) = self.do_payperiod_f(int(x))
        App.get_running_app().root.current_screen.ids["dstart"].text = str(b.date())
        App.get_running_app().root.current_screen.ids["dend"].text = str(e.date())
        self.menu.dismiss()

    def format_minutes(self, t, v, d):
        # v=5
        if d == True:
            return t + " Notification will be sent " + str(v) + " minutes before call"
        if d == False:
            return t + " Notification disabled"

    def enable_nots(self):
        global x
        self.root.current = "settings"
        tog1 = App.get_running_app().root.current_screen.ids["switchnotify"].active
        # logging.info(tog1, x)
        x["not"] = tog1

        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)

    def loadnots(self, sslider):
        global x

        self.root.current = "notification"

        if x["not1"] == True:
            App.get_running_app().root.current_screen.ids["disable1"].active = True

        if x["not2"] == True:
            App.get_running_app().root.current_screen.ids["disable2"].active = True
        App.get_running_app().root.current_screen.ids["slider2"].value = x["not2time"]
        try:
            App.get_running_app().root.current_screen.ids["slider2"].value = x[
                "not2time"
            ]
            App.get_running_app().root.current_screen.ids["slider1"].value = x[
                "not1time"
            ]
        except:
            logging.info("rip")
        lib_updateuserdata.updateuser(x, ad)

    def makenots(self, sslider):
        from kivymd.uix.expansionpanel import (
            MDExpansionPanel,
            MDExpansionPanelThreeLine,
            MDExpansionPanelOneLine,
        )

        global x
        # self.root.current = "notification"
        self.root.push("notification")
        try:
            App.get_running_app().root.current_screen.ids["button4"].text = x[
                "sound_effects"
            ]
        except:
            App.get_running_app().root.current_screen.ids["button4"].text = "Normal"

        first = str(
            App.get_running_app().root.current_screen.ids["slider" + sslider].value
        )
        # App.get_running_app().root.current_screen.ids['text'+sslider].text=first

        text1 = str(App.get_running_app().root.current_screen.ids["slider1"].value)
        text2 = str(App.get_running_app().root.current_screen.ids["slider2"].value)
        tog1 = App.get_running_app().root.current_screen.ids["disable1"].active

        tog2 = App.get_running_app().root.current_screen.ids["disable2"].active

        x["not1"] = tog1
        x["not1time"] = text1

        x["not2"] = tog2
        x["not2time"] = text2
        import libs.lib_updateuserdata

        libs.lib_updateuserdata.updateuser(x, ad)
        try:
            self.root.current_screen.ids["box"].remove_widget(content.parent)

        except:
            logging.info("omg")

    def about(self):
        self.root.push("about")

    def ach_top(self, lol):
        logging.info("achtop", lol)
        from kivy.metrics import dp
        from kivy.uix.anchorlayout import AnchorLayout

        self.root.push("achscore")
        self.root.current_screen.ids["graphs3"].clear_widgets()
        import libs.lib_score

        name = x["name"]
        scores, place, q = libs.lib_score.parse_score(
            name, lol, ad, self.theme_cls.primary_color
        )

        logging.info(q, "SCORESSSS", place)
        tables = MDDataTable(
            # size_hint=(0.9, 0.6),
            #
            # background_color_selected_cell=self.theme_cls.primary_light,
            column_data=[
                ("Points", dp(20)),
                ("Name", dp(30)),
                ("Rank", dp(20)),
            ],
            row_data=[
                q
                # The number of elements must match the length
                # of the `column_data` list.
            ],
        )

        self.root.current_screen.ids["graphs3"].add_widget(tables)

    def ach_info(self, data):
        logging.info("info ach", data)
        self.root.push("achinfo")
        self.root.current_screen.ids["ach_info_id"].clear_widgets()
        dd = [
            [data["name"], data["disc"]],
            ["Date Achieved:", data["date_achieved"]],
            [data["ach_extra"], (data["ach_progress"])],
            ["Points:", data["ach_level"]],
        ]
        shows = ""
        # logging.info(data["ach_shows"])
        # logging.info(type(data["ach_shows"]))
        # logging.info("LISTNODATA")
        try:
            newd = dict(
                sorted(
                    data["ach_shows"].items(), key=lambda item: item[1], reverse=True
                )
            )
            keys = list((newd).keys())
            values = list((newd).values())
            totshows = 0
            for x in range(len(values)):
                totshows = totshows + values[x]
        except:
            newd = data["ach_shows"]
            keys = data["ach_shows"]
            values = data["ach_shows"]

        # (keys,values) = zip(*tel.items())

        # shows = "[font=Roboto-Regular]" + shows + "[/font]"
        # logging.info(f"{a:10}{b:10}{c:10}"
        # logging.info(shows)

        for z in range(len(dd)):
            # logging.info(str(dd[z][0],str(dd[z][1])
            items = TwoLineAvatarListItem22(
                text=str(dd[z][0]),
                secondary_text=str(dd[z][1]),
                # icon=real_icon,
                # on_release=lambda x, y=data[i]: self.ach_info(y),
            )

            self.root.current_screen.ids["ach_info_id"].add_widget(items)

        # self.root.current_screen.ids["ach_info_id"].add_widget(SmoothLabel(text=self.ids.msg.text, size_hint_x=0.5, size_hint_y=0.1, pos_hint={"x": 0.1, "top": 0.8}, background_color=(0.2, 0.6, 1, 1)))
        # keys.insert(0, "Pos:")
        # values.insert(0, "#:")
        first = 30
        second = 20
        third = 20
        for m in range(len(keys)):
            logging.info(keys)
            if data["name"] == "Hustle and Grind":
                logging.info("jesusccc")

                # keysm = str(m)
                keysm = ""
                valuesm = data["ach_shows"][m][1]
                perc = data["ach_shows"][m][2]

                valuesm, junk, junk = str.split(valuesm, " ")
                first = 4
                third = 30
            if data["name"] == "Celery man!":
                logging.info("jesusccc")

                # keysm = str(m)
                keysm = str(data["ach_shows"][m][0])
                logging.info(data["ach_shows"][m])
                valuesm = data["ach_shows"][m][1]
                perc = data["ach_shows"][m][2]

                perc, junk, junk = str.split(perc, " ")
                first = 6

            if data["name"] == "Wear The Hat":
                try:
                    perc = values[m] / (totshows * 1.0)

                    perc = perc * 100
                    perc = f"{perc:.2f}%"
                    perc = str(perc)
                    keysm = str(keys[m])
                    valuesm = str(values[m])

                except:
                    perc = data["ach_graph_disc"][0]
                    keysm = data["ach_graph_disc"][1]
                    try:
                        valuesm = data["ach_graph_disc"][2]
                    except:
                        valuesm = ""
            try:
                while len(keysm) < first:
                    keysm = keysm + " "
                while len(valuesm) < 20:
                    valuesm = valuesm + " "
                while len(perc) < third:
                    perc = perc + " "

                if len(valuesm) > 15:
                    valuesm = valuesm[0:15]
                if len(perc) > 15:
                    perc = perc[0:15]
                shows = (
                    f"[font=Roboto-Regular]{keysm} {str(valuesm)} {str(perc)}[/font]\n"
                )
            except:
                logging.info(keys)
                shows = str(keys)

            items = SmoothLabel(
                text=(shows),
                size_hint_x=0.5,
                # font_name="Roboto-Regular",
                markup=True,
                # font_size="10dp",
            )
            # if data["name"] == "Wear The Hat":
            self.root.current_screen.ids["ach_info_id"].add_widget(items)
        # if data["name"] == "Hustle and Grind":
        # self.root.current_screen.ids["ach_info_id"].add_widget(items)

    def rainbow(self):
        # hex_colormap
        logging.info(
            dir(hex_colormap), x, self.theme_cls.secondaryColor, "what is this color"
        )
        # return self.theme_cls.secondaryColor

    def ach_reset(self):
        logging.info("reset ach")
        import libs.lib_ach

        libs.lib_ach.make_ach(ad)
        App.get_running_app().root.current_screen.ids["ach_points"].text = (
            "Points: " + str(0)
        )

        self.trophys("all")

    def check_ach(self):
        logging.info("checking ach")
        import libs.lib_ach
        import libs.lib_score

        # dicts = self.load_paychecks()
        libs.lib_ach.check_scroll(self, ad, x)
        libs.lib_ach.check_hats(self, ad)

        points = App.get_running_app().root.current_screen.ids["ach_points"].text

        junk, points = str.split(points, " ")
        logging.info(points, "POINTSITES")
        libs.lib_score.submit(x["name"], points, 0, ad)

        self.trophys("all")

    def trophys(self, select):
        # global i
        # import lib_test
        # lib_test.n22()
        from kivymd.icon_definitions import md_icons

        self.root.push("ach")
        self.root.current_screen.ids["ach_id"].clear_widgets()
        import libs.lib_ach

        icons = list(md_icons.keys())

        data = libs.lib_ach.list_ach(ad, select)
        points = 0
        for i in range(len(data)):
            # logging.info(data[i])
            tt = data[i]["name"] + "\n" + data[i]["disc"] + "[size=0]" + str(i)
            # self.root.current_screen.ids["ach_id"].add_widget(
            #    ListItemWithCheckbox(
            #        text=tt, icon=icons[i], icon2=icons[i + 10], secondary_text="lalala"
            #    )
            # )
            real_icon = icons[i]
            if data[i]["achieved"] == "False":
                real_icon = "lock"
            if data[i]["achieved"] == "True":
                real_icon = data[i]["ach_icon"]
            items = TwoLineAvatarListItem22(
                text=data[i]["name"],
                secondary_text=data[i]["disc"],
                icon=real_icon,
                on_release=lambda x, y=data[i]: self.ach_info(y),
            )
            if data[i]["ach_level"] > 0:
                points = points + data[i]["ach_level"]

            # items.text_color = (1, 0, 0, 0)
            # items.icon_color = [1, 1, 0, 1]
            # items = items.text_color = self.theme_cls.text_color
            self.root.current_screen.ids["ach_id"].add_widget(items)
            App.get_running_app().root.current_screen.ids["ach_points"].text = (
                "Points: " + str(points)
            )

    def make_stats(self, start, b, e):
        self.root.push("stats")
        """
        if start == "ytde":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if start == "yeare":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if start == "custome":
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if start == "alle":
            App.get_running_app().root.current_screen.ids[
                "syear"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sytd"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            """

        from kivy.utils import get_color_from_hex

        # self.root.current = "stats"
        # self.root.current("stats")
        # self.root.push("stats")
        # self.root.current = "stats"

        self.root.current_screen.ids["graphs"].clear_widgets()
        import libs.lib_makegraphs as lib_makegraphs

        if start == "custom":
            # new_finish = App.get_running_app().root.current_screen.ids["dstart"].text
            # new_start = App.get_running_app().root.current_screen.ids["dend"].text
            # new_finish = pp_date = datetime.datetime.strptime(new_finish, "%Y-%m-%d")
            # new_start = pp_date = datetime.datetime.strptime(new_start, "%Y-%m-%d")
            new_finish = e
            new_start = b
            # logging.info(type(e), "GARBAGE")
        if start == "all":
            new_finish = datetime.datetime.now() - datetime.timedelta(days=10365)
            new_start = datetime.datetime.now()
            App.get_running_app().root.current_screen.ids["dstart"].text = str("ALL")
            App.get_running_app().root.current_screen.ids["dend"].text = str("ALL")
        if start == "ytd":
            doy = datetime.datetime.now().timetuple().tm_yday
            new_finish = datetime.datetime.now() - datetime.timedelta(days=doy)
            new_start = datetime.datetime.now()
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                new_finish.date()
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                new_start.date()
            )
        if start == "year":
            now = datetime.datetime.now()
            three_yrs_ago = datetime.datetime.now() - datetime.timedelta(days=365)
            new_start = now
            new_finish = three_yrs_ago
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                new_finish.date()
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                new_start.date()
            )
        # logging.info(new_finish - new_start)
        (
            dd,
            dd2,
            maxd,
            maxm,
            max_dy,
            max_my,
            ins,
            outs,
            shows,
            max_t,
        ) = lib_makegraphs.parsepp(self, ad, "check", new_start, new_finish)

        lib_makegraphs.make_stats_pp(self, "Checks", dd, maxm, max_dy)

        lib_makegraphs.make_stats_pp(self, "$/Day", dd2, maxd, max_dy)
        dumb = str(f"In ~ Show ~ Out\n" + str(ins) + " " + str(shows) + " " + str(outs))
        dumb = str(f"In ~ Show ~ Out\n" + str(ins) + " " + str(shows) + " " + str(outs))
        dumb = f"In  ~  Out  ~  Show\n{ins:<4}{outs:>8}{shows:>14}"

        lib_makegraphs.make_stats_pp(
            self,
            dumb,
            [[0, ins], [1, shows], [2, outs]],
            max_t,
            3,
        )

        self.root.current_screen.ids["graphs"].add_widget(
            SwipeToDeleteItem2(text="wow+0")
        )

        self.root.push("stats")

    def maketransp(self):
        x = self.theme_cls.primary_color
        x[3] = 0.3
        return x

    def menuu(self):
        self.do_login("", useold)

    def test_not(self):
        logging.info(x)
        toast("Success")

        sh = {
            "date": "10/07/2022",
            "time": "07:00",
            "show": "(TMA) MY CHEMICAL ROMANCE - PLACEHOLDER",
        }
        import libs.lib_bonus

        logging.info(x, "dothis)")
        libs.lib_bonus.create_notification(sh, x, False, ad)

    def mainmenuf(self):
        self.root.push("mainmenu")
        # self.root.current_screen.ids["payperiod_list"].clear_widgets()

    def dlpp(self):
        import libs.lib_ppdownloader as lib_ppdownloader

        if x["name"] == "Test McDemo":
            self.snackbarx(str("No Paychecks found for ") + x["name"])
        else:
            paystubs, new = lib_ppdownloader.thinkpp(x, ad)

            logging.info("Downloaded  " + str(new) + " out of  " + str(paystubs))
            self.snackbarx("Downloaded  " + str(new) + " out of  " + str(paystubs))

    def ccc(self):
        logging.info(mjds)
        confable = []
        for i in range(len(mjds)):
            if 1 == 1:
                # if mjds[i].has_key(["confirmable"]):
                if "confirmable" in mjds[i]:
                    z = mjds[i]["confirmable"]
                    logging.info(z)
                    confable.append(mjds[i]["confirmable"])
            # except:
            #    pass
        for i in range(len(confable)):
            logging.info(confable[i], len(confable))
        logging.info(len(confable), "confable")
        #self.snackbar = MDSnackbar(
        #    text="Success!" + str(len(confable)), bg_color=self.theme_cls.primary_color
        #)
        #self.snackbar.open()

    def dialog_close(self, *args):
        for z in range(len(self.dialog2)):
            try:
                self.dialog2[z].dismiss(force=True)
            except:
                logging.info(z, "wow")
            try:
                self.dialog.dismiss(force=True)
            except:
                logging.info(z, "fail")

    gshow = {}

    def animate_money_new(self, y):
        global gshow
        import libs.lib_new

        global x
        xx9 = x
        self.dialog_close()
        logging.info(y, "XXXX9")

        try:
            js = libs.lib_new.get_json_schedule(x, ad)
        except:
            toast("login failed")
            return "fail"
        s = y[2]
        show = js["shows"][s]
        gshow = show
        logging.info(s)
        logging.info(type(js))

        from kivy.clock import Clock

        now = datetime.datetime.now()
        start_time = datetime.datetime.strptime(
            show["date"] + "." + show["time"], "%m/%d/%Y.%H:%M"
        )
        logging.info(start_time, now, type(start_time), type(now), "showdate")
        if start_time < now:
            self.root.push("animate")
        else:
            toast("Unavalable")
            # return
        # logging.info(y, xx9)

        pos = show["pos"]

        qq = libs.lib_readuserdata.readrate(ad, pos)

        App.get_running_app().root.current_screen.ids["moneyinfo"].text = str(qq)

        App.get_running_app().root.current_screen.ids["show"].text = show["show"]
        App.get_running_app().root.current_screen.ids["top"].text = str("call start")
        App.get_running_app().root.current_screen.ids["moneyinfo"].secondary_text = str(
            pos + " rate"
        )
        # zzz = self.root.get_screen("info").ids["lunches"].text
        hours_text = "Rounded Hours"
        self.root.get_screen("animate").ids["moneya"].secondary_text = "Actual Hours"
        self.root.get_screen("animate").ids["moneyb"].secondary_text = "Earned"
        self.root.get_screen("animate").ids[
            "money_pay"
        ].secondary_text = "Earned (Actual)"
        try:
            if int(zzz) == 1:
                hours_text = hours_text + " (-1 Hour Lunch)"
            if int(zzz) == 2:
                hours_text = hours_text + " (-2 Hour Lunches)"
        except:
            pass

        self.root.get_screen("animate").ids["money_r"].secondary_text = hours_text

        # logging.info(dir(self.root.get_screen("info").ids["lunches"]))
        # logging.info(zzz, "zzz")

        Clock.schedule_interval(self.update_label_new, 0.1)

    def animate_money(self):
        from kivy.clock import Clock

        self.root.push("animate")
        pos = mjds[idex]["pos"]
        App.get_running_app().root.current_screen.ids["top"].text = str("call start")
        App.get_running_app().root.current_screen.ids["moneyinfo"].secondary_text = str(
            pos + " rate"
        )
        zzz = self.root.get_screen("info").ids["lunches"].text
        hours_text = "Rounded Hours"
        self.root.get_screen("animate").ids["moneya"].secondary_text = "Actual Hours"
        self.root.get_screen("animate").ids["moneyb"].secondary_text = "Earned"
        self.root.get_screen("animate").ids[
            "money_pay"
        ].secondary_text = "Earned (Actual)"
        try:
            if int(zzz) == 1:
                hours_text = hours_text + " (-1 Hour Lunch)"
            if int(zzz) == 2:
                hours_text = hours_text + " (-2 Hour Lunches)"
        except:
            pass

        self.root.get_screen("animate").ids["money_r"].secondary_text = hours_text

        # logging.info(dir(self.root.get_screen("info").ids["lunches"]))
        # logging.info(zzz, "zzz")

        Clock.schedule_interval(self.update_label, 0.1)

    def update_label_new(self, dt):
        from datetime import datetime
        import libs.lib_readuserdata as lib_extractjson

        xx9 = gshow

        start_time = xx9["date"] + "." + xx9["time"]
        start_time = datetime.strptime(start_time, "%m/%d/%Y.%H:%M")
        pos = xx9["pos"]
        rate = lib_extractjson.readrate(ad, pos)
        try:
            rate = float(rate)
        except:
            rate = 0.00
            logging.info("fail convert")
        # logging.info (rate,'raterate')
        now = datetime.now()
        difff = now - start_time
        difff = int(difff.total_seconds())
        diffs = difff / 3600
        earn = difff * float(rate)
        earn = earn / 3600
        earn = round(earn, 2)

        hours = int(diffs)
        minutes = (diffs * 60) % 60
        seconds = (diffs * 3600) % 60

        newh = "%d:%02d.%02d" % (hours, minutes, seconds)
        rhours = hours
        if minutes < 5:
            rminutes = 0
        if minutes >= 5 and minutes < 35:
            rminutes = 30
        if minutes >= 35:
            rminutes = 0
            rhours = rhours + 1
        # zzz = self.root.get_screen("info").ids["lunches"].text
        # ot_after = float(self.root.get_screen("info").ids["ot_spin"].text)
        ot_after = 8
        try:
            if int(zzz) > 0:
                rhours = rhours - int(zzz)
        except:
            pass
        r_hours = "%d:%02d" % (rhours, rminutes)

        dec_hours = rhours
        if rminutes == 30:
            dec_hours = dec_hours + 0.5
        r_pay = dec_hours * float(rate)
        if dec_hours > ot_after:
            r_pay = ot_after * float(rate)
            ot_hours = dec_hours - ot_after
            r_pay = r_pay + (ot_hours * float(rate) * 1.5)

        r_pay = dec_hours * float(rate)

        # new_text = datetime.datetime.now().strftime("%H:%M:%S")

        # label.text = new_text
        # logging.info(new_text)
        self.root.get_screen("animate").ids["top"].text = str(start_time)
        # self.root.get_screen("animate").ids["moneyinfo"].text = str(
        #    "%.2f" % float(rate)
        # )
        self.root.get_screen("animate").ids["moneya"].text = str(newh)
        self.root.get_screen("animate").ids["moneyb"].text = str(earn)
        self.root.get_screen("animate").ids["money_r"].text = str(r_hours)
        self.root.get_screen("animate").ids["money_pay"].text = str("%.2f" % r_pay)
        # logging.info (r_pay,"RPAY")

    def update_label66(self, dt):
        from datetime import datetime
        import libs.lib_extractjson as lib_extractjson

        start_time = mjds[idex]["date"] + "." + mjds[idex]["time"]
        start_time = datetime.strptime(start_time, "%m/%d/%Y.%H:%M")
        pos = mjds[idex]["pos"]
        rate = lib_extractjson.extract_pos(App, config_file, pos)
        now = datetime.now()
        difff = now - start_time
        difff = int(difff.total_seconds())
        diffs = difff / 3600
        earn = difff * float(rate)
        earn = earn / 3600
        earn = round(earn, 2)

        hours = int(diffs)
        minutes = (diffs * 60) % 60
        seconds = (diffs * 3600) % 60

        newh = "%d:%02d.%02d" % (hours, minutes, seconds)
        rhours = hours
        if minutes < 5:
            rminutes = 0
        if minutes >= 5 and minutes < 35:
            rminutes = 30
        if minutes >= 35:
            rminutes = 0
            rhours = rhours + 1
        zzz = self.root.get_screen("info").ids["lunches"].text
        ot_after = float(self.root.get_screen("info").ids["ot_spin"].text)
        try:
            if int(zzz) > 0:
                rhours = rhours - int(zzz)
        except:
            pass
        r_hours = "%d:%02d" % (rhours, rminutes)

        dec_hours = rhours
        if rminutes == 30:
            dec_hours = dec_hours + 0.5
        r_pay = dec_hours * float(rate)
        if dec_hours > ot_after:
            r_pay = ot_after * float(rate)
            ot_hours = dec_hours - ot_after
            r_pay = r_pay + (ot_hours * float(rate) * 1.5)

        # r_pay = dec_hours * float(rate)

        # new_text = datetime.datetime.now().strftime("%H:%M:%S")

        # label.text = new_text
        # logging.info(new_text)
        self.root.get_screen("animate").ids["top"].text = str(start_time)
        self.root.get_screen("animate").ids["moneyinfo"].text = str(
            "%.2f" % float(rate)
        )
        self.root.get_screen("animate").ids["moneya"].text = str(newh)
        self.root.get_screen("animate").ids["moneyb"].text = str(earn)
        self.root.get_screen("animate").ids["money_r"].text = str(r_hours)
        self.root.get_screen("animate").ids["money_pay"].text = str("%.2f" % r_pay)

    def confirm(self, what):
        fail = self.confirm_real(what)
        old = False
        import libs.lib_readuserdata

        x = libs.lib_readuserdata.readuserdata(App, ad, ios)
        logging.info(x)
        if x["login"] == "False":
            fail = "fail"

        if fail != "fail":
            nf2 = ad + "/realdata.html"
            try:
                with open(nf2, mode="r") as f:
                    for line in f.readlines():
                        # logging.info (line)

                        if "javascript'>alert" in line:
                            old = True
                            l, x = str.split(line, "(")
                            x, l = str.split(x, ")")
                            # logging.info(x)
            except:
                self.snackbarx('fail')
                # if not self.snackbar:
        if old == True:
            self.snackbarx('old')
            self.snackbar.open()
        if fail == "fail":
            self.snackbarx('already confirmed')
        if old == False and fail != "fail":
            self.snackbarx('success')
    def confirm_real(self, what):
        global browser
        import ssl

        ssl.verify = False
        ssl._create_default_https_context = ssl._create_unverified_context
        # logging.info (what)
        # logging.info(len(xxx[idex]))
        try:
            # logging.info(xxx[idex][13])
            pass
        except:
            logging.info("nonconfirm")
            return "fail"
        dg = what
        confirmable = False
        try:
            if "dg" in dg:
                confirmable = True
                # logging.info("trying to confirm " + str(xx9["date"]))
        except:
            logging.info("nonconfirmable you nerd")

        # logging.info(type(browser), "OMGWHATISTHISSTUFF", dg)
        if 1 == 1:
            if 1 == 1:
                try:
                    try:
                        browser.select_form(name="ctl00")
                    except:
                        browser.select_form(nr=0)
                    logging.info("USED OLD BROWSER")
                except:
                    browser = lib_think.openbrowser(ad, x, ios, App)
                    try:
                        browser.select_form(name="ctl00")
                    except:
                        browser.select_form(nr=0)
                    logging.info("USED NEW BROWSER")

                # logging.info(browser, 'browser 1')
                control_t = browser.form.find_control("__EVENTTARGET")
                control_a = browser.form.find_control("__EVENTARGUMENT")
                # logging.info(browser, "browser 2")
                control_t.readonly = False
                control_a.readonly = False

                # control_t.value = str(xxx[idex][13])
                control_t.value = str(dg)
                control_a.value = "Confirm"
                # logging.info(browser, 'browser 3')

                response = browser.submit()
                # logging.info(browser, 'browser 4')
                aa = response.get_data()
                # logging.info(browser, "browser 5")

                aaa = open(ad + "/realdata.html", "wb")
                aaa.write((aa))
                aaa.close()
        # except:
        #    """"""

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def delete_shows(self, what):
        # logging.info (what)
        from os import walk

        dirs = ["pp", "backup", "shows", "future_shows", "custom_shows"]
        g = 0
        f = 0
        for i2 in range(len(dirs)):
            filenames = next(walk(ad + "/" + dirs[i2]), (None, None, []))[
                2
            ]  # [] if no file
            # logging.info(filenames)

            for i in range(len(filenames)):
                os.remove(ad + "/" + dirs[i2] + "/" + filenames[i])
                g = g + 1

        filenames = next(walk(ad + "/"), (None, None, []))[2]  # [] if no file
        for i in range(len(filenames)):
            try:
                os.remove(ad + "/" + filenames[i])
                g = g + 1
            except:
                f = f + 1
        toast("deleted " + str(g) + " files, " + str(f) + " failed")
        self.dialog.dismiss()

    def show_delete_dialog(self):
        from kivymd.uix.dialog import MDDialog

        if not self.dialog:
            self.dialog = MDDialog(
                text="Delete All Data?",
                buttons=[
                    MDButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.closeDialog,
                    ),
                    MDButton(
                        text="DELETE",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.delete_shows,
                    ),
                ],
            )
        self.dialog.open()

    def handle_selection(self, selection):
        """
        Callback function for handling the selection response from Activity.
        """
        # self.selection = selection
        logging.info(selection)

    def on_selection(self, *a, **k):
        """
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        """
        App.get_running_app().root.ids.result.text = str(self.selection)

    def delete_demo(self):
        listofdicks = libs.lib_archive.delete_demo_files("/future_shows", ad)
        self.snackbarx("deleted  demo shows")

    def show_archive(self):
        self.root.push("archive")
        z, z1, f1, f2 = self.find_pay_date(self.archive_trim)
        listofdicks = libs.lib_archive.load("/future_shows", ad, f1, f2)
        # ntime='wow'
        ntime = "wow2"
        # color='bob3'
        # show_date='now'
        # logging.info (len(listofdicks),'listofdicks')
        App.get_running_app().root.current_screen.ids["dend"].text = str(z1)
        App.get_running_app().root.current_screen.ids["dstart"].text = str(z)
        self.root.current_screen.ids["archive"].clear_widgets()
        tot_hours = 0
        ot_hours = 0
        reg_hours = 0
        tot_money = 0
        tottime_all = 0
        earnings_all = 0
        bu = ["Current", "Next", "Last", "All", "Custom"]
        bu2 = ["date", "hours", "pay"]
        for z in range(len(listofdicks)):
            three = "Lunches!"
            # logging.info (listofdicks[z],'LISTOFDICKS')
            if listofdicks[z].get("lunches") == None:
                three = "No Lunches"
            else:
                three = listofdicks[z]["lunches"]
                three = ""
            # try:

            if listofdicks[z].get("totaltime") != None:
                tottime_all = tottime_all + listofdicks[z].get("totaltime")
                # logging.info(tottime_all, "tottime_all")
            if listofdicks[z].get("earnings") != None:
                earnings_all = earnings_all + listofdicks[z].get("earnings")
                # logging.info(earnings_all, "earnings_all")

            if listofdicks[z].get("pay") == None:
                allhours, reg, over = self.calc_time(listofdicks[z])
                # logging.info (listofdicks[z]["show"],reg,allhours,over,'OMG')
                money = self.calc_money(listofdicks[z], reg, over)
                listofdicks[z]["hours"] = allhours
                listofdicks[z]["reghours"] = reg
                listofdicks[z]["ot"] = over
                listofdicks[z]["pay"] = money

                self.update_show_single(listofdicks[z])
            else:
                allhours = listofdicks[z]["hours"]
                reg = listofdicks[z]["reghours"]
                over = listofdicks[z]["ot"]
                money = listofdicks[z]["pay"]
            try:
                tot_hours = float(tot_hours) + float(allhours)
            except:
                """"""
            try:
                ot_hours = float(ot_hours) + float(over)
            except:
                """"""
            try:
                reg_hours = float(reg_hours) + float(reg)
            except:
                """"""
            try:
                tot_money = float(tot_money) + float(money)
            except:
                """"""

            if 1 == 2:
                three = "Hours: " + self.only5(allhours)
                if over != "-" and over > 0:
                    three = (
                        three + " Reg: " + self.only5(reg) + " OT: " + self.only5(over)
                    )
                # if money[0]!='0':
                three = three + " $" + str(money)

        for nan in range(len(listofdicks)):
            # logging.info(listofdicks[nan].get(self.archive_sort))
            if listofdicks[nan].get(self.archive_sort) == None:
                listofdicks[nan][self.archive_sort] = 0.0
            if listofdicks[nan][self.archive_sort] == "-":
                listofdicks[nan][self.archive_sort] = 0.0
        if self.archive_sort == "date":
            listofdicks = sorted(
                listofdicks,
                key=lambda i: i[self.archive_sort],
                reverse=self.archive_reverse,
            )
        else:
            listofdicks = sorted(
                listofdicks,
                key=lambda i: i[self.archive_sort],
                reverse=not self.archive_reverse,
            )
        self.root.get_screen("archive").ids.archive.add_widget(
            MDListItem(
                MDListItemLeadingIcon(
                    # icon=self.find_type(i, "type"),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    icon_color=self.theme_cls.onPrimaryColor,
                ),
                MDListItemTrailingIcon(
                    # icon=self.find_type(i, "pos"),
                    icon_color=self.theme_cls.errorColor,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                MDListItemHeadlineText(text=str(len(listofdicks)) + " Shows Total"),
                MDListItemSupportingText(
                    text="Hours: "
                    + str(tottime_all)
                    + "    Earnings: "
                    + str(earnings_all)
                ),
            )
        )
        for z in range(len(listofdicks)):
            # text5="Show: " + str((listofdicks[z]["show"])),
            #    secondary_text="Date: "
            #    + str(listofdicks[z]["date"])
            #    + " Hours: "
            #    + realtime,

            # show_date = datetime.datetime.strptime(date, "%m/%d/%Y")
            ntime = self.ampm(listofdicks[z]["time"])
            hours = ""
            if listofdicks[z].get("totaltime"):
                hours = " Hours: " + str(listofdicks[z].get("totaltime"))
            earnings = ""
            if listofdicks[z].get("earnings"):
                earnings = " Earnings: " + str(listofdicks[z].get("earnings"))
            thing = "Please Set Time"
            if (
                listofdicks[z].get("endtime")
                and listofdicks[z].get("earnings")
                and listofdicks[z].get("totaltime")
            ):
                thing = listofdicks[z]["time"] + "-" + hours + earnings
            self.root.get_screen("archive").ids.archive.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        # icon=self.find_type(i, "type"),
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        icon_color=self.theme_cls.primaryColor,
                    ),
                    MDListItemTrailingIcon(
                        # icon=self.find_type(i, "pos"),
                        icon_color=self.theme_cls.errorColor,
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    ),
                    MDListItemHeadlineText(text=listofdicks[z]["show"]),
                    MDListItemSupportingText(
                        text=listofdicks[z]["date"]
                        + " "
                        + listofdicks[z]["pos"]
                        + " "
                        + listofdicks[z]["type"]
                    ),
                    MDListItemSupportingText(text=thing),
                    # MDListItemHeadlineText(listofdicks[z]['show']),
                    # MDListItemHeadlineText(text=str(len(listofdicks))+' Shows Total'),
                    # MDListItemSupportingText(text=color + show_date + " " + ntime),))
                    # on_release=self.edit_show_details()))
                    on_release=lambda x, y=(listofdicks[z]): self.edit_show_details(y),
                )
            )

    def show_archiveold(self):
        import libs.lib_archive

        logging.info("archive")
        self.root.push("archive")
        # self.archive_sort=1

        logging.info(
            self.archive_sort,
            self.archive_reverse,
            self.archive_trim,
            "archive details",
        )

        z, z1, f1, f2 = self.find_pay_date(self.archive_trim)
        App.get_running_app().root.current_screen.ids["dend"].text = str(z1)
        App.get_running_app().root.current_screen.ids["dstart"].text = str(z)

        if self.archive_reverse == False:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-descending"
            logging.info("acend")
        else:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-ascending"
            logging.info("decend")

        self.root.current_screen.ids["archive"].clear_widgets()
        listofdicks = libs.lib_archive.load("/future_shows", ad, f1, f2)
        listofcustomdicks = libs.lib_archive.load("/custom_shows", ad, f1, f2)
        # listofdicks.update(listofcustomdicks)
        for q in range(len(listofcustomdicks)):
            listofdicks.append(listofcustomdicks[q])

        for nan in range(len(listofdicks)):
            logging.info(listofdicks[nan].get(self.archive_sort))
            if listofdicks[nan].get(self.archive_sort) == None:
                listofdicks[nan][self.archive_sort] = 0.0
            if listofdicks[nan][self.archive_sort] == "-":
                listofdicks[nan][self.archive_sort] = 0.0
        if self.archive_sort == "date":
            listofdicks = sorted(
                listofdicks,
                key=lambda i: i[self.archive_sort],
                reverse=self.archive_reverse,
            )
        else:
            listofdicks = sorted(
                listofdicks,
                key=lambda i: i[self.archive_sort],
                reverse=not self.archive_reverse,
            )
        # logging.info (len(listofdicks),'lenlistofdicts',listofdicks)
        tot_hours = 0
        ot_hours = 0
        reg_hours = 0
        tot_money = 0
        tottime_all = 0
        earnings_all = 0
        bu = ["Current", "Next", "Last", "All", "Custom"]
        bu2 = ["date", "hours", "pay"]

        if self.archive_reverse == False:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-descending"
            logging.info("acend")
        else:
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].icon = "sort-ascending"
            logging.info("decend")

        panel3 = MDListItem(
            text="Shows ",
            # + str((listofdicks[z]["date"])),
            secondary_text="Hours11: ",
            # + str(listofdicks[z]["show"]),
            # + " Hours: "
            # + str(listofdicks[z]["totalhours"]),
            # + " Overtime: "
            # + str(listofdicks[z]["othours"]),
            # tertiary_text="Other Stuff",
            # bg_color=self.theme_cls.bg_dark,
            radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
            on_release=self.edit_show_details,
        )

        self.root.get_screen("archive").ids.archive.add_widget(panel3)
        listofdicks_copy = listofdicks

        if 1 == 1:
            panel = MDListItem(
                text="Show: " + str((listofdicks[z]["show"])),
                secondary_text="Date: "
                + str(listofdicks[z]["date"])
                + " Hours: "
                + realtime,
                # + " Overtime: ",
                # + str(listofdicks[z]["othours"]),
                # tertiary_text=three,
                # bg_color=self.theme_cls.bg_dark,
                radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
                on_release=self.edit_show_details,
            )
            if listofdicks[z].get("hidden") is not True or x["hide_shows"] == False:
                self.root.get_screen("archive").ids.archive.add_widget(panel, z)
        App.get_running_app().root.current_screen.ids["archive"].text = "bla"
        bb = App.get_running_app().root.current_screen.ids["archive"].children
        # logging.info (bb,dir(bb),'BSDF')
        bbl = len(bb)
        bb = bb[bbl - 1]
        bb.text = "Shows!: " + str(bbl - 1)
        # bb.secondary_text = "Hours: " + str(self.format_hours(tottime_all)[0])
        # bb.tertiary_text = "Pay: " + str(self.format_money(earnings_all))
        try:
            ratee = "   Rate: $%.2f" % (tot_money / tot_hours)
            # ratee="    Rate: $"+str(tot_money/tot_hours)
        except:
            ratee = ""
        # bb.secondary_text="Hours: "+str(tot_hours)+"   Reg: "+str(reg_hours) +"   OT: "+str(ot_hours)
        # bb.tertiary_text="$: "+str(tot_money) +ratee

    def calc_money(self, v, h, o):
        if v.get("rate") != None:
            # logging.info (h,o,v['rate'],v['show'],'ALL OF IT')
            try:
                h = float(h)
            except:
                h = 0
            if type(h) == float or type(h) == int:
                rate = float(v["rate"])

                money = float(rate) * h
                try:
                    money2 = money + float(rate) * o * 1.5
                except:
                    # logging.info('noot')
                    money2 = money
                # logging.info (money,money2,'DUMB')

                return money2
            # except:
            #    return '--'
        else:
            logging.info(type(h), v.get("rate"), "hello)")
            return "-"

    def only5(self, v):
        try:
            v = str(v)
            z = str.split(v, ".")
            if z[1] == "0":
                return z[0]
            else:
                return v
        except:
            return str(v)

    def calc_time(self, z):
        from datetime import datetime

        a = ["lunches", "time", "endtime", "ota", "rate"]
        for p in range(len(a)):
            if z.get(a[p]) == None:
                z[a[p]] = 0
        # logging.info (z['time'],z['ota'],z['endtime'],z['rate'],z['lunches'],'TESTTEST')
        starttime = z["time"]
        start = datetime.strptime(starttime, "%H:%M")
        try:
            end = datetime.strptime(z["endtime"], "%H:%M:%S")
        except:
            # logging.info('time not found')
            return ("-", "-", "-")
        try:
            hours = self.conv_time_float(str(start - end))
        except:
            # logging.info (start,end,'STARTEND')
            hours = self.conv_time_float(str(end - start))
            # return('-','-','-')

        # logging.info (hours,'DECIMAL NUMBERS')
        reg_hours = 0
        ot = 0
        hours = float(hours)
        if float(z["lunches"]) > 0:
            hours = hours - float(z["lunches"])
        reg_hours = hours
        if hours > float(z["ota"]):
            reg_hours = float(z["ota"])
            ot = hours - float(z["ota"])
        # logging.info(hours,reg_hours,ot,z['show'])
        return hours, reg_hours, ot

    def conv_time_float(self, value):
        vals = value.split(":")
        t, hours = divmod(float(vals[0]), 24)
        t, minutes = divmod(float(vals[1]), 60)
        minutes = minutes / 60.0
        return hours + minutes

    def edit_show_details(self, b):
        try:
            self.menu.dismiss()
        except:
            pass

        import libs.lib_new
        import libs.lib_positions

        # try:
        flag = False

        show, filee = libs.lib_new.load_archive_json(ad, b)
        flag = True
        if 1 == 1 and flag == False:
            show = b
        # except:
        #    logging.info("old show data")
        #    toast("failed to find show")
        #    return
        self.root.push("editShow")
        z = App.get_running_app().root.current_screen.ids["show"]
        z.text = str(show["show"])
        z2 = App.get_running_app().root.current_screen.ids["show2"]
        z2.text = str(show["date"]) + " " + str(show["time"])
        z3 = App.get_running_app().root.current_screen.ids["show3"]

        three = show["time"]
        try:
            App.get_running_app().root.current_screen.ids["newhoursplus"].text = str(
                show["totaltime"] - int(show["lunches"])
            )

        except:
            App.get_running_app().root.current_screen.ids["newhoursplus"].text = ""
        try:
            App.get_running_app().root.current_screen.ids["earningsl"].text = str(
                show["earnings"]
            )
        except:
            App.get_running_app().root.current_screen.ids["earningsl"].text = ""

        try:
            App.get_running_app().root.current_screen.ids["button5"].text = str(
                show["ota"]
            )
        except:
            App.get_running_app().root.current_screen.ids["button5"].text = "8"

        try:
            App.get_running_app().root.current_screen.ids["button4"].text = str(
                show["lunches"]
            )
        except:
            App.get_running_app().root.current_screen.ids["button4"].text = "550"

        App.get_running_app().root.current_screen.ids["rat"].text = (
            show["pos"] + " Rate"
        )

        try:
            three = thre5e + " " + show["endtime"]
        except:
            logging.info("THREE IS GOOD")
            pass
        z3.text = (
            three
            + "[size=-0]"
            + "%%%"
            + show["date"]
            + "%%%"
            + show["time"]
            + "%%%"
            + show["job"]
            + "%%%"
            + show["show"]
        )

        logging.info(str(z) + "button4")
        za = App.get_running_app().root.current_screen
        id = ["lunches", "endtime", "rate", "user_notes"]
        b5 = ["button4", "newhours", "rate", "user_notes"]

        for q in range(len(id)):
            # if 1 == 1:
            try:
                if str(show[id[q]]) == "":
                    show[id[q]] = "0"
                    if id[q] == "user_notes":
                        show[id[q]] = ""

                za.ids[b5[q]].text = str(show[id[q]])
                logging.info("setting! " + str(str(show[id[q]])) + " to bla")

            except:
                # za.ids[b5[q]].text='?'
                logging.info("not able to set " + id[q])
                za.ids[b5[q]].text = ""
                if id[q] == "rate":
                    logging.info("FINDING RATE RIGHT NOW for " + show["pos"])
                    rate = libs.lib_positions.get_single_rate(ad, show["pos"])
                    logging.info(str(rate), "found the rate for", str(show["pos"]))
                    za.ids[b5[q]].text = str(rate)
                if id[q] == "lunches":
                    # logging.info("setting lunches!!!!")
                    za.ids[b5[q]].text = str(0)
        App.get_running_app().root.current_screen.ids["rat"].text = (
            "%%%"
            + show["date"]
            + "%%%"
            + show["time"]
            + "%%%"
            + show["job"]
            + "%%%"
            + show["show"]
        )
        self.update_show()

    def update_show_single(self, f):
        import libs.lib_new

        try:
            b = (
                "%%%"
                + f["date"]
                + "%%%"
                + f["time"]
                + "%%%"
                + f["job"]
                + "%%%"
                + f["show"]
            )
        except:
            b = "%%%" + f["date"] + "%%%" + f["time"] + "%%%" + f["show"]
        show, fileee = libs.lib_new.load_archive_json(ad, b)
        show["hours"] = f["hours"]
        show["reghours"] = f["reghours"]
        show["ot"] = f["ot"]
        show["pay"] = f["pay"]
        # logging.info ('updated for you')
        libs.lib_new.update_archive_json(ad, show)

    def hide_show(self):
        logging.info("hide_show")
        z = App.get_running_app().root.current_screen
        import libs.lib_new

        show, filee = libs.lib_new.load_archive_json(ad, z.ids["show"].tertiary_text)
        show["hidden"] = True
        libs.lib_new.update_archive_json(ad, show)

    def format_hours(self, time):
        if time == "":
            return "", "", ""

        time = float(time)
        # logging.info(int(time), "zzzzzzzzzzzzzzzz")
        woop = "zz"
        hours = "5"
        minutes = "wow"
        hours = int(time)
        try:
            hours = int(time)
            minutes = int((time * 60) % 60)
            if len(str(minutes)) == 1:
                minutes = "0" + str(minutes)

            seconds = (time * 3600) % 60
            woop = str(hours) + ":" + str(minutes)
        except:
            pass

        return woop, hours, minutes

    def update_show(self):
        z = App.get_running_app().root.current_screen
        import libs.lib_new

        show, filee = libs.lib_new.load_archive_json(ad, z.ids["show3"].text)
        show["endtime"] = z.ids["newhours"].text
        show["lunches"] = z.ids["button4"].text
        show["ota"] = z.ids["button5"].text
        show["rate"] = z.ids["rate"].text
        show["user_notes"] = z.ids["user_notes"].text
        # show['totalhoursplus']=z.ids['totalhours'].text
        # show['total_hours']=z.ids['newhours'].text-show['time']-z.ids['lunches'].text
        # show['ot']=z.ids['ot'].text

        from datetime import datetime

        datetime_str_end = z.ids["newhours"].text
        datetime_str_start = show["time"]
        start = datetime.strptime(datetime_str_start, "%H:%M")
        flag = True
        try:
            end = datetime.strptime(datetime_str_end, "%H:%M")

        except:
            # self.snackbarx("PLEASE SET OUT TIME")
            # end = datetime.strptime("00:00", "%H:%M")
            flag = False
        if flag == True:
            tot = end - start
            end = str(end)
            ehour, eminute, escond = str.split(end, ":")
            eminute = float(eminute) / 60
            junk, ehour = str.split(ehour, " ")
            ehour = str(ehour)
            logging.info(str(eminute) + str(ehour) + "eminute2")
            dtimeout = float(ehour) + float(eminute)
            # -z.ids['lunches']
            # show['rate']=z.ids['rate'].text
            dstart_h, dstart_m = str.split(show["time"], ":")
            dstart_m = float(dstart_m) / 60
            dstart = float(dstart_h) + dstart_m

            show["totaltime"] = dtimeout - dstart
            if show["totaltime"] < 0:
                show["totaltime"] = show["totaltime"] + 24
            logging.info(str(show["totaltime"]) + "titaltime")

            time = show["totaltime"]
            time = show["totaltime"] - int(show["lunches"])
            formatted_hours, junk, junk = self.format_hours(time)
            # logging.info(hours, minutes, "whatttttt")

            App.get_running_app().root.current_screen.ids[
                "newhoursplus"
            ].text = formatted_hours

            # logging.info(show["rate"], (show["totaltime"], float(show["lunches"])), "maths")
            show["earnings"] = float(show["rate"]) * float(
                (show["totaltime"]) - float(show["lunches"])
            )
            otearnings = 0
            if float(
                ((show["totaltime"]) - float(show["lunches"])) > float(show["ota"])
            ):
                ot = float(
                    ((show["totaltime"]) - float(show["lunches"])) - float(show["ota"])
                )
                logging.info(str(ot) + "boo ya, overtime")
                otearnings = float(show["rate"]) * 0.5 * ot
                show["ot"] = ot

            show["earnings"] = show["earnings"] + otearnings
            # show['earnings']=self.format_money(show['earnings'])
            App.get_running_app().root.current_screen.ids[
                "earningsl"
            ].text = str(self.format_money(show["earnings"]))
            logging.info(str(ot) + "boo ya, test")


            # logging.info (timeout,lunches,ota,rate,notes,show,'THISISTHEINFO')

        libs.lib_new.update_archive_json(ad, show)

    def backup_new(self):
        results = "blablabla"
        self.results = "asdfasdfasdf"
        logging.info("backup_omg")
        # filechooser.open_file(on_selection=self.handle_selection)

        out_file = ad + "/result.json"
        with open(out_file, "w") as ofile:
            import json

            json.dump(self.results, ofile, indent=4)

        if platform == "ios":
            self.do_share_ios(out_file, "Some title")
        if platform != "ios":
            filechooser.open_file(on_selection=self.handle_selection)
    def share_android(self,title):
        #https://stackoverflow.com/questions/38983649/kivy-android-share-image
        if platform == 'android':
            from android.storage import primary_external_storage_path
            from jnius import autoclass
            from jnius import cast
            import os
            
            StrictMode = autoclass('android.os.StrictMode')
            StrictMode.disableDeathOnFileUriExposure()
            
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')
            Uri = autoclass('android.net.Uri')
            File = autoclass('java.io.File')

            shareIntent = Intent(Intent.ACTION_SEND)
            shareIntent.setType('"application/pdf"')

            path = os.path.join(primary_external_storage_path(),title)

            imageFile = File(path)
            uri = Uri.fromFile(imageFile)
            parcelable = cast('android.os.Parcelable', uri)
            shareIntent.putExtra(Intent.EXTRA_STREAM, parcelable)

            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(shareIntent)

    def do_share_ios(self, data, title):
        if platform=='ios':
            data='wow'
            data=title
            URL = NSURL.fileURLWithPath_(data)
            UIActivityViewController = autoclass("UIActivityViewController")
            UIcontroller = sharedApplication.keyWindow.rootViewController()
            UIActivityViewController_instance = UIActivityViewController.alloc().init()
            # logging.info(dir(UIActivityViewController_instance))
            activityViewController = UIActivityViewController_instance.initWithActivityItems_applicationActivities_(
                [URL], None
            )
            UIcontroller.presentViewController_animated_completion_(
                activityViewController, True, None
            )
        if platform=='android':
            self.share_android(title)

    def backup(self):
        import os
        import shutil

        nf = os.path.join(ad, "shows2.zip")
        # nf='C:/Users/kw/AppData/Roaming/demo3/shows2.zip'
        try:
            shutil.make_archive(ad + "/show2", "zip", ad + "/shows")

            nfc = ad
            nf2 = os.path.join(nfc, "show2.zip")
            with open(nf2, mode="rb") as f:
                f = f.read()
                logging.info(type(f), "typef")
                f = str(f)
            # logging.info (f)
            return f

        except:
            self.snackbarx('no show files')

    def restorebin(self, x):
        import shutil
        import os

        try:
            # logging.info(x)
            nf2 = os.path.join(ad, "show3.zip")
            # j,x,j=str.split(x,'"')
            # logging.info (x)
            # x=x.encode()
            # logging.info (bytes(x,'utf-8'))
            x = eval(x)

            with open(nf2, mode="wb") as f:
                f.write(x)
            shutil.unpack_archive(nf2, ad + "/shows")
        except:
            self.snackbarx('not valid backup')

    def search_menu(self):
        # scale=2
        show = P()  # Create a new instance of the P class

        popupWindow = Popup(
            title="asdf",
            content=show,
            size_hint=(0.5, 0.5),
            size=(400 * scale, 600 * scale),
            separator_height=1,
            title_size=1,
            background_color=(self.theme_cls.primary_dark),
        )
        # Create the popup window

        popupWindow.open()  # show the popup

    def search(self, x):
        # term=App.get_running_app().root.current_screen.ids['search'].text
        # logging.info(x.text)
        self.do_login(x.text, useold)
        # root.dismiss()

    def set_caption(self, popup):
        self.button.text = popup.content.text

    def get_rate(self):
        if 1 == 1:
            import libs.lib_extractjson as lib_extractjson

            # logging.info(xxx[idex], "get_rate")
            pos = xxx[idex][8]
            rate = lib_extractjson.extract_pos(App, config_file, pos)
            logging.info("rate mofo", rate)
            # App.get_running_app().root.current_screen.ids["rate"].text = str(rate)

            # App.get_running_app().root.current_screen.ids["venue"].text = str(rate)
            # except:
            logging.info("failed to get rate")

            # logging.info(xxx, "get_rate2error3")
            # pass

    def save_rate(self):
        logging.info("save rate")

    def set_rate(self):
        # rate=str(28.5)
        try:
            rate = App.get_running_app().root.current_screen.ids["moneyinfo"].text
        except:
            rate = App.get_running_app().root.current_screen.ids["rate"].text
            pos, junk = str.split(
                App.get_running_app().root.current_screen.ids["rat"].text, " "
            )

        import libs.lib_makeuserdata as lib_makeuserdata

        lib_makeuserdata.makeratefile(ad, rate, pos)
        logging.info("set rate")

    def get_date(self, date):
        """
        :type date: <class 'datetime.date'>
        """
        # return date
        pass

    def create_custom_show(self):
        iid = App.get_running_app().root.current_screen
        notes = iid.ids["user_notes"].text
        end_time = iid.ids["end_time"].text
        start_time = iid.ids["start_time"].text
        location = iid.ids["location"].text
        event = iid.ids["event"].text
        date = iid.ids["start_date"].text

        new_event = {
            "show": event,
            "date": date,
            "location": location,
            "notes:": notes,
            "time": start_time,
            "custom": True,
            "end time": end_time,
            "job": "Custom",
        }
        logging.info("notes,notes", new_event)
        import json

        end_time = str.replace(end_time, ":", "")
        start_time_edit = str.replace(start_time, ":", "")

        fname = date + event + str(start_time_edit)
        fname = str.replace(fname, "\t", "  ")
        try:
            os.mkdir(ad + "/custom_shows")
            with open(ad + "/custom_shows/" + fname + ".json", "w") as outfile:
                json.dump(new_event, outfile, indent=4)
        except:
            with open(ad + "/custom_shows/" + fname + ".json", "w") as outfile:
                json.dump(new_event, outfile, indent=4)

    def set_pp(self, current):
        App.get_running_app().root.current_screen.ids[
            "scustom"
        ].md_bg_color = self.theme_cls.primary_light
        if current == "current":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light

        if current == "last":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if current == "custom":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_light
        if current == "all":
            App.get_running_app().root.current_screen.ids[
                "scustom"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "scurrent"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "slast"
            ].md_bg_color = self.theme_cls.primary_light
            App.get_running_app().root.current_screen.ids[
                "sall"
            ].md_bg_color = self.theme_cls.primary_dark
            App.get_running_app().root.current_screen.ids["dend"].text = str("All")
            App.get_running_app().root.current_screen.ids["dstart"].text = str("All")
        flag = False
        firstdate = datetime.date(2021, 10, 13)
        #:
        now = datetime.datetime.now()
        now = datetime.date.today()
        while flag == False:
            nextdate = firstdate + datetime.timedelta(days=14)
            lastdate = nextdate + datetime.timedelta(days=13)
            if nextdate <= now <= lastdate:
                flag = True
                if current == "current":
                    App.get_running_app().root.current_screen.ids["dstart"].text = str(
                        nextdate
                    )
                    App.get_running_app().root.current_screen.ids["dend"].text = str(
                        lastdate
                    )
                if current == "last":
                    App.get_running_app().root.current_screen.ids["dstart"].text = str(
                        nextdate - datetime.timedelta(days=14)
                    )
                    App.get_running_app().root.current_screen.ids["dend"].text = str(
                        lastdate - datetime.timedelta(days=14)
                    )
            firstdate = nextdate
        if current != "custom":
            self.do_history()

    def show_date_picker(self):
        date_dialog = MDModalDatePicker(mode="range")
        date_dialog.bind(on_ok=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        # App.get_running_app().root.current_screen.ids['send'].md_bg_color= self.theme_cls.primary_light
        # App.get_running_app().root.current_screen.ids['sstart'].md_bg_color= self.theme_cls.primary_light
        # App.get_running_app().root.current_screen.ids['scustom'].md_bg_color= self.theme_cls.primary_dark

    def show_date_picker_norange(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_n, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_cancel(self, instance, value):
        # self.root.ids.date_label.text = "You Clicked Cancel"
        pass

    def on_save_n(self, instance, value, date_range):
        App.get_running_app().root.current_screen.ids["start_date"].text = str(value)
        logging.info("omg!", instance, value)

    def send_dates(self, dates):
        logging.info("SEND DATES,", dates)

    def on_save(self, instance_date_picker):
        date_range = instance_date_picker.get_date()
        from datetime import datetime

        # logging.info(self.root.current, "CURRENT SCREEEEEEN")
        # logging.info(date_range, "wowowow")
        # self.root.ids.date_label.text = str(value)
        # self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        try:
            App.get_running_app().root.current_screen.ids["dstart"].text = str(
                date_range[0]
            )
            App.get_running_app().root.current_screen.ids["dend"].text = str(
                date_range[-1]
            )
        except:
            App.get_running_app().root.current_screen.ids["dstart"].text = str("")
            App.get_running_app().root.current_screen.ids["dend"].text = str("")
        # logging.info(self.root.current, "CURRENT SCREEN===:")
        if self.root.current == "stats":
            # self.make_stats("custom", "custom")
            self.make_stats("custom", date_range[-1], date_range[0])
        if self.root.current == "history":
            self.do_history()
        if self.root.current == "newstats":
            d0 = datetime.combine(date_range[-1], datetime.min.time())
            d1 = datetime.combine(date_range[0], datetime.min.time())

            self.do_new_stats(d1, d0, "Custom")
        if self.root.current == "pay":
            self.lday = datetime.combine(date_range[-1], datetime.min.time())
            self.fday = datetime.combine(date_range[0], datetime.min.time())
            self.do_payperiod("x")
        instance_date_picker.dismiss()

    def updatetext(self, box):
        app = App.get_running_app()
        ad = app.user_data_dir
        debugbox = App.get_running_app().root.current_screen.ids[box].active
        x[box] = debugbox
        logging.info(x[box], box, " SETTINGS TOGGLE")
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    def maps(
        self,
    ):
        bbb = App.get_running_app().root.current_screen.ids["venue"].text
        webbrowser.open("https://www.google.com/maps/search/" + bbb)

    def save(show):
        pass

    def format_textt(self, name):
        name = str.replace(name, "/", "")
        name = str.replace(name, ":", "")
        return name

    def show_time_picker2(self):
        import libs.lib_makeuserdata

        libs.lib_makeuserdata.makeshowfile(App, xxx[idex], config_file, ios)

    def show_time_picker_vertical(self, *args):
        time_picker_vertical = MDTimePickerDialVertical()
        time_picker_vertical.bind(on_ok=self.on_ok)
        time_picker_vertical.open()

    def on_edit_time_picker_input(self, time_picker_input):
        time_picker_input.dismiss()

        # Clock.schedule_once(self.show_time_picker_vertical, 0.2)

    def get_time(self, instance):
        logging.info(instance, dir(instance), "thisisinstance")
        time = instance.time
        # temp = str.split(instance.time, ":")
        # time = temp[0] + ":" + temp[1]
        logging.info(time)

        # App.get_running_app().root.current_screen.ids["newhours"].text = str(time)
        # return time

    def on_ok(self, time_picker_vertical: MDTimePickerDialVertical):
        ttt = time_picker_vertical.time.strftime("%H:%M")

        App.get_running_app().root.current_screen.ids["newhours"].text = str(ttt)
        time_picker_vertical.dismiss()
        self.update_show()

    def get_time_start(self, instance, time):
        temp = str.split(str(time), ":")

        time = temp[0] + ":" + temp[1]
        App.get_running_app().root.current_screen.ids["start_time"].text = str(time)
        return time

    def get_time_end(self, instance, time):
        temp = str.split(str(time), ":")
        time = temp[0] + ":" + temp[1]
        App.get_running_app().root.current_screen.ids["newhours"].text = str(time)
        logging.info(time)
        return time

    def make_info(self, thing):
        return thing

    def on_checkbox_active(self, checkbox, value):
        global x
        if value:
            logging.info(
                "The checkbox", checkbox, "is active", "and", checkbox.state, "state"
            )
            x["usecache"] = "True"
        else:
            logging.info(
                "The checkbox", checkbox, "is inactive", "and", checkbox.state, "state"
            )
            x["usecache"] = "False"
        btnState2 = StringProperty("false")
        lib_updateuserdata.updateuser(x, ad)

    def removeAll(self):
        self.root.current_screen.ids["users_lst"].clear_widgets()

    from typing import Union

    def do_theme(self):
        specific_text_color = ""
        logging.info(x, "pcolor")
        if x["pcolor"] == None:
            x["pcolor"] = "Blue"
        self.root.push("theme")
        self.root.get_screen("theme").ids["pic"].source = self.get_wall("theme")
        self.root.get_screen("theme").ids["button_t"].text = x["pcolor"]
        self.theme_cls.update_theme_colors()
        self.save_theme_picker()

    theme_settings = ""

    def do_old_theme2(self):
        self.root.push("theme_picker")
        self.save_theme_picker()

    def show_theme_picker(self, t):
        global theme_setting
        theme_setting = t

        # theme_dialog = MDThemePicker()
        color_picker = MDColorPicker(size_hint=(0.45, 0.45))
        color_picker.open()
        color_picker.bind(
            on_select_color=self.on_select_color,
            # on_select_color=self.on_select_color,
            on_release=self.get_selected_color,
        )

    # on_release=(lambda a: self.grabText(ttt)),
    def update_color(self, color: list) -> None:
        # self.root.ids.toolbar.md_bg_color = color
        logging.info(color)

    """
    def get_selected_color(
        self,
        instance_color_picker: MDColorPicker,
        type_color: str,
        selected_color: Union[list, str],
    ):
        

        logging.info(f"Selected color is {selected_color}")
        logging.info(theme_setting)
        self.update_color(selected_color[:-1] + [1])

        if theme_setting == "p":
            self.theme_cls.primary_palette = selected_color

        if theme_setting == "s":
            self.theme_cls.accent_palette = selected_color

        if theme_setting == "d":
            self.theme_cls.theme_style = selected_color
        # s = self.theme_cls.theme_style
        # p = self.theme_cls.primary_palette
        # a = self.theme_cls.accent_palette

        self.save_theme_picker()
    """

    def on_select_color(self, instance_gradient_tab, color: list) -> None:
        """Called when a gradient image is clicked."""

    def save_theme_picker(self):
        s = self.theme_cls.theme_style
        p = self.theme_cls.primary_palette
        # a = self.theme_cls.accent_palette
        a = "CRAP"
        import libs.lib_readuserdata as lib_readuserdata

        x = lib_readuserdata.readuserdata(App, ad, ios)
        # logging.info(s, p, a, x)
        x["pcolor"] = p
        x["scolor"] = a

        try:
            if x["theme2"] == True:
                x["theme"] = "Dark"
            else:
                x["theme"] = "Light"
        except:
            x["theme"] = "Dark"
        self.theme_cls.theme_style = x["theme"]

        # logging.info(s, p, a, x)
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)
        # logging.info(x)

    def change_screen(self, screen, direction):
        self.root.transition.direction = direction
        # self.root.current = screen
        self.root.push(screen)

    def do_pp_sum(self, lala, t):
        if t == "pp":
            # logging.info("cc", lala)
            global pp_index
            pp_index = pp_index + lala
            # logging.info(pp_index, "INDEXXX")
            paydate, payperiod = self.find_pay_date(pp_index)
            # zz=self.find_pay_date(pp_index)
            # logging.info (zz)

            paylist = self.root.get_screen("today").ids["pay1"]
            paylist.text = "Payday:  " + paydate + " "
            paylist2 = self.root.get_screen("today").ids["pay2"]
            paylist.text = "Payperiod: " + payperiod
            self.update_today_pp(pp_index)
        if t == "cal":
            global cal_index
            cal_index = cal_index + lala
            month, year, mmonth = self.find_month(cal_index)
            # logging.info(month, year, "cal in pp")
            self.make_calendar_today(month, year, mmonth)

    def find_month(self, i):
        import datetime
        from dateutil import relativedelta

        # nextdate = now + timedelta(months=i)
        nextdate = datetime.date.today() + relativedelta.relativedelta(months=i)

        # logging.info(i, "FIND MONTH", nextdate)

        callist = self.root.get_screen("today").ids["cal_month"]
        callist.text = nextdate.strftime("%B %Y")
        month = nextdate.strftime("%m")
        year = nextdate.strftime("%Y")
        mmonth = nextdate.strftime("%B")

        # paylist.secondary_text = "Payperiod: " + payperiod
        # return (i, nextdate)
        # logging.info(month, year, "in find month", nextdate)
        return month, year, mmonth

    def load_paychecks(self):
        import glob, os
        from datetime import datetime

        try:
            os.chdir(ad + "/pp")
        except:
            os.mkdir(ad + "/pp")
            os.chdir(ad + "/pp")
        x = 0
        listofdicks = []
        # now = datetime.now()
        # logging.info(self.fday, "now", self.lday)
        from kivy.clock import Clock

        for file in glob.glob("*.html"):
            # logging.info (file)
            import libs.lib_parse as lib_parse

            f1 = datetime.strptime(file, "%m-%d-%Y.html")
            # logging.info (f1,self.fday,self.lday,'LOADPPDates')
            # logging.info (type(f1),type(self.fday),type(self.lday),'LOADPPDates')

            dd, junk, junk, junk, junk, junk = lib_parse.parsepayperiod(
                ad + "/pp/" + file
            )
            if self.fday <= f1 and f1 <= self.lday:
                listofdicks.append(dd)
                x = x + 1
            # logging.info(x)
            # toast("loaded:" + str(x))
            # Clock.schedule_once(self.dumb(x))

        return listofdicks

    def dumb(self, z):
        logging.info(z)

    def check_var(self, x):
        logging.info(x)
        if x == True:
            return "^^"
        else:
            return "vv"

    def spinner_toggle(self):
        logging.info("Spinner Toggle")
        app = self.get_running_app()
        sp = self.sp

        # sp = self.root.current_screen.ids["spinner"]
        if sp == False:
            sp = True
        else:
            sp = False

    def do_payperiod_trim(self, sort, page):
        if self.sort_pp == sort:
            self.rreverse = not self.rreverse
        if self.sort_search == sort:
            self.reverse_search = not self.reverse_search

        # Clock.schedule_once()
        if page == "pp":
            self.sort_pp = sort
            self.do_payperiod("x")
        if page == "search":
            self.sort_search = sort
            self.display_search(self)
        ## Clock.schedule_once(self.do_payperiod())

    def do_reverse_all(self, sort, screen):
        # logging.info (sort,screen,'SORT AND SCREEN')
        if self.archive_reverse == self.archive_reverse:
            # logging.info("omg its equal")
            self.archive_reverse = not self.archive_reverse
        self.show_archive()

    def do_sort_all(self, date_rng, screen):
        self.archive_sort = date_rng

        self.show_archive()

    def do_trim_all(self, trim, screen):
        # logging.info (sort,'trimall',self.archive_sort)
        self.archive_trim = trim

        self.show_archive()

    def do_payperiod_f(self, date_rng):
        ssort = self.sort_pp
        fdate, ldate = self.get_dates(date_rng)
        # logging.info(fdate, ldate, self.rreverse, ssort, "do_payperiod")
        self.lday = ldate
        self.fday = fdate
        self.date_range_pp = date_rng

        self.do_payperiod("None")
        return fdate, ldate

    def toggle_any(self, stat):
        if x[stat] == False:
            x[stat] = True
            # toast("Hide Personal Data")
        else:
            x[stat] = False
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)

    def toggle_hidden(self):
        if x["hidden"] == False:
            x["hidden"] = True
            # toast("Hide Personal Data")
        else:
            x["hidden"] = False
            # toast("Show Personal Data")
        logging.info("toggle_hidden", x["hidden"])
        import libs.lib_updateuserdata as lib_updateuserdata

        lib_updateuserdata.updateuser(x, ad)
        self.root.push("pay")
        self.prep_stats()

    def do_payperiod(self, zz):
        self.root.push("pay")
        self.root.get_screen("today").ids["pic"].source = self.get_wall("theme")
        # from kivymd.uix.list import ThreeLineListItem
        logging.error(zz)

        ssort = self.sort_pp
        rreverse = self.rreverse
        logging.info(str(rreverse) + "REVERSE")

        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        listofdicks = self.load_paychecks()
        listofdicks = sorted(listofdicks, key=lambda i: i[ssort], reverse=rreverse)

        bu = ["YTD", "Year", "All", "Custom"]
        bu2 = ["paydate", "moneytotal", "totalhours"]

        App.get_running_app().root.current_screen.ids["dstart"].text = (
            self.format_date(self.fday, "full") + "     to"
        )

        App.get_running_app().root.current_screen.ids["dend"].text = self.format_date(
            self.lday, "full"
        )
        hours = 0
        ot = 0
        pay = 0
        reg = 0
        checks=0
        # print(listofdicks[0])
        for bb in range(len(listofdicks)):
            reg = reg + float((listofdicks[bb]["reghours"]))
            ot = ot + float((listofdicks[bb]["othours"]))
            hours = hours + float((listofdicks[bb]["totalhours"]))
            pay = pay + float(listofdicks[bb]["moneytotal"])
        if len(listofdicks)>0:
            per = ot / reg

            per = per * 100
            per = round(per, 2)
        else:
            per=0
        # print(per, "percc")

        self.root.get_screen("pay").ids.payperiod_list.add_widget(
            MDListItem(
                MDListItemLeadingIcon(
                    # icon=self.find_type(i, "type"),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    icon_color=self.theme_cls.primaryColor,
                ),
                MDListItemTrailingIcon(
                    # icon=self.find_type(i, "pos"),
                    icon_color=self.theme_cls.errorColor,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                # MDListItemHeadlineText(text=listofdicks[z]["show"]),
                MDListItemHeadlineText(text="Total Checks: " + str(len(listofdicks))),
                MDListItemSupportingText(
                    text="Hours: "
                    + str(hours)
                    + " Regular: "
                    + str(reg)
                    + " OT:"
                    + str(ot)
                ),
                MDListItemSupportingText(text="$" + str(pay) + " OT %" + str(per)),
                MDListItemSupportingText(text="$" + "text6"),
            ),
            # MDListItemHeadlineText(listofdicks[z]['show']),
            # MDListItemHeadlineText(text=str(len(listofdicks))+' Shows Total'),
            # MDListItemSupportingText(text=color + show_date + " " + ntime),))
            # on_release=self.edit_show_details()))
            # on_release=lambda x, y=(listofdicks[z]): self.edit_show_details(y),
        )

        for z in range(len(listofdicks)):
            # logging.info(listofdicks[z])
            perc = float(listofdicks[z]["othours"]) / float(listofdicks[z]["reghours"])
            perc = perc * 100
            perc = round(perc, 2)
            self.root.get_screen("pay").ids.payperiod_list.add_widget(
                MDListItem(
                    MDListItemLeadingIcon(
                        # icon=self.find_type(i, "type"),
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        icon_color=self.theme_cls.primaryColor,
                    ),
                    MDListItemTrailingIcon(
                        # icon=self.find_type(i, "pos"),
                        icon_color=self.theme_cls.errorColor,
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                    ),
                    # MDListItemHeadlineText(text=listofdicks[z]["show"]),
                    MDListItemHeadlineText(
                        text=str(self.format_date(listofdicks[z]["paydate"], "full"))
                    ),
                    MDListItemSupportingText(
                        text="Shows: "
                        + str(listofdicks[z]["shows"])
                        + " Hours: "
                        + str(listofdicks[z]["totalhours"])
                        + " Overtime: "
                        + str(listofdicks[z]["othours"])
                    ),
                    MDListItemSupportingText(
                        text="$"
                        + str(self.hide(listofdicks[z]["moneytotal"]))
                        + " OT %"
                        + str(perc)
                    ),
                    # MDListItemHeadlineText(listofdicks[z]['show']),
                    # MDListItemHeadlineText(text=str(len(listofdicks))+' Shows Total'),
                    # MDListItemSupportingText(text=color + show_date + " " + ntime),))
                    # on_release=self.edit_show_details()))
                    on_release=lambda x, y=(listofdicks[z]): self.do_pay_ind(y),
                )
            )

        # panel = MDList(
        #    text="Paydate: "
        #    + str(self.format_date(listofdicks[z]["paydate"], "full")),
        #    secondary_text="Shows: "
        #    + str(listofdicks[z]["shows"])
        #    + " Hours: "
        #    + str(listofdicks[z]["totalhours"])
        #    + " Overtime: "
        #    + str(listofdicks[z]["othours"]),
        #    tertiary_text="$" + str(self.hide(listofdicks[z]["moneytotal"])),
        #    # bg_color=self.theme_cls.bg_dark,
        #    radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
        #    on_release=self.do_pay_ind,
        # )

        # self.root.get_screen("pay").ids.payperiod_list.add_widget(panel, z)
        # """

    def do_pay_ind(self, b):
        import libs.lib_parse2

        print(str(b["paydate"].date()), "WHAT")

        m = str(b["paydate"].month)

        if len(m) == 1:
            m = "0" + m
        d = str(b["paydate"].day)
        if len(d) == 1:
            d = "0" + d

        # i = str.split(b, " ")
        # d, m, y = str.split(i[1], "/")
        z = libs.lib_parse2.parsepayperiod(
            ad
            + "/pp/"
            + str(m)
            + "-"
            + str(d)
            + "-"
            + str(b["paydate"].year)
            + ".html",
        )
        #print (z,'what is this thing')
        # logging.info(z, "gigigig")
        # for line in o.readlines():
        #    logging.info(line)
        import os

        # logging.info(os.getcwd(), "CWDDDDD")
        os.chdir(cwd)
        # logging.info(os.getcwd(), "CWDDDDD")
        #print (z,'this is the paycheck')

        
        self.root.push("pay_breakdown")
        self.root.current_screen.ids["pay_gigs"].clear_widgets()
        self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(
            MDListItem(
                MDListItemLeadingIcon(
                    # icon=self.find_type(i, "type"),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    icon_color=self.theme_cls.primaryColor,
                ),
                MDListItemTrailingIcon(
                    # icon=self.find_type(i, "pos"),
                    icon_color=self.theme_cls.errorColor,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                # MDListItemHeadlineText(text=listofdicks[z]["show"]),
                MDListItemHeadlineText(text="Date: " + str(z['paydate'])),
                MDListItemSupportingText(
                    text="Hours: "
                    + str(float(z['reghours'])+float(z['othours']))
                    + " Regular: "
                    + str(z['reghours'])
                    + " OT:"
                    + str(z['othours'])
                ),
                #MDListItemSupportingText(text="$" + str(pay) + " OT %" + str(per)),
                #MDListItemSupportingText(text="$" + "text6"),
            ),)
        for i in range(len(z["gigs"])):
            d = z["gigs"][i]
            print (d)
            din, tin = str.split(d["timeIn"], " ")
            junk, monthi, datei = str.split(din, "-")
            h_i, min_i, junk = str.split(tin, ":")

            dout, tout = str.split(d["timeOut"], " ")
            h_o, min_o, junk = str.split(tout, ":")
            junk, montho, dateo = str.split(din, "-")

            hours_nice = "Hours:" + str(d["tot_hours"])
            if float((d["otH"])) > 0:
                hours_nice = hours_nice + " Overtime: " + str(d["otH"])
            time = (
                    monthi
                    + "-"
                    + datei
                    + " "
                    + h_i
                    + ":"
                    + min_i
                    + " -- "
                    + h_o
                    + ":"
                    + min_o
                )
        
            self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(
                    MDListItem(
                        MDListItemLeadingIcon(
                            # icon=self.find_type(i, "type"),
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                            icon_color=self.theme_cls.primaryColor,
                        ),
                        MDListItemTrailingIcon(
                            # icon=self.find_type(i, "pos"),
                            icon_color=self.theme_cls.errorColor,
                            pos_hint={"center_x": 0.5, "center_y": 0.5},
                        ),
                        # MDListItemHeadlineText(text=listofdicks[z]["show"]),
                        MDListItemHeadlineText(
                            text=str(d["show"])
                        ),
                        MDListItemSupportingText(
                            text=time

                        ),
                        MDListItemSupportingText(
                            text=str(hours_nice)
                            #+ " OT %"
                            #+ str(perc)
                        ),
                        # MDListItemHeadlineText(listofdicks[z]['show']),
                        # MDListItemHeadlineText(text=str(len(listofdicks))+' Shows Total'),
                        # MDListItemSupportingText(text=color + show_date + " " + ntime),))
                        # on_release=self.edit_show_details()))
                        #on_release=lambda x, y=(listofdicks[z]): self.do_pay_ind(y),

                    ))

        """
        panel = MDListItem(
            text="Paydate: " + str(z["paydate"]),
            secondary_text="Shows: "
            + str(z["days"])
            + " RegHours: "
            + str(z["reghours"])
            + " Overtime: "
            + str(z["othours"]),
            tertiary_text="$" + str(self.hide(z["grandtotal"])),
            # fourth_text="test",
            #bg_color=self.theme_cls.bg_darkest,
            radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
            # on_release=self.do_pay_ind,
        )

        self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(panel)

        for i in range(len(z["gigs"])):
            d = z["gigs"][i]
            din, tin = str.split(d["timeIn"], " ")
            junk, monthi, datei = str.split(din, "-")
            h_i, min_i, junk = str.split(tin, ":")

            dout, tout = str.split(d["timeOut"], " ")
            h_o, min_o, junk = str.split(tout, ":")
            junk, montho, dateo = str.split(din, "-")

            hours_nice = "Hours:" + str(d["tot_hours"])
            if float((d["otH"])) > 0:
                hours_nice = hours_nice + " Overtime: " + str(d["otH"])
            panel = MDListItem(
                secondary_text=time,
                text=d["show"],
                tertiary_text=hours_nice,
                #bg_color=self.theme_cls.bg_dark,
                radius=[self.c_radius, self.c_radius, self.c_radius, self.c_radius],
                # on_release=self.do_pay_ind,
            )
        """
        #self.root.get_screen("pay_breakdown").ids.pay_gigs.add_widget(panel)

    def do_payperiod2(self, ssort, rreverse):
        self.root.push("pay")
        self.root.current_screen.ids["payperiod_list"].clear_widgets()
        listofdicks = self.load_paychecks()
        # self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text='bla1'))

        # self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd)+'[size='+str(x)))
        # if x<5:
        #    self.root.current_screen.ids["payperiod_list"].add_widget(HistoryItem(text=str(dd['dtext'])+'[size=0]'+str(x)))
        # listofdicks.sort()
        # listofdicks= (sorted(listofdicks, key = lambda i: i['paydate'],reverse=True))
        # listofdicks= (sorted(listofdicks, key = lambda i: i['shows'],reverse=True))
        # listofdicks= (sorted(listofdicks, key = lambda i: i['moneytotal'],reverse=rrverse))
        listofdicks = sorted(listofdicks, key=lambda i: i[ssort], reverse=rreverse)
        moneys = 0
        hourst = 0
        hoursot = 0
        hourstot = 0
        # hourstot=0
        # logging.info(listofdicks)
        i = 0
        for i in range(len(listofdicks)):
            logging.info(listofdicks[i])
            self.root.current_screen.ids["payperiod_list"].add_widget(
                HistoryItem(text=str(listofdicks[i]["dtext"]) + "[size=0]" + str(i))
            )
            moneys = moneys + float(listofdicks[i]["moneytotal"])
            try:
                hourst = hourst + float(listofdicks[i]["reghours"])
            except:
                pass
            try:
                hoursot = hoursot + float(listofdicks[i]["othours"])
            except:
                pass
            try:
                hourstot = hourstot + float(listofdicks[i]["totalhours"])
            except:
                pass

        xy = "Found " + str(i) + " PayStubs "
        if i > 0:
            xyz1 = "Average Paycheck $ " + str(moneys / len(listofdicks))
            xyz2 = "\nAverage Reg Hours: " + str(hourst / len(listofdicks))
            xyz3 = "\nAverage Ot Hours: " + str(hoursot / len(listofdicks))
            xyz4 = "\nAverage Total Hours: " + str((hourstot) / len(listofdicks))
            xyzz = xyz1 + xyz2 + xyz3 + xyz4

            try:
                self.root.current_screen.ids["payperiod_list"].add_widget(
                    HistoryItem(text=xy + "[size=0]" + str(i + 1))
                )

                self.root.current_screen.ids["payperiod_list"].add_widget(
                    HistoryItem(text=xyzz + "[size=0]" + str(i + 2))
                )

            except:
                self.root.current_screen.ids["payperiod_list"].add_widget(
                    HistoryItem(text="No Pay Stubs found!" + "[size=0]" + str(1))
                )
        if i == 0:
            toast("No Paystubs Found")
        # logging.info(moneys, "moneys")

    def do_history(self):
        self.root.push("history")
        self.root.current_screen.ids["history_list"].clear_widgets()
        # self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text='bla'))
        import glob, os

        try:
            os.chdir(ad + "/shows")
        except:
            os.mkdir(ad + "/shows")
            os.chdir(ad + "/shows")
        x = 0

        for file in glob.glob("*.json"):
            x = x + 1
        x = "Found " + str(x) + " Shows "
        # self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=str(x))+'0')
        allshows = []
        # allshows.sort()
        hours = 0
        ot = 0
        pay = 0
        tot = 0

        now = datetime.datetime.now()
        for file in glob.glob("*.json"):
            if 1 == 1:
                import libs.lib_extractjson

                data, pay2, ot2, hours2, tot2, date = libs.lib_extractjson.extract_show(
                    App, file, ad
                )
                logging.info(data, pay2, ot2, hours2, tot2, date, "HOLY CRAP")
                show_date = datetime.datetime.strptime(date, "%m/%d/%Y")
                dstart = App.get_running_app().root.current_screen.ids["dstart"].text
                dend = App.get_running_app().root.current_screen.ids["dend"].text
                # logging.info(show_date.date(), dstart, dend)
                # logging.info(type(show_date.date()), type(dstart), type(dend))
                force = False
                if dstart == "All":
                    dstart = datetime.datetime.strptime("1900", "%Y")
                    dend = datetime.datetime.strptime("2200", "%Y")
                    force = True
                else:
                    # dstart != 'All':
                    # logging.info(dstart, dend, "WF")
                    dstart = datetime.datetime.strptime(dstart, "%Y-%m-%d")
                    dend = datetime.datetime.strptime(dend, "%Y-%m-%d")
                    # logging.info(
                    #    type(show_date.date()), type(dstart.date()), type(dend.date())
                    # )
                # logging.info(data, dstart.date(), dend.date(), show_date.date(), "data66")
                if dstart.date() <= show_date.date() <= dend.date():
                    logging.info(data, "inside the loop")

                    allshows.append(data)
                    pay = pay + pay2
                    ot = ot + ot2
                    hours = hours + hours2
                    tot = tot + tot2

            # except:
            # logging.info("failed to add show")
        self.root.current_screen.ids["history_list"].add_widget(
            HistoryItem(
                text="pay="
                + str(pay)
                + "\nhours="
                + str(hours)
                + "\not="
                + str(ot)
                + "\nTotal Hours="
                + str(tot)
                + "\nTotal Shows="
                + str(len(allshows))
                + "[size=1 sp]***1"
            )
        )
        s = allshows
        s = allshows.sort(reverse=True)
        logging.info(allshows, "allshows")

        for i in range(len(allshows)):
            t = allshows[i] + "[size=1 sp]***" + str(i)
            self.root.current_screen.ids["history_list"].add_widget(HistoryItem(text=t))

    def check_pull_refresh(self, view, grid):
        pass
        """
        max_pixel = 200
        # aa=self.root.get_screen("home").ids['sv']
        # logging.info
        try:
            totwidget = (plus_search) + 2
            action = totwidget
            stupid = view.scroll_y
            max = (view.scroll_y) / totwidget
            max2 = totwidget / view.scroll_y
            max3 = totwidget * view.scroll_y
            junk = 1 * (stupid - 1)
            junk = junk * grid.height
            #logging.info(junk, h / 3, plus_search)
            if (junk) > (h / 3):
                logging.info("overscroll")
                # self.do_login("",useold)
        except:
            logging.info("fail")
            """

        # for id in self.root.get_screen("home").ids:
        # for id in self.root.get_screen("home").ids:

        # logging.info (id)
        # logging.info (view.height,aa.height,aa.pos,aa.size,aa.scroll_distance,dir(aa))

        # to_relative = max_pixel / ( view.height)
        # if view.scroll_y < 1.0 + to_relative or self.refreshing:
        # return

        # self.refresh_data()

    def grabText(self, inst):
        from kivy.core.clipboard import Clipboard

        logging.info(inst, "inst!!!!")

        Clipboard.copy(inst)

        # logging.info("grabtext", inst)

        self.snackbarx("Copied")

    task_list_dialog = None

    def add_task(self, init):
        # for x in range(len(self.dialog.clear_widgets)):
        #    logging.info(self.dialog.items[x])
        # logging.info(dir(self.dialog))
        self.dialog.text = "loser"
        pass

    def poppy(self, v):
        from kivymd.uix.button import MDFlatButton

        from kivymd.uix.dialog import MDDialog

        logging.info("poppy", v)
        if v == "about":
            ttt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            if not self.dialog:
                self.dialog = MDDialog(
                    text=ttt,
                    type="custom",
                    # content_cls=Content(),
                    buttons=[],
                )
        if v == "notes":
            ttt = mjds[idex][v]
            if len(ttt) < 2:
                self.snackbarx('empty')

            if not self.dialog:
                self.dialog = MDDialog(
                    text=ttt,
                    type="custom",
                    # content_cls=Content(),
                    buttons=[
                        MDFlatButton(
                            text="Copy",
                            text_color=self.theme_cls.primary_color,
                            on_release=(lambda a: self.grabText(ttt)),
                        ),
                    ],
                )
        if len(ttt) > 2:
            self.dialog.open()

            self.dialog.text = ttt

    def refresh_data(self):
        logging.info("lol")

    # def check_login(self):
    # good_login=self.do_login('',False)
    # if good_login==True:
    # self.save_login()
    # self.root.current = "home"

    def save_login(self):
        loc = App.get_running_app().root.current_screen.ids["lol"].text
        logging.info(loc, "LOC")
        blank = False
        if loc == "Select Location":
            self.snackbarx("Please Enter Location")
            blank = True
            logging.info(blank, "locc")
        if App.get_running_app().root.current_screen.ids["temail"].text == "":
            self.snackbarx("Please Enter Email")
            blank = True
            logging.info(blank, "emailloc")
        zz = App.get_running_app().root.current_screen.ids

        # logging.info(self.root.ids.pass2,'lolz')
        passw = (
            App.get_running_app().root.current_screen.ids["pass2"].ids["tpassword"].text
        )
        if passw == "":
            self.snackbarx("Please Enter Password")
            blank = True
            logging.info(blank, "passwordloc")
        logging.info(blank, "BLANK")
        success = False
        if blank == False:
            import libs.lib_new

            import libs.lib_enc

            self.root.current = "login"
            x["username"] = App.get_running_app().root.current_screen.ids["temail"].text
            x["usecache"] = False
            x["password"] = str(libs.lib_enc.make_password(passw))
            x["city"] = App.get_running_app().root.current_screen.ids["lol"].text

            import libs.lib_updateuserdata as lib_updateuserdata

            lib_updateuserdata.updateuser(x, ad)
            js = libs.lib_new.make_json_schedule(x, ad)

            try:
                logging.info(js, "JesusCh")
                self.snackbarx(str(js))
                success = True
            except:
                self.snackbarx("login failed...")
                return "fail"
            if success == True:
                self.delete_demo()
                self.root.push("today")
                self.update()
                self.snackbarx(str(js))

    # btnState2 = StringProperty("false")


# Config.set('kivy', 'log_dir', 'your_chosen_log_dir_path')

# filename of the log file
# Config.set('kivy', 'log_name', "anything_you_want_%y-%m-%d_%_.log")

# Keep log_maxfiles recent logfiles while purging the log directory. Set ‘log_maxfiles’ to -1 to disable logfile purging (eg keep all logfiles).
# Config.set('kivy', 'log_maxfiles', 1000)

# minimum log level which is what you need to not see kivy's default info logs
# Config.set("kivy", "log_level", "error")

# apply all these changes
# Config.write()


Demo3App().run()


# Your appId:	d6073280-f7af-4082-8b33-0356d7068f51
# Your appSecret:	073276b2-4940-40f0-87cc-7e4805382cd0
# https://www.highscores.ovh/

##Photo by <a href="https://unsplash.com/@sebastiaanstam?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">sebastiaan stam</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
##Photo by <a href="https://unsplash.com/@fkaregan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Samuel Regan-Asante</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
##Photo by <a href="https://unsplash.com/@nickleejeffries?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Nicholas Jeffries</a> on <a href="https://unsplash.com/s/photos/concert?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>