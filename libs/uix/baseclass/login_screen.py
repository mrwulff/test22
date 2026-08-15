from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    # changing screens also can be done in python
    # def goto_home_screen(self):
    #     self.manager.goback()
    def on_enter(self):
        self.open_dispatch_portal()

    def open_dispatch_portal(self):
        print("TODO: Launch native WebView")
