# libs/ios/webview.py

from kivy.utils import platform

if platform == "ios":
    from pyobjus import autoclass

    UIApplication = autoclass("UIApplication")
    WKWebView = autoclass("WKWebView")
    NSURL = autoclass("NSURL")
    NSURLRequest = autoclass("NSURLRequest")

    KWWebViewHelper = autoclass("KWWebViewHelper")


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

        self.load_url(url)
        self.show()

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