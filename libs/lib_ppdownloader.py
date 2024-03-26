import os
import mechanize
import ssl
import urllib
import string
import logging


def open_files():
    f = os.listdir("pp")
    logging.info(f)
    logging.info(type(f))
    logging.info(len(f))
    for i in range(1):
        # for i in range(len(f)):

        logging.info(f[i])
        a = open("pp/" + f[i], "r")
        for line in a.readlines():
            # logging.info (line)
            if 'cell-noborder">' in line:
                logging.info(line)


def doublefake():
    global browser
    global response
    logging.info("doublefake")

    url = "http://127.0.0.1:8000/list.html"
    url = urllib.parse.unquote(url)
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.set_handle_equiv(False)

    br.open(url)

    aa = "test2.html"

    g = find_paychecks(str(aa))

    for i in range(len(g)):
        # logging.info (g[i][1])
        try:
            mm = open(g[i][1] + ".htm1l", "r")
            logging.info(g[i][1] + "opened successful")
        except:
            logging.info(g[i][1] + "opened failed")

            try:
                br.select_form(name="ctl00")
            except:
                br.select_form(nr=0)
            control_a = br.form.find_control("__EVENTARGUMENT")
            control_vs = br.form.find_control("__VIEWSTATE")

            control_g = br.form.find_control("__VIEWSTATEGENERATOR")
            control_va = br.form.find_control("__EVENTVALIDATION")

            try:
                br.select_form(name="ctl00")
            except:
                br.select_form(nr=0)

            control_t = br.form.find_control("__EVENTTARGET")

            control_t.readonly = False

            control_t.value = g[i][1]

            response = br.response()
            aa = response.get_data()
            aaa = open(g[i][1] + ".html", "wb")
            aaa.write((aa))
            aaa.close()


def find_paychecks(a, ad):
    # logging.info("find_paychecks")
    # logging.info(a)
    b = open(ad + "/" + a, "r")
    c = []
    for line in b.readlines():
        c.append(line)
    g = []
    logging.info(len(c))
    for d in range(len(c)):
        if 'aystub" href="javascript' in c[d]:
            # logging.info (c[d],'FOUND ONE BOSS!')
            # logging.info(c[d])

            e = str.split(c[d], "'")
            url = e[1]
            f = str.split(c[d + 1], ">")
            # logging.info (len(f))
            if len(f) > 3:
                # logging.info (f[2])
                date, junk = str.split(f[2], "<")
                date = str.replace(date, "/", "-")
                links = (url, date)
                g.append(links)
    return g


def thinkpp(x, ad, kind):
    # logging.info("thinkpp", x)
    import libs.lib_enc

    # USERNAME
    import ssl

    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    ssl._DEFAULT_CIPHERS = "DES-CBC3-SHA"

    # PE_LOGIN = 'http://www.thinkrhino.com/employee/lasvegas/'
    PE_LOGIN = "https://www.thinkrhino.com/employee/lasvegas/index.aspx"

    PE_COUNTRIES = "payperiods.aspx"
    if kind == "sheets":
        PE_COUNTRIES = "timekeeper.aspx"

    pp = "test2.html"
    try:
        aaa = open(ad + "/" + pp, "wb")
    except:
        os.mkdir(ad + "/pp")
        aaa = open(ad + "/" + pp, "wb")
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
    # logging.info (browser)
    # logging.info browser.title

    res = browser.submit()

    aa = res.get_data()
    # logging.info (aa)

    res = browser.open(PE_COUNTRIES)

    aa = res.read()
    # logging.info (aa)

    aaa.write((aa))
    aaa.close()
    g = find_paychecks(pp, ad)

    try:
        browser.select_form(name="ctl00")
    except:
        browser.select_form(nr=0)
    found = 0

    for z in range(len(g)):
        found_flag = False
        # for z in range(2):
        try:
            aaa = open(ad + "/pp" + "/" + g[z][1] + ".html", "r")
            # logging.info("found " + g[z][1])
            found_flag = True
            try:
                lin = ""
                for line in aaa.readlines():
                    lin = line + lin
                if (len(lin)) < 10:
                    found_flag = False
                    logging.info("error in " + g[z][1])
            except:
                found_flag = False

            aaa.close()
        except:
            pass

        if found_flag == False:
            try:
                l = ""
                aaa2 = open(ad + "/pp" + "/" + g[z][1] + ".html", "wb")

            except:
                os.mkdir(ad + "/pp")
                aaa2 = open(ad + "/pp" + "/" + g[z][1] + ".html", "wb")
        if found_flag == False:
            try:
                browser.select_form(name="ctl00")
            except:
                browser.select_form(nr=0)
            control_t = browser.form.find_control("__EVENTTARGET")
            control_t.readonly = False
            # control_t.value='dgResults$ctl02$btn_Paystub'
            control_t.value = g[z][0]
            # logging.info (g[z][0], type(g[z][0]),'gz')
            # logging.info (type(g[z][0]))
            # control_t.value=g[z][0]
            # logging.info (control_t.value,type(control_t.value),'value')

            res = browser.submit()

            request = browser.request
            # logging.info (request.header_items())

            aa = res.get_data()
            aaa2.write((aa))
            logging.info("Downloaded from server " + g[z][1])
            aaa2.close()
            browser.open(PE_COUNTRIES)
            found = found + 1
    return len(g), found


def get_files():
    # logging.info('getting files from live site')
    # think()

    # doublefake()

    think()
    open_files()


def main():
    get_files()


# main()
