

##KIVY IMPORTS###
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform
from kivy.clock import Clock


from kivy.app import App
app = App.get_running_app()
import humanize


###python imports####
from datetime import datetime, timedelta



###custom Libs###
from libs.lib_rhino import RhinoClient
from libs.lib_rhino_models import RhinoParser
from libs.lib_rhino_db import RhinoDatabase
from libs.lib_remote_config import RemoteConfig
from libs.ios.webview import IOSWebView



import libs.lib_enc

###custom kv ####
from widgets.stat_card import StatCard
from widgets.show_card import ShowCard
from widgets.navigation_bar import NavigationBar
from widgets.nav_button import NavButton

from widgets.badge import Badge

from kivy.lang import Builder
Builder.load_file("widgets/stat_card.kv")
Builder.load_file("widgets/show_card.kv")
Builder.load_file("widgets/badge.kv")
Builder.load_file("widgets/navigation_bar.kv")
Builder.load_file("widgets/nav_button.kv")







###kivy School IMoprts
from libs.uix.root import Root


###python imports####
import logging










class Demo3App(MDApp):



    def build(self):
        print ("def BUILD")
        
        self.root = Root()
        self.root.push("today")

        self.theme_cls.theme_style_switch_animation = True
        self.remote_config = RemoteConfig("config.json")
        self.rhino = RhinoClient()
        self.rhino_db = RhinoDatabase()

        print(
            "[DB TEST] ACTUAL DATABASE:",
            self.rhino_db.db_path
        )

        
        #self.dlpp()       #self.load_rhino()

        self.rhino_db.debug_payroll_columns()
        self.rhino_db.debug_insert_payroll_test()        #self.root.push("today")

#       GET USER DATA         x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        logging.info("BUILD COMPLETE")
      
        self.today()
        return self.root

    def today(self):
        logging.info("Starting modern today function")

        self.remote_config = RemoteConfig()
        self.remote_config.update()

        html = self.rhino.load_cached_html()

        if html is None:
            logging.info("[SCHEDULE] No cached Rhino schedule found")

            if not self.rhino.has_credentials():
                today_screen = self.root.get_screen("today")
                today_screen.ids.login_card.opacity = 1
                today_screen.ids.login_card.disabled = False
                today_screen.ids.login_card.height = 250
                logging.info("[SCHEDULE] No Rhino credentials found")
                return

            logging.info("[SCHEDULE] Credentials exist; attempting fresh schedule update")
            try:
                self.update()
            except Exception as exc:
                logging.exception("[SCHEDULE] Automatic refresh failed: %s", exc)
            return

        parser = RhinoParser(html).parse()
        print("[SCHEDULE] Parsed shows:", len(parser.shows))

        # A cached schedule can exist but contain no upcoming shows when
        # the app has not been opened for several days. Refresh it before
        # allowing the UI to assume there are shows.
        if not parser.shows:
            logging.warning("[SCHEDULE] Cached schedule has no upcoming shows")

            if self.rhino.has_credentials():
                logging.info("[SCHEDULE] Attempting automatic Rhino refresh")
                try:
                    parser = self.update()
                except Exception as exc:
                    logging.exception("[SCHEDULE] Automatic refresh failed: %s", exc)

            if parser is None:
                logging.warning("[SCHEDULE] No schedule available after refresh attempt")
                parser = RhinoParser(html).parse()

        self.populate_show_cards(parser)
        self.populate_stats(parser)

        today_screen = self.root.get_screen("today")
        today_screen.ids.login_card.opacity = 0
        today_screen.ids.login_card.disabled = True
        today_screen.ids.login_card.height = 0
    def login(self):
        print ("DOING NEW LOGIN!!!")
        


        if not hasattr(self, "rhino"):
            self.rhino = RhinoClient("lasvegas")


        if platform =="ios":
            self.login_ios()
            #self.update()
        if platform !="ios":
            #print ("OLD LOGIN")
            self.login_other()
        
        #self.root.push("today")
    def login_other(self):
        logging.info("Loading old Login Page")
        #self.root = Root()
        self.root.push("login_other")
    def paystub(self):
        logging.info("Loading Paystub Page")
        #self.root = Root()
        self.root.push("pay")
    def paystub_item(self, payroll_item_id):
        logging.info("Loading Paystub Item Page")

        # Make sure the lazy-loaded screen exists first
        self.root._ensure_screen_loaded("pay_item")

        # Set the item ID BEFORE pushing the screen
        screen = self.root.get_screen("pay_item")
        screen.payroll_item_id = str(payroll_item_id)
        print (payroll_item_id,"PAYROLL ITEM ID")

        # Now navigate to it
        self.root.push("pay_item", "down")
    def save_old_login(self):
        user=App.get_running_app().root.current_screen.ids["temail"].text
        passw = (
            App.get_running_app().root.current_screen.ids["pass2"].text)
        passw = str(libs.lib_enc.make_password(passw))
        print (user,passw,"USER PASS")
        self.rhino.db.save_user_setting("username", user)
        self.rhino.db.save_user_setting("password", passw)
        self.rhino.db.save_user_setting("city", "lasvegas")
        self.update()
    def check_att(self, text):
        return True

    def open_paystub(self, paystub_id):
        self.root._ensure_screen_loaded("pay_breakdown")

        screen = self.root.get_screen("pay_breakdown")
        screen.paystub_id = str(paystub_id)

        self.root.current = "pay_breakdown"
    
    def update(self):
        app = App.get_running_app()
        ad = app.user_data_dir

        logging.info("[SCHEDULE] UPDATE FUNCTION")
        print((self.rhino.username, self.rhino.password))

        html = self.rhino.login(
            self.rhino.username,
            self.rhino.password,
        )

        self.rhino.save_schedule(ad + "/realdata.html")

        html = self.rhino.load_cached_html()

        if html is None:
            raise RuntimeError("[SCHEDULE] Rhino refresh produced no cached HTML")

        parser = RhinoParser(html).parse()
        print("[SCHEDULE] Fresh schedule contains:", len(parser.shows), "upcoming shows")

        # These functions are safe with 0, 1, 2, or 3+ upcoming shows.
        self.populate_show_cards(parser)
        self.populate_stats(parser)

        self.db = RhinoDatabase()
        self.last_updated = self.db.get_last_updated()

        shows = parser.shows + parser.old_shows

        changes = self.db.compare(shows)

        self.db.save_shows(shows)
        self.db.save_changes(changes)

        print(changes["modified"], "changes!!!")

        return parser
    def dlpp(self):
        import os
        import glob
        import logging

        import libs.lib_ppdownloader as lib_ppdownloader
        from libs.paystub_parser import parse_paystub

        app = App.get_running_app()
        ad = app.user_data_dir

        print("[PAY] Starting paystub download")

        credentials = {
            "username": self.rhino.username,
            "password": self.rhino.password,
            "city": self.rhino.city,
        }

        try:
            # --------------------------------------------------
            # DOWNLOAD PAYSTUB HTML FROM RHINO
            # --------------------------------------------------

            paystubs, new = lib_ppdownloader.thinkpp(
                credentials,
                ad,
                "pp",
            )

            logging.info(
                "Downloaded %s new paystubs out of %s",
                new,
                paystubs,
            )

            print(
                f"[PAY] Rhino reports {new} new paystubs "
                f"out of {paystubs}"
            )

            # --------------------------------------------------
            # FIND DOWNLOADED PAYSTUB FILES
            # --------------------------------------------------

            pp_dir = os.path.join(ad, "pp")

            if not os.path.isdir(pp_dir):
                print("[PAY] Paystub directory does not exist:", pp_dir)
                return

            files = sorted(
                glob.glob(
                    os.path.join(pp_dir, "*.html")
                )
            )

            print(
                f"[PAY] Found {len(files)} paystub HTML files"
            )

            if not files:
                print("[PAY] No paystub files found")
                return

            # --------------------------------------------------
            # LOAD CURRENT RHINO SHOWS
            # --------------------------------------------------

            shows = self.db.get_all_shows()

            print(
                f"[PAY] Matching payroll against "
                f"{len(shows)} stored Rhino shows"
            )

            # --------------------------------------------------
            # PARSE + IMPORT
            # --------------------------------------------------

            imported = 0
            new_paystubs = 0
            payroll_lines = 0
            exact = 0
            possible = 0
            unmatched = 0

            for filename in files:

                print(
                    f"[PAY] Processing: "
                    f"{os.path.basename(filename)}"
                )

                try:
                    with open(
                        filename,
                        "r",
                        encoding="utf-8",
                        errors="replace",
                    ) as f:
                        html = f.read()

                    if len(html) < 100:
                        print(
                            "[PAY] Skipping empty/invalid file:",
                            filename,
                        )
                        continue

                    # Parse the HTML into our standard paystub dict.
                    paystub = parse_paystub(html)

                    if not paystub:
                        print(
                            "[PAY] Parser returned nothing:",
                            filename,
                        )
                        continue

                    if not paystub.get("pay_period_start"):
                        print(
                            "[PAY] No pay period found:",
                            filename,
                        )
                        continue

                    if not paystub.get("pay_date"):
                        print(
                            "[PAY] No pay date found:",
                            filename,
                        )
                        continue

                    print(
                        "[PAY] Parsed:",
                        paystub.get("pay_period_start"),
                        "->",
                        paystub.get("pay_period_end"),
                        "| Pay date:",
                        paystub.get("pay_date"),
                    )

                    # --------------------------------------------------
                    # IMPORT INTO PERMANENT DATABASE
                    # --------------------------------------------------

                    result = self.db.import_paystub(
                        paystub,
                        shows,
                    )

                    imported += 1

                    if result["is_new_paystub"]:
                        new_paystubs += 1

                    payroll_lines += result["imported"]
                    exact += result["exact"]
                    possible += result["possible"]
                    unmatched += result["unmatched"]

                    print(
                        "[PAY] Imported:",
                        result["paystub_id"],
                        "| lines:",
                        result["imported"],
                        "| exact:",
                        result["exact"],
                        "| possible:",
                        result["possible"],
                        "| unmatched:",
                        result["unmatched"],
                    )

                except Exception as exc:
                    logging.exception(
                        "[PAY] Failed to import %s",
                        filename,
                    )

            # --------------------------------------------------
            # SUMMARY
            # --------------------------------------------------

            print("")
            print("========== PAY IMPORT COMPLETE ==========")
            print("[PAY] Files processed:", imported)
            print("[PAY] New paystubs:", new_paystubs)
            print("[PAY] Payroll lines:", payroll_lines)
            print("[PAY] Exact matches:", exact)
            print("[PAY] Possible matches:", possible)
            print("[PAY] Unmatched:", unmatched)
            print("=========================================")

            logging.info(
                "Pay import complete: "
                "%s files, %s new paystubs, %s payroll lines",
                imported,
                new_paystubs,
                payroll_lines,
            )

        except Exception as exc:
            logging.exception(
                "[PAY] Paystub download/import failed"
            )

            print(
                "[PAY] ERROR:",
                exc,
            )

    def populate_show_cards(self, parser):
        cards = [
            "show_card_1",
            "show_card_2",
            "show_card_3",
        ]

        shows = list(parser.shows or [])
        screen = self.root.get_screen("today")

        print("[SCHEDULE] populate_show_cards:", len(shows), "shows")

        # First hide every card. This makes 0/1/2-show schedules safe.
        for card_id in cards:
            card = screen.ids[card_id]
            card.opacity = 0
            card.disabled = True

        if not shows:
            print("[SCHEDULE] No upcoming shows to display")
            return

        for x, show in enumerate(shows[:len(cards)]):
            card = screen.ids[cards[x]]

            card.opacity = 1
            card.disabled = False

            card.show = show.show

            try:
                show_date = datetime.strptime(
                    show.date,
                    "%m/%d/%Y",
                )
                card.day = show_date.strftime("%A")
                card.date = (
                    show_date.strftime("%B ")
                    + str(show_date.day)
                )
            except Exception as exc:
                print("[SCHEDULE] Date formatting error:", exc)
                card.day = ""
                card.date = show.date or ""

            card.time = show.time
            card.position = show.position
            card.status = show.status

            if show.status == "Confirmed":
                card.status_color = "blue"
                card.status_icon = "check-circle-outline"

            card.show_class = show.type

            badge, title = self.parse_show(show.show)
            card.show = title
            card.venue_code = badge

            card.venue = show.location
            card.address = show.venue
    def populate_stats(self, js):
        app = App.get_running_app()
        ad = app.user_data_dir

        self.db = RhinoDatabase()
        last_updated = self.db.get_last_updated()

        shows = list(js.shows or [])
        screen = self.root.get_screen("today")

        print("[SCHEDULE] populate_stats:", len(shows), "shows")

        # Zero upcoming shows is a valid state.
        if not shows:
            print("[SCHEDULE] No upcoming shows; skipping next-show stats")

            try:
                screen.ids.update_card.value = "—"
                screen.ids.update_card.title = "No Upcoming Shows"
                screen.ids.update_card.subtitle = "Tap to update"
            except Exception as exc:
                print("[SCHEDULE] update_card error:", exc)

            try:
                screen.ids.confirmed_card.value = "0"
                screen.ids.confirmed_card.title = "Confirmed"
                screen.ids.confirmed_card.subtitle = "0 Pending"
            except Exception as exc:
                print("[SCHEDULE] confirmed_card error:", exc)

            return

        if last_updated is not None:
            now = datetime.now()
            diff2 = self.time_since(now - last_updated)

            # Find the first upcoming show instead of assuming shows[1] exists.
            next_show = None

            for show in shows:
                try:
                    show_dt = datetime.strptime(
                        show.date + " " + show.time,
                        "%m/%d/%Y %H:%M",
                    )

                    if show_dt >= now:
                        next_show = show_dt
                        break
                except Exception as exc:
                    print("[SCHEDULE] Next-show date error:", exc)

            if next_show is not None:
                print("[SCHEDULE] Next show:", next_show)
            else:
                print("[SCHEDULE] No upcoming show found after parsing")

            try:
                screen.ids.update_card.value = diff2[0]
                screen.ids.update_card.title = diff2[1]
                screen.ids.update_card.subtitle = "Tap to update"
            except Exception as exc:
                print("[SCHEDULE] update_card error:", exc)

        len_shows = str(len(shows))

        try:
            confirmables = js.confirmables or []
        except Exception:
            confirmables = []

        print(len(confirmables), "len confirmables")

        try:
            if len(confirmables) > 0:
                screen.ids.confirmed_card.value = str(len(confirmables))
                screen.ids.confirmed_card.title = "Pending"
                screen.ids.confirmed_card.subtitle = "Tap to confirm"
            else:
                screen.ids.confirmed_card.value = len_shows
                screen.ids.confirmed_card.title = "Confirmed"
                screen.ids.confirmed_card.subtitle = "0 Pending"
        except Exception as exc:
            print("[SCHEDULE] confirmed_card error:", exc)
    def history(self):
        print ("HISTORY!@@")
        self.root.push("history")
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

    #main.py  
    def parse_show(self,show):

        
        self.remote_config = RemoteConfig()


        for prefix, venue in self.remote_config.show_prefixes.items():

            if show.startswith(prefix):
                return venue, show[len(prefix):]

        return "", show


    def time_since(self,dt):
        """
        Returns:
            value, title

        Examples:
            ("5", "Minutes Ago")
            ("3", "Hours Ago")
            ("2", "Days Ago")
            ("1", "Week Ago")
            ("4", "Weeks Ago")
            ("7", "Months Ago")
            ("1", "Year Ago")
        """

        from datetime import datetime

        #now = datetime.now()
        delta =  dt

        seconds = int(delta.total_seconds())

        if seconds < 60:
            return "Just", "Updated"

        minutes = seconds // 60
        if minutes < 60:
            return str(minutes), "Minute Ago" if minutes == 1 else "Minutes Ago"

        hours = minutes // 60
        if hours < 24:
            return str(hours), "Hour Ago" if hours == 1 else "Hours Ago"

        days = delta.days
        if days < 7:
            return str(days), "Day Ago" if days == 1 else "Days Ago"

        weeks = days // 7
        if days < 30:
            return str(weeks), "Week Ago" if weeks == 1 else "Weeks Ago"

        months = days // 30
        if days < 365:
            return str(months), "Month Ago" if months == 1 else "Months Ago"

        years = days // 365
        return str(years), "Year Ago" if years == 1 else "Years Ago"

    def changes(self):
        print ("SHOW CHANGES SCREEN!")
        self.root.push("changes")

    def delete_changes_db(self):

        db = RhinoDatabase()
        db.reset_dev()
        db.close()

    def change_screen(self, screen, direction):
        self.root.push(screen, direction)

############ RHINO WEBVIEW LOGIN"""""""""

    def login_ios(self):
        if not hasattr(self, "webview"):
            self.webview = IOSWebView()

        #
        # Show page
        #

        #self.webview.show_url(login_url)
        
        self.webview.show_url(self.rhino.login_url)

        #
        # Wait a bit, then inject JS
        #

        Clock.schedule_once(
            lambda dt: self.webview.run_js_file("thinkrhino.js"),
            2
        )

        #
        # Don't start multiple polling timers
        #

        if not hasattr(self, "_webview_poll"):

            self._webview_poll = Clock.schedule_interval(
                self.check_webview,
                0.2
            )






    def new_login(self):
        print ("DOING NEW LOGIN!!!")
        


        if not hasattr(self, "rhino"):
            self.rhino = RhinoClient("lasvegas")


        if platform =="ios":
            self.login_ios()
            #self.update()
        if platform !="ios":
            #print ("OLD LOGIN")
            pass
        self.root.push("today")


        

    def check_webview(self, dt):

        import json
        from urllib.parse import unquote

        if not hasattr(self, "webview"):
            return

        msg = self.webview.get_message()

        if msg is None:
            return

        print("MESSAGE =", repr(msg))

        #
        # Force to python string
        #

        msg = f"{msg}"

        if not msg.startswith("schedulara://login?"):
            return

        payload = msg.split("?", 1)[1]

        data = json.loads(unquote(payload))

        print("EMAIL =", data["email"])
        print("PASSWORD =", data["password"])
        print("URL =", data["url"])

        #
        # Stop polling
        #

        self._webview_poll.cancel()
        del self._webview_poll

        self.webview.hide()

        import libs.lib_enc
        EMAIL = data["email"]
        PASSWORD = data["password"]

        enc = libs.lib_enc.make_password(PASSWORD)
        print (enc,"ENC!")

        html = self.rhino.login(
            EMAIL,
            enc,
        )
        #print (html,'login result')

        schedule = self.rhino.download_schedule()
        print (schedule,'schedule result')
        app = App.get_running_app()
        ad = app.user_data_dir
        with open(ad + "/realdata.html", "wb") as f:
            f.write(schedule)

        self.rhino.username = EMAIL
        self.rhino.password = libs.lib_enc.make_password(PASSWORD)
        self.rhino.login_url=data["url"]
        return html






    def on_login(
        email,
        password,
        url
    ):
        logging.info("on_login", email, password, url)
    def inject_login_js(self, dt):

        self.webview.inject_js("""
            document.body.style.background = "red";
        """)

        self.webview.inject_js("""
            document.querySelectorAll("section")[1].style.display = "none";
        """)

Demo3App().run()