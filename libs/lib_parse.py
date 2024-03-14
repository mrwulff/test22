def parsepayperiod(file):
    from datetime import datetime
    from datetime import date

    import re

    from bs4 import BeautifulSoup

    aaa = open(file, "r", encoding="utf8")
    soup = BeautifulSoup(aaa, "html.parser")
    grandtotal = soup.find("span", id="lblGrandTotal")
    paydate = soup.find("span", id="lblPayDate")
    reghours = soup.find("span", id="lblRegHoursTotal")
    othours = soup.find("span", id="lblOTHoursTotal")
    payperiod = soup.find("span", id="lblPayPeriod")
    days = 0
    day = soup.findAll("span", id=re.compile("_ct"))
    ab = soup.find_all("tr")
    in_type = 0
    out_type = 0
    show_type = 0
    positions = []

    fullnj = []
    allday = []
    today = date.today()
    flag1 = False
    flag2 = False
    hhours = []
    for i in range(len(ab)):
        ax = ab[i].find_all("td")
        # for x in range(len(ax)):
        # logging.info (ax[x].get_text(),'AX',x)
        try:
            alldays = [
                ax[5].get_text(),
                ax[11].get_text(),
                ax[4].get_text(),
                ax[13].get_text(),
            ]
            # timein,total,show

            if (ax[1].get_text()) == "SHOW":
                show_type = show_type + 1
            if (ax[1].get_text()) == "OUT":
                out_type = out_type + 1
            if (ax[1].get_text()) == "IN":
                in_type = in_type + 1
            allday.append(alldays)
        except:
            pass
        try:
            xx = ax[2].get_text()
            if flag2 == False:
                if (xx) == "\xa0":
                    flag2 = True

            if flag1 == True and flag2 == False:
                positions.append(xx)
            if xx == "Pos":
                flag1 = True

        except:
            # logging.info(ax, "fail")
            pass
        try:
            hours_worked = (float(ax[7].get_text())) + (float(ax[8].get_text()))
            # logging.info(hours_worked, "hoursworked")
            # hours_worked = int(hours_worked)
            hhours.append([hours_worked, ax[4].get_text(), ax[5].get_text()])
        except:
            # logging.info(ax, "failuresss")
            pass
    # test_list = list(set(positions))
    test_list = positions
    ###TODO
    realday = []
    day_ach = []
    # logging.info(allday,'WHAT')
    for i in range(1, len(allday) - 1):
        # allday[i][0], junk, junk = str.split(allday[i][0], " ")
        # logging.info (allday[i],'allday')
        newallday0, junk, junk = str.split(allday[i][0], " ")
        try:
            junk, allday[i][1] = str.split(allday[i][1], "$")
        except:
            junk, allday[i][1] = str.split(allday[i][3], "$")
        allday[i][1], junk = str.split(allday[i][1], "\n")
        # allday[i][1] = float(allday[i][1])
        newallday = float(allday[i][1])
        try:
            newallday0, junk = str.replace(newallday, ",", "")
        except:
            pass
        dayday = datetime.strptime(newallday0, "%m/%d/%Y")
        delta = today - dayday.date()
        newallday0 = delta.days
        realday.append([delta.days, newallday])
        day_ach.append([delta.days, allday[i][0], allday[i][2]])

    # day=soup.findAll('span', id=re.compile('^post_'))
    days = len(day)
    temp = paydate.text
    temp = str.split(temp, " ")
    temp = temp[3]

    import datetime

    past = False
    dobj = datetime.datetime.strptime(temp, "%m/%d/%Y")
    # logging.info (dobj.day)
    dobj2 = datetime.datetime.strftime(dobj, "%d %b %Y")
    ddelta = date.today() - dobj.date()
    ddelta = ddelta.days

    # lblRegHoursTotal
    # lblOTHoursTotal
    # lblPayPeriod
    # logging.info (grandtotal.text)
    # logging.info (paydate.text)
    # logging.info (grandtotal.text)
    # logging.info (reghours)
    # logging.info (othours)
    # logging.info (paydate.text)
    # ddict=dobjgrandtotal.text
    totalhours = float(reghours.text) + float(othours.text)
    text = (
        "Paydate: "
        + str(dobj2)
        + " "
        + grandtotal.text
        + "\nRegHours: "
        + reghours.text
        + " "
        + "Othours: "
        + othours.text
        + " Shows: "
        + str(days)
    )
    grandtotal = str.replace(grandtotal.text, ",", "")
    grandtotal = str.replace(grandtotal, "$", "")
    grandtotal = float(grandtotal)

    ddict = {
        "paydate": dobj,
        "moneytotal": grandtotal,
        "reghours": reghours.text,
        "othours": othours.text,
        "totalhours": totalhours,
        "shows": days,
        "ddelta": ddelta,
        "dtext": text,
        # "daysago": realday[0],
        "day_ach": day_ach,
        "hours_ach": hhours,
    }
    # logging.info(realday, alldays)

    # logging.info (text)
    show_types = in_type, out_type, show_type
    # logging.info(show_types)
    return ddict, realday, in_type, out_type, show_type, test_list


def format_textt(name):
    name = str.replace(name, "/", "")
    name = str.replace(name, ":", "")
    return name


def parse(sch, ad, usecache, x5):
    import hashlib

    debug = False
    logging.info(ad, "ifadisblankwtf")
    if ad == "":
        ad = "C:\\Users\\kw\\AppData\\Roaming\\demo3\\"
        sch = "C:\\Users\\kw\\AppData\\Roaming\\demo3\\new.html"
        debug = True

    # debug=False
    ios = True

    from logging import NOTSET
    import os
    import json

    #
    appname = ""
    appauthor = "Acme"
    # a= (	(appname, appauthor))
    # a2=open(a,'w')
    # a2.write('test')
    # from os import *

    # ad=config_file
    import libs.lib_createcache
    from bs4 import BeautifulSoup

    global mj
    global mj2
    global mj3

    global l
    global firstName
    global lastName
    mjds = []
    flag_new = False

    l = []

    d = []
    ti = []
    j = []
    s = []
    v = []
    l = []
    l2 = []
    c = []
    ty = []
    p = []
    st = []
    n = []
    tk = []
    pl = []
    p2 = []
    dd = {}
    mj = []
    mj2 = []
    mj3 = []
    joob3 = []
    l2 = []
    try:
        aaa = open(sch, "r", encoding="utf8")
        encoding = "utf8"
    except:
        sch = ad + "/conf.html"
        aaa = open(sch, "r", encoding="utf8")
        encoding = "utf8"

    # ab=aaa.read()
    soup = BeautifulSoup(aaa, "html.parser")
    name = soup.find("span", id="lblEmpName")

    name = str.split(name.get_text(), ", ")
    logging.info(name, "wtfname")
    name = name[1] + " " + name[0]

    nn = soup.find_all("span")
    for i in range(1, len(nn) - 1):
        try:
            realName = nn[i].get_text()
            lastName, firstName = str.split(realName, ", ")
        except:
            """"""
    try:
        logging.info(name.get_text(), "realname")
    except:
        logging.info(nn, "realname")

    ab = soup.find_all("tr")

    fullnj = []
    for i in range(1, len(ab) - 1):
        logging.info("testtest")
        nj = []
        nj2 = {}
        ax = ab[i].find_all("td")

        date = ax[0].get_text()
        time = ax[1].get_text()
        jobid = ax[2].get_text()
        show = ax[3].get_text()
        venue = ax[4].get_text()
        locationclient = ax[5].get_text()
        typeposition = ax[6].get_text()
        details = ax[7].get_text()

        status = ax[8].get_text()
        notes = ax[9].get_text()
        tk = ax[10].get_text()
        conf = ax[11].get_text()

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
            "canceled": False,
            "confirmid": "",
            "lunches": "",
            "endtime": "",
            "is_new": False,
        }
        try:
            {"what": ax[14].get_text()}
            # logging.info(i,ax[14])
        except:
            pass
        try:
            if "dgR" in str(ax[13]):
                xx = str(ax[13])
                f = str.split(xx, '"')
                thisdict["confirmable"] = f[3]
        except:
            pass
        # logging.info ((ax[13]))
        # thisdict={"canceled":  False}
        if len((ax[13].get_text())) > 3:
            can = ax[13]

            # logging.info (can)
            if "Red" in str(can):
                # logging.info ("OMG ITS RED")
                thisdict["canceled"] = True

        mjds.append(thisdict)
        nj.append(ax[0].get_text())
        nj.append(ax[1].get_text())
        nj.append(ax[2].get_text())
        nj.append(ax[3].get_text())
        nj.append(ax[4].get_text())
        nj.append(ax[5].get_text())
        nj.append(ax[6].get_text())
        nj.append(ax[7].get_text())

        nj.append(ax[8].get_text())
        nj.append(ax[9].get_text())
        nj.append(ax[10].get_text())
        nj.append(ax[11].get_text())
        nj.append(ax[12].get_text())
        if "dgR" in str(ax[13]):
            xx = str(ax[13])
            f = str.split(xx, '"')
            nj.append(f[3])

        if i > 0:
            mj3.append(nj)

        fdate = format_textt(thisdict["date"])
        ftime = format_textt(thisdict["time"])
        fshow = format_textt(thisdict["show"])
        fname = fdate + " " + ftime + " " + thisdict["job"] + " " + fshow

        # hash_object = hashlib.sha1(str(thisdict))
        # hex_dig = hash_object.hexdigest()
        # logging.info(hex_dig)
        mystring = str(thisdict)
        hash_object = hashlib.md5(mystring.encode())
        fname = hash_object.hexdigest()

        # thisdict['is_new']=False
        try:
            nf = os.path.join(ad, "future_shows", fname) + ".json"
            x = open(nf, "r")

            thisdict["is_new"] = False
            logging.info("show exists gagagaag")
        except:
            thisdict["is_new"] = True
            flag_new = True
            mystring = str(thisdict)
            hash_object = hashlib.md5(mystring.encode())
            fname = hash_object.hexdigest()

            try:
                with open(ad + "/future_shows/" + fname + ".json", "w") as outfile:
                    json.dump(thisdict, outfile)
            except:
                os.mkdir(ad + "/future_shows")
                with open(ad + "/future_shows/" + fname + ".json", "w") as outfile:
                    json.dump(thisdict, outfile)

    if flag_new == True:
        import libs.lib_bonus

        libs.lib_bonus.cancel_notification()
        for i in range(len(mjds)):
            pass
            libs.lib_bonus.create_notification(mjds[i], x5, False)
            # try:
            #    lib_bonus.create_notification(mjds[i],x5)
            # except:
            #    logging.info ('failed to make notification')

    # for i in range(15,len(ab)-15):
    # logging.info (len(ab))

    for i in range(len(ab)):
        asds = str(ab[i].contents)

        if "input2 name" not in asds:
            l.append((ab[i].get_text()))
        if "input4 name" in asds:
            l.append(str(ab[i]))
    # for z in range(len(mj3)):
    # logging.info (mj3[z])
    if debug == True:
        for i in range(len(mjds)):
            pass
            # logging.info (mjds[i])
    import json

    final = json.dumps(mjds, indent=2)
    # logging.info (final)
    return mj3, mjds, name


if __name__ == "__main__":
    # parse("sch", "ad", False)
    # parsepayperiod("C:/Users/kw/AppData/Roaming/demo3/pp/01-25-2022.html")
    parsepayperiod("C:/Users/twat/AppData/Roaming/demo3/pp/01-25-2022.html")
    parsepayperiod("C:/Users/twat/AppData/Roaming/demo3/pp/11-28-2023.html")
