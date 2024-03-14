def webviews(App, ad, ios,self):

    from libs.webview import WebView
    #self.browser = WebView('https://www.google.com',
    #                           enable_javascript = True,
    #                           enable_downloads = True,
    #                           enable_zoom = True)
    self.filename=ad+'/realdata.html'
    #self.filename=ad+'/calendar/index.html'

    self.browser = WebView('file://'+self.filename)
    return ('wowzers')