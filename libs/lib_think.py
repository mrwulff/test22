import logging


def login(ad, x, ios, App):
    import mechanize
    import ssl
    import libs.lib_enc

    if ios == True:
        app = App.get_running_app()
        ad = app.user_data_dir
    # logging.info (x)

    logging.debug("using real data")
    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    # logging.info("using real data66")
    logging.info(libs.lib_enc.r_password(x["password"]))
    # logging.info(x["username"])

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_COUNTRIES = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"

    # logging.info(PE_COUNTRIES, "PE_COUNTRIES")
    browser = mechanize.Browser()

    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    # logging.info(PE_LOGIN, "PE_LOGIN")
    if 1 == 1:
        # try:
        browser.open(PE_LOGIN)
        logging.info("browser=open")
    # except:
    # logging.info("using real data669")
    #    return False
    try:
        browser.select_form(name="ctl00")
    except:
        browser.select_form(nr=0)
    # logging.info (x['username'],x['password'])
    # logging.info (type(x['username']),type(x['password']))
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = browser["mypassword"] = libs.lib_enc.r_password(
        x["password"]
    )

    res = browser.submit()

    aa = res.get_data()  # HTML source of the page
    # logging.info (aa)
    full = open(ad + "/fullwebsite.html", "wb")
    full.write(aa)

    res = browser.open(PE_COUNTRIES)

    aa = res.get_data()  # HTML source of the page
    # logging.info (aa)
    b2 = open(ad + "/realdata.html", "wb")
    # logging.info("using real data66")

    b2.write(aa)

    b2.close()
    logging.info("login success")
    return True
    # except:
    #    logging.info ('login failed')
    #    return False


def openbrowser(ad, x, ios, App):
    import ssl
    import os
    import mechanize
    import libs.lib_enc

    ssl.verify = False

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_SCHEDULE = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"

    dir_path = os.path.dirname(os.path.realpath(__file__))
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    browser.open(PE_LOGIN)
    try:
        browser.select_form(name="ctl00")
    except:
        browser.select_form(nr=0)
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = libs.lib_enc.r_password(x["password"])

    res = browser.submit()

    res = browser.open(PE_SCHEDULE)
    return browser


def login_basic(ad, x, App):
    import mechanize
    import ssl
    import libs.lib_enc

    app = App.get_running_app()
    ad = app.user_data_dir
    # logging.info (x)

    # logging.info("using real data")
    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    # logging.info("using real data66")

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_COUNTRIES = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"
    # logging.info("using real data67")
    # USERNAME = c.text
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # aaa=open(dir_path+'/test2.html','wb')
    # global browser
    browser = mechanize.Browser()

    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    logging.info(PE_LOGIN, "PE_LOGIN")
    if 1 == 1:
        # try:
        browser.open(PE_LOGIN)
        logging.info("browser=open")
    # except:
    #    return False
    try:
        browser.select_form(name="ctl00")
    except:
        browser.select_form(nr=0)
    # logging.info (x['username'],x['password'])
    # logging.info (type(x['username']),type(x['password']))
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = browser["mypassword"] = libs.lib_enc.r_password(
        x["password"]
    )

    res = browser.submit()

    res = browser.open(PE_COUNTRIES)

    aa = res.get_data()  # HTML source of the page
    # logging.info (aa)
    b2 = open(ad + "/realdata.html", "wb")

    b2.write(aa)

    b2.close()
    logging.info("login success")
    return True
    # except:
    #    logging.info ('login failed')
    #    return False
