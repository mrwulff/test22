# libs/rhino.py

import mechanize
import ssl
import certifi
import logging
import libs.lib_enc


_real = ssl.create_default_context

def patched(*args, **kwargs):
    kwargs["cafile"] = certifi.where()
    return _real(*args, **kwargs)
class RhinoClient:

    USER_AGENT = (
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) "
        "Gecko/2008071615 Firefox/3.0.1-1.fc9 Firefox/3.0.1"
    )

        

    def __init__(self):


        self.browser = self._create_browser()

        self.logged_in = False





        self.username = ""
        self.password = ""
        self.city=""
        #self.city = "lasvegas"

        self.usecache = False

        self.pcolor = "Azure"
        self.scolor = "CRAP"

        self.debug = True

        self.theme = "Dark"
        self.theme2 = True

        self.not1 = False
        self.not2 = False
        self.not1time = 0
        self.not2time = 0

        self.sound_effects = "Bang"

        self.refreshreload = False

        self.not_enabled = False

        self.name = ""

        self.login = False

        self.hide_canceled = False
        self.hide_shows = False

        self.today_start = True
        self.twenty = False

        self.bio = False
        self.nick = True
        self.phone = False

        self.button4 = False
        self.hidden = False

        self.onboarding = True

        self.menu_login = True
        self.menu_timesheets = True
        self.menu_settings = True
        self.menu_notes = True
        self.menu_paychecks = True
        self.menu_insights = True
        self.menu_search = True
        self.menu_stats = True
        self.menu_cloud = True
        self.menu_position_list = True
        self.menu_close = True

        self.branding = False

        self.login_url = ""
        self.schedule_url = ""




    def set_city(self, city):

        self.city = city.lower()

        self.login_url = (
            f"https://www.thinkrhino.com/employee/{self.city}/Index.aspx"
        )

        self.schedule_url = (
            f"https://www.thinkrhino.com/employee/{self.city}/Schedule.aspx"
        )

    def open_login_page(self):
        return self.browser.open(self.login_url)


    def _create_browser(self):

        ssl.create_default_context = patched

        ssl.verify = False
        ssl._create_default_https_context = ssl._create_unverified_context

        browser = mechanize.Browser()
        browser._factory._context = ssl._create_unverified_context()

        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)

        browser.addheaders = [
            ("User-agent", self.USER_AGENT)
        ]

        return browser
    def get_schedule(self,x,ad):
        print ('def get_schedule ')
    def login(self, username, encrypted_password):

        if self.browser is None:
            self._create_browser()

        logging.info("Logging into Rhino")

        self.browser.open(self.login_url)

        try:
            self.browser.select_form(name="ctl00")
        except:
            self.browser.select_form(nr=0)

        self.browser["emailaddress"] = username

        self.browser["mypassword"] = libs.lib_enc.r_password(
            encrypted_password
        )

        response = self.browser.submit()

        html = response.get_data()
        text = html.decode("utf-8", errors="ignore")

        #

        # actually verify login here
        #

        success = (
            "View My Schedule" in text
            or "Schedule.aspx" in text
            or "Logout" in text
        )

        
        if success:
            self.logged_in = True
            return html

        self.logged_in = False
        return False
    def download_schedule(self):

        response = self.browser.open(self.schedule_url)

        return response.get_data()
    def save_schedule(self, filename):

        html = self.download_schedule()

        with open(filename, "wb") as f:
            f.write(html)

        return filename