import logging


def make_json_schedule(x, ad):
    logging.info("make_json_schedule")
    from bs4 import BeautifulSoup
    import libs.lib_updateuserdata

    # import lib_think

    logging.info("asdfasdf", x["usecache"])
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        conf = "/conf.html"
        cache = True
    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        conf = "/realdata.html"
        cache = False
        logging.info("WHY YOU NOT WORK")

    encoding = "utf8"
    logging.info(str(cache) + "CACHE IN NEW")

    if 1 == 1:
        if cache == True:
            logging.info("truecache")
            if x["username"] == "test":
                x["backdoor"] = True
                libs.lib_updateuserdata.updateuser(x, ad)
            if x["username"] == "undo":
                x["backdoor"] = False
                libs.lib_updateuserdata.updateuser(x, ad)
            import libs.lib_createcache

            libs.lib_createcache.createcache(ad, 25)
            z = open(ad + conf, "r", encoding="utf8")

        if cache == False:
            logging.info("cache == false")
            import libs.lib_createcache

            # lib_createcache.createcache(ad, 15)
            good_login = True
            good_login = libs.lib_think.login(ad, x, False, False)
            if good_login == False:
                return False
            z = open(ad + conf, "r", encoding="utf8")

    soup = BeautifulSoup(z, "html.parser")
    try:
        name = soup.find("span", id="lblEmpName")
        # logging.info(name)
    except:
        logging.info("emp not found")
        return
    logging.info(name.get_text() + " YOUR NAME HERE")
    try:
        name = str.split(name.get_text(), ", ")
    except:
        return "Failed to Login (57)]"
    # logging.info(name, "wtfname")
    name = name[1] + " " + name[0]
    x["name"] = name

    libs.lib_updateuserdata.updateuser(x, ad)

    ab = soup.find_all("tr")

    fullnj = []
    alldict = []
    olddict = []
    confirmable = []
    conf_bool = False
    from datetime import datetime

    for i in range(1, len(ab) - 1):
        nj = []
        nj2 = {}
        ax = ab[i].find_all("td")
        # logging.info(ax)
        f3 = "False"
        canceled = False
        old = False
        if "dgR" in str(ax[13]):
            xx = str(ax[13])
            f = str.split(xx, '"')
            f3 = f[3]
            confirmable.append(f3)
            conf_bool = True
        can = ax[13]
        can2 = ax[0]
        # logging.info(can2)
        if "Red" in str(can):
            # logging.info ("OMG ITS RED")
            canceled = True

        show_date = datetime.strptime(ax[0].get_text(), "%m/%d/%Y")
        now = datetime.now()
        if show_date.date() < now.date():
            old = True

        thisdict = {
            "date": ax[0].get_text(),
            "time": ax[1].get_text(),
            "job": ax[2].get_text(),
            "show": ax[3].get_text(),
            "venue": ax[4].get_text(),
            "location": ax[5].get_text(),
            "client": ax[6].get_text(),
            "type": ax[7].get_text(),
            "pos": ax[8].get_text(),
            "details": ax[9].get_text(),
            "status": ax[10].get_text(),
            "notes": ax[11].get_text(),
            "timekeep": ax[12].get_text(),
            "plus": ax[13].get_text(),
            "canceled": canceled,
            "confirmid": "",
            "lunches": "",
            "endtime": "",
            "is_new": False,
            "confirable": f3,
            "old": old,
        }
        if "Turned Down" in thisdict["status"]:
            thisdict["canceled"] = True
        if old == False:
            alldict.append(thisdict)
            # logging.info(old, "OLD")
        if old == True:
            olddict.append(thisdict)
            # logging.info(old, "OLD")
        # logging.info(thisdict, "thisdict")
        update_history(thisdict, ad)

    cconfirmables = {
        "confirmable": conf_bool,
        "num_shows": len(confirmable),
        "shows": confirmable,
    }

    from datetime import datetime

    now = datetime.now()
    s = {
        "name": name,
        "num_shows": len(alldict),
        "old_shows": olddict,
        "shows": alldict,
        "confirmable": conf_bool,
        "num_shows": len(confirmable),
        "confirmables": confirmable,
        "confirmables2": cconfirmables,
        "updated": str(now),
    }
    # logging.info(olddict)

    # logging.info(alldict)
    import json

    json_object = json.dumps(s, indent=4)
    if cache == True:
        x = open(ad + "/jason_show_cache_fake.json", "w")
    if cache == False:
        x = open(ad + "/jason_show_cache_real.json", "w")
    x.write(json_object)
    return "Logged in as " + name


def format_textt(name):
    name = str.replace(name, "/", "")
    name = str.replace(name, ":", "")
    return name


def get_archive_json(ad, thisdict):
    import json

    fname = (
        format_textt(thisdict["date"])
        + " "
        + format_textt(thisdict["time"])
        + " "
        + thisdict["job"]
        + " "
        + format_textt(thisdict["show"])
    )

    # z = open(ad + "/future_shows/" + fname + ".json", "r")
    z = ad + "/future_shows/" + fname + ".json"

    # logging.info(thisdict, "success")
    with open(z) as json_file:
        data = json.load(json_file)
    return data


def update_archive_json(ad, thisdict):
    import json

    try:
        fname = (
            format_textt(thisdict["date"])
            + " "
            + format_textt(thisdict["time"])
            + " "
            + thisdict["job"]
            + " "
            + format_textt(thisdict["show"])
        )

        with open(ad + "/future_shows/" + fname + ".json", "w") as outfile:
            json.dump(thisdict, outfile, indent=4)
    except:
        pass


def load_archive_json(ad, x):
    import json
    import os

    # logging.info (x)
    flag = 0
    job = ""
    d = "future_shows"
    try:
        space = " "
        fname = (
            format_textt(x["date"])
            + space
            + format_textt(x["time"])
            + space
            + x["job"]
            + space
            + format_textt(x["show"])
        )
    except:
        pass
    try:
        junk, date, time, job, show = str.split(x, "%%%")
        space = " "

        fname = (
            format_textt(date)
            + space
            + format_textt(time)
            + space
            + job
            + space
            + format_textt(show)
        )
    except:
        pass
    if job == "Custom":
        d = "custom_shows"
        logging.info(type(show), type(date), "show")
        fname = format_textt(date) + format_textt(show) + format_textt(time)

    # logging.info (x,"WHATTTTT")
    nf = os.path.join(ad, d, fname) + ".json"
    if 1 == 1:
        # try:
        with open(nf) as json_file:
            data = json.load(json_file)
    # except:
    #    data = {}
    return data, nf


def update_history(thisdict, ad):
    import hashlib
    import json
    import os

    # logging.info("omg its history")

    # hash_object = hashlib.md5(show.encode())
    # fname = hash_object.hexdigest()

    # thisdict['is_new']=False
    # logging.info(show, '"SHOW"')
    fname = (
        format_textt(thisdict["date"])
        + " "
        + format_textt(thisdict["time"])
        + " "
        + thisdict["job"]
        + " "
        + format_textt(thisdict["show"])
    )
    try:
        nf = os.path.join(ad, "future_shows", fname) + ".json"
        x = open(nf, "r")

        thisdict["is_new"] = False
    except:
        thisdict["is_new"] = True
        flag_new = True
        mystring = str(thisdict)
        hash_object = hashlib.md5(mystring.encode())
        fname2 = hash_object.hexdigest()

        try:
            with open(ad + "/future_shows/" + fname + ".json", "w") as outfile:
                json.dump(thisdict, outfile, indent=4)
                # json.dump(self.results, ofile, indent=4)
        except:
            os.mkdir(ad + "/future_shows")
            with open(ad + "/future_shows/" + fname + ".json", "w") as outfile:
                json.dump(thisdict, outfile, indent=4)


def get_json_schedule(x, ad):
    # import libs.lib_think

    # logging.info(x["usecache"], "usecache!!!")
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        logging.info("USING CACHE true/false")
        show = "jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        # logging.info("USING Real?", x["refreshreload"])
        show = "jason_show_cache_real.json"
        if (
            x["refreshreload"] == "True"
            or x["refreshreload"] == True
            or x["refreshreload"] == "true"
        ):
            logging.info("forcing new data", type(x["refreshreload"]))
            make_json_schedule(x, ad)
            # good_login = lib_think.login(ad, x, "True", App)
    # logging.info("showasdf", show)
    data = get_json_schedule_2(x, ad, show)
    return data


def get_json_schedule_1(x, ad):
    # import libs.lib_think

    # logging.info(x["usecache"], "usecache!!!")
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        logging.info("USING CACHE DATA OK?")
        show = "jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        # logging.info("USING Real DATA OK?")
        show = "jason_show_cache_real.json"
        if (
            x["refreshreload"] == "True"
            or x["refreshreload"] == True
            or x["refreshreload"] == "true"
        ):
            logging.info("forcing new data from thingys", type(x["refreshreload"]))
            # make_json_schedule(x, ad)
            # good_login = lib_think.login(ad, x, "True", App)
            pass
    data = get_json_schedule_2(x, ad, show)
    return data
def make_menu(self):
    #change_screen('settings', 'left')

    login={"name":'Login',"func": (lambda x: self.change_screen('login', 'left')),'icon':'account-circle','order':2,'disabled':False}
    settings={"name":'Settings',"func": (lambda x: self.do_settings()),'icon':'cog','order':1,'disabled':False}
    field={"name":'Notes',"func": (lambda x: self.view_fieldnotes('')),'icon':'note','order':9,'disabled':False}
    payperiod={"name":'PayChecks',"func": (lambda x: self.do_payperiod_f("YTD")),'icon':'cash-100','order':4,'disabled':True}
    graphs={"name":'Insights',"func": (lambda x: self.prep_stats()),'icon':'chart-areaspline','order':5,'disabled':True}
    search={"name":'Search',"func": (lambda x: self.new_search()),'icon':'magnify','order':100,'disabled':True}
    cloud={"name":'Cloud',"func": (lambda x: self.change_screen('settings', 'left')),'icon':'cloud','order':101,'disabled':True}
    stats={"name":'Stats',"func": (lambda x: self.do_internal_stats()),'icon':'gauge','order':105,'disabled':False}
    exit={"name":'Close',"func": (lambda x: self.close_menu()),'icon':'close-square','order':999,'disabled':False}
    restart={"name":'Restart',"func": (lambda x: self.restart("today")),'icon':'restart','order':101,'disabled':False}
    pos_list={"name":'Position List',"func": (lambda x: self.view_icons("")),'icon':'format-list-bulleted-square','format-list-bulleted-square':101,'disabled':False}
    cloud={"name":'Cloud',"func": (lambda x: self.change_screen('settings', 'left')),'icon':'cloud','order':101,'disabled':True}



        #change_screen('login', 'left')
    menu_items=[]
    menu_items.append(login)
    menu_items.append(settings)
    menu_items.append(field)
    menu_items.append(payperiod)
    menu_items.append(graphs)
    menu_items.append(search)
    menu_items.append(cloud)
    menu_items.append(stats)
    menu_items.append(cloud)
    menu_items.append(pos_list)
    menu_items.append(exit)
    #menu_items.append(restart)
    





    return menu_items

def get_json_schedule_2(x, ad, show):
    import json, os

    # logging.info("get_json_schedule2222")

    if 1 == 1:
        # logging.info("no " + show + "  Createing now")
        # logging.info("forcing new data", type(x["refreshreload"]))
        if x["refreshreload"] == True:
            make_json_schedule(x, ad)
        nf = os.path.join(ad, show)
        # logging.info(nf, "NF lib new")
        try:
            with open(nf) as json_file:
                data = json.load(json_file)
                # logging.info(data)
                # logging.info("LOADED JSON FILE SUPER FAST on second try")
        except:
            try:
                make_json_schedule(x, ad)
                with open(nf) as json_file:
                    data = json.load(json_file)
                    # logging.info(data)
                    logging.info("LOADED JSON FILE SUPER FAST on second try")
            except:
                data = {"num_shows": 0}

    return data


def just_get_json_schedule(x, ad):
    import json, os

    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        logging.info("USING CACHE DATA OK?")
        show = "/jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        # logging.info("USING Real DATA OK?")
        show = "/jason_show_cache_real.json"

    nf = os.path.join(ad, show)

    nf = ad + "/" + show

    # logging.info(nf, ad, "WTF MAN")

    with open(nf) as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":
    # parse("sch", "ad", False)
    from kivy.app import App

    ad = "C:/Users/kw/AppData/Roaming/demo3/"
    import lib_readuserdata

    x = lib_readuserdata.readuserdata("", ad, False)
    get_json_schedule(x, ad)
    # parsepayperiod, ("C:/Users/kw/AppData/Roaming/demo3/pp/")
