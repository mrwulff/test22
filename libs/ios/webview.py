# libs/ios/webview.py
import os 
from kivy.clock import Clock
from kivy.utils import platform

if platform == "ios":
    from pyobjus import autoclass

    UIApplication = autoclass("UIApplication")
    WKWebView = autoclass("WKWebView")
    NSURL = autoclass("NSURL")
    NSURLRequest = autoclass("NSURLRequest")

    KWWebViewHelper = autoclass("KWWebViewHelper")

    print("FILE",__file__)

    print("OSLISTDIR",os.listdir(os.path.dirname(__file__)))


class IOSWebView:

    def __init__(self):

        self.created = False

        self.view = None
        self.webview = None

        self.helper = None

    # --------------------------------------------------------
    # Create
    # --------------------------------------------------------

    def create(self):
        print ("Creating WebView")

        if self.created:
            return

        app = UIApplication.sharedApplication()
        window = app.keyWindow
        root = window.rootViewController()

        self.view = root.view()

        self.webview = WKWebView.alloc().init()

        bounds = self.view.bounds()

        frame_type = type(self.view.frame())
        frame = frame_type()

        frame.origin.x = 0
        frame.origin.y = 0

        frame.size.width = bounds.size.width
        frame.size.height = bounds.size.height

        self.webview.setFrame_(frame)

        self.helper = KWWebViewHelper.alloc().init()
        print ("NEWDEBUG")
        self.helper = KWWebViewHelper.alloc().init()

        #print(dir(KWWebViewHelper))
        print([x for x in dir(self.helper) if "URL" in x or "url" in x or "take" in x])
        print ("NEWDEBUG_END")
        self.webview.setNavigationDelegate_(self.helper)

        self.created = True

    # --------------------------------------------------------
    # Show
    # --------------------------------------------------------

    def show(self):
        print ("Showing WebView")

        if not self.created:
            self.create()

        self.view.addSubview_(self.webview)
        self.view.bringSubviewToFront_(self.webview)

    # --------------------------------------------------------
    # Hide
    # --------------------------------------------------------

    def hide(self):

        if self.webview:
            self.webview.removeFromSuperview()

    # --------------------------------------------------------
    # Destroy
    # --------------------------------------------------------

    def destroy(self):
        print ("Destroying WebView")

        self.hide()

        self.helper = None
        self.webview = None
        self.view = None

        self.created = False

    # --------------------------------------------------------
    # Load URL
    # --------------------------------------------------------

    def load_url(self, url):
        print ("Loading URL:", url)

        if not self.created:
            self.create()

        nsurl = NSURL.URLWithString_(url)
        request = NSURLRequest.requestWithURL_(nsurl)

        self.webview.loadRequest_(request)

    # --------------------------------------------------------
    # Show URL
    # --------------------------------------------------------

    def show_url(self, url):
        print ("Showing URL:", url)
        self.show()
        self.load_url(url)
        

    # --------------------------------------------------------
    # HTML
    # --------------------------------------------------------

    def load_html(self, html):
        print("loadhtml")
        #
        # We'll implement this once the bridge exists.
        #

    # --------------------------------------------------------
    # JavaScript
    # --------------------------------------------- -----------

    def inject_js(self, js):
        print ("Injecting JS:", js)

        if self.helper:
            self.helper.runJS_script_(self.webview, js)

    def run_js(self, js):

        if self.helper:
            self.helper.runJS_script_(self.webview, js)


    def run_js_file(self, filename):
        here = os.path.dirname(__file__)
        path = os.path.join(here, filename)

        print(path)

        with open(path, "r", encoding="utf-8") as f:
            self.inject_js(f.read())
        print(self.helper.lastURL)

        #print(self.helper.takeLastURL())
        #lastURL
    def get_message(self):
        if not self.helper:
            return None

        msg = self.helper.lastURL

        if msg:
            # Clear it so we don't process it twice
            self.helper.lastURL = None
            return str(msg)

        return None


