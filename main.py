

##KIVY IMPORTS###
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import platform

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
        self.rhino = RhinoClient()
        #self.load_rhino()


        #self.root.push("today")

#       GET USER DATA         x = libs.lib_readuserdata.readuserdata(App, ad, ios)

        logging.info("BUILD COMPLETE")
      
        self.today()
        return self.root

    def today(self):
        logging.info('Starting modern today function')

        self.remote_config = RemoteConfig()
        
        
        self.remote_config.update()
        html=self.rhino.load_cached_html()

        if html is not None:

            parser = RhinoParser(html).parse()
            print(len(parser.shows))
            self.populate_show_cards(parser)
            self.populate_stats(parser)
            today_screen = self.root.get_screen("today")
            today_screen.ids.login_card.opacity = 0
            today_screen.ids.login_card.disabled = True
            today_screen.ids.login_card.height = 0
        else:
            ##do login##
            logging.info ("DOING LOGIN PART #")
            if not self.rhino.has_credentials():
                today_screen = self.root.get_screen("today")
                today_screen.ids.login_card.opacity = 1
                today_screen.ids.login_card.disabled = False
                today_screen.ids.login_card.height = 250

                logging.info("No Rhino credentials found")

                #self.show_login_card()

                return

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

    def update(self):
        app = App.get_running_app()
        ad = app.user_data_dir
        logging.info("UPDATE FUNCTION!")
        print((self.rhino.username,self.rhino.password))
        html=self.rhino.login(self.rhino.username,self.rhino.password)
        self.rhino.save_schedule(ad + "/realdata.html")
        #print (html,'HTML+++')
        html=self.rhino.load_cached_html()
        parser = RhinoParser(html).parse()
        print(len(parser.shows))
        self.populate_show_cards(parser)
        self.populate_stats(parser)

    def populate_show_cards(self,parser):
        print (parser.shows[1].date,"DATE!!")


        cards=["show_card_1","show_card_2","show_card_3"]
        shows = parser.shows
        screen = self.root.get_screen("today")
        for x in range(3):
            screen.ids[cards[x]].show= shows[x].show
            #screen.ids[cards[x]].show= "WTF"

            show_date = datetime.strptime(shows[x].date, "%m/%d/%Y")
            #print (show_date,"SHOWDATE")
            #show_date = show_date.strftime("%A, %m/%d")
            screen.ids[cards[x]].day= show_date.strftime("%A")
            screen.ids[cards[x]].date= show_date.strftime("%B ") + str(show_date.day)
            screen.ids[cards[x]].time= shows[x].time
            screen.ids[cards[x]].position= shows[x].position
            screen.ids[cards[x]].status= shows[x].status
            #print("status_icon =", screen.ids[cards[x]].status_icon)
            if shows[x].status== "Confirmed":
                screen.ids[cards[x]].status_color= "blue"
                screen.ids[cards[x]].status_icon= "check-circle-outline"



            screen.ids[cards[x]].show_class= shows[x].type
            #print("after SET!status_icon =", screen.ids[cards[x]].status_icon)


            badge, title = self.parse_show(shows[x].show)

            screen.ids[cards[x]].show = title
            screen.ids[cards[x]].venue_code = badge

            screen.ids[cards[x]].venue = shows[x].location
            screen.ids[cards[x]].address = shows[x].venue

    def populate_stats(self, js):
        #print (dir(js),"JS INFOs")
        app = App.get_running_app()
        ad = app.user_data_dir
        self.db = RhinoDatabase()
        last_updated = self.db.get_last_updated()
        shows = js.shows
        update = last_updated
        print (update)
        if  update != None:
        
            #old_update = datetime.datetime.strptime(update, "%Y-%m-%d %H:%M:%S.%f")
            old_update=update
            now = datetime.now()
            diff2 = self.time_since(now - old_update)
            next_show = shows[1].date + " " + shows[1].time
            next_show = datetime.strptime(next_show, "%m/%d/%Y %H:%M")
            bb = 0
            nns = now - next_show
            # logging.info('asdfasdf',nns,type(nns),shows)

            while (nns) >= timedelta(0):
                print (next_show,'111')
                next_show = shows[bb+1].date + " " + shows[bb+1].time
                print (next_show,'222')
                next_show = datetime.datetime.strptime(next_show, "%m/%d/%Y %H:%M")
                nns = now - next_show

                bb = bb + 1
            diff3 = humanize.naturaltime(now - next_show)
            screen = self.root.get_screen("today")
            print(screen.ids.keys(),"WHAT!!!!!")
            print(list(screen.ids.keys()))
            screen.ids.update_card.value = diff2[0]
            screen.ids.update_card.title = diff2[1]
            screen.ids.update_card.subtitle = "Tap to update"

        #print (len(shows), "len shows")
            len_shows=str(len(shows))
            
            print (len(js.confirmables),"len confirmables")
            screen.ids.confirmed_card.subtitle= str(len(js.confirmables)) + " Pending"
            if (len(js.confirmables)>0):
                screen.ids.confirmed_card.value= str(len(js.confirmables))
                screen.ids.confirmed_card.title="Pending"
                screen.ids.confirmed_card.subtitle= str("Tap to confirm")
            if (len(js.confirmables)==0):
                screen.ids.confirmed_card.value= len_shows
                screen.ids.confirmed_card.title="Confirmed"
                screen.ids.confirmed_card.subtitle= str("0 Pending")



        
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


Demo3App().run()