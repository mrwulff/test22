def load_full_pp(ad, fil, idex):
    from ndicts import NestedDict
    import json

    with open(ad + "/" + fil) as json_file:
        data = json.load(json_file)
    # logging.info(data, "wtfdata,", type(data), len(data["shows"]))

    # logging.info(fil, idex, "LOADFULLPP")
    if idex == "POS":
        pos_k, pos_v, pos_l = count_pos(data, "pos", False)
    if idex == "TYPE":
        pos_k, pos_v, pos_l = count_pos(data, "class", False)
    if idex == "PCDA":
        pos_v, pos_k, pos_l = count_pc(data, "whole")
    if idex == "CLIENT":
        pos_k, pos_v, pos_l = count_pos(data, "client", True)
        # logging.info(pos_k, pos_v, pos_l,'WTFYOU')
        # a, b, c = shrink2(pos_k, pos_v, pos_l, 5)

    if idex == "VENUE":
        pos_k, pos_v, pos_l = count_pos(data, idex, True)
        # logging.info(pos_k, pos_v, pos_l)
        # a, b, c = shrink2(pos_k, pos_v, pos_l, 5)

    if idex == "TOTAL":
        pos_k, pos_v, pos_l = count_gig(data, "Total")
    if idex == "hours":
        # logging.info ('idex=hours')

        pos_k, pos_v, pos_l, tot = count_pos(data, idex, False)
        logging.info(tot, "WTFYOU")
        return pos_k, pos_v, pos_l, tot

    if idex == "otH":
        (
            pos_k,
            pos_v,
            pos_l,
        ) = count_pos(data, idex, False)
        return (
            pos_k,
            pos_v,
            pos_l,
        )

    if idex == "pos":
        pos_k, pos_v, pos_l = count_pos_future(data, "pos", False)
    if idex == "venue":
        pos_k, pos_v, pos_l = count_pos_future(data, "venue", False)

    if fil == "jason_show_cache_real.json":
        pos_k, pos_v, pos_l = count_pos_future(data, idex, False)

    if idex == "p_rate":
        return data

    return pos_k, pos_v, pos_l


def round_money(x):
    # return round(x / 1000, 1)
    return x


def shrink2(a, b, c, l):
    logging.info(a, b, c, l)


def count_gig(data, uu):
    import collections

    # logging.info(len(data))
    # data = NestedDict(data)
    pos = []
    v22 = []
    k22 = []
    for k, v in data.items():
        for z in range(len(v)):
            # logging.info(v[z], z)
            for k2, v2 in v[z].items():
                # logging.info(k2, v2)
                if k2 == "gigs":
                    num_of_shows_per_pp = len(v2)
                    # logging.info(v2)
                    for m in range(len(v2)):
                        pos.append({"money": v2[m][uu], "date": v2[m]["timeIn"]})
    pos = sorted(pos, reverse=True, key=lambda i: i["date"])
    # logging.info(pos)

    for x in range(len(pos)):
        v22.append(pos[x]["money"])
        k22.append(pos[x]["date"])

    return v22, k22, k22


def count_pc(data, uu):
    import collections
    from datetime import datetime

    pos = []
    pos2 = []
    pos3 = []
    k2 = []
    v2 = []
    l3 = []
    for k, v in data.items():
        # logging.info(v,'vvvv')
        for z in range(len(v)):
            pc = v[z]
            z = pc["paydate"]

            # logging.info (reg,'REGGGG')
            z = datetime.strptime(z, "%m/%d/%Y")
            gg = {"gt": pc["grandtotal"], "pd": z, "pds": z}
            # logging.info(gg,"GG")
            pos.append(gg)
            # pos4.append(pc["grandtotal"])
    # logging.info(pos)

    pos = sorted(pos, reverse=True, key=lambda i: i["pd"])
    # logging.info(pos, "nonsortedyear")

    for x in range(len(pos)):
        k2.append(round_money(pos[x]["gt"]))
        v2.append(pos[x]["pd"])
        temp = " "
        if (x == 0) or x == (len(pos) - 1):
            temp = pos[x]["pds"]
            # logging.info(temp, type(temp), "temp2222")
            temp = temp.strftime("%m/%d/%y")

        l3.append(temp)

    pos_r = []
    # logging.info(l3, "LLLLL3333")

    return (k2, l3, l3)


def count_pos_future(data, uu, shrink):
    import collections

    # logging.info(data, uu, shrink, "THIS IS THE NEW THINGGY")
    # logging.info(len(data))
    cc = []
    for z in range(len(data["shows"])):
        a = data["shows"][z][uu]
        if "MOBILE" in a and "ARENA" in a:
            a = "TMA"
        if "MGM" in a and "ARENA" in a:
            a = "MGM"
        if len(a) > 8:
            a = a[0:6]
        cc.append(a)
    z = collections.Counter(cc)
    # logging.info(z)

    k2 = []
    v2 = []
    v3 = []
    z2 = dict(
        sorted(z.items(), reverse=True, key=lambda item: item[1]),
    )
    for k, v in z2.items():
        # logging.info(k, v)

        if shrink == True:
            logging.info(k)
            if len(k) > 10:
                k = k[0:10]
        v2.append(v)
        k2.append(k)
    zz = (k2, v2)
    # logging.info(zz)
    # logging.info(zz[0][0])
    return k2, v2, v3
    return ("x", "x", "x")


def count_pos(data, uu, shrink):
    import collections

    # logging.info(len(data))
    # data = NestedDict(data)
    # if uu=='VENUE':
    # logging.info (uu,"UUuuu")
    pos = []
    poss = []
    for k, v in data.items():
        added = False
        logging.info(len(v), "lenvvv")
        qwer = len(v)
        for z in range(len(v)):
            # logging.info(len(v),'LENVVVV')
            for k2, v2 in v[z].items():
                # logging.info(k2, v2)
                if k2 == "gigs":
                    num_of_shows_per_pp = len(v2)
                    # logging.info(v2)
                    for m in range(len(v2)):
                        if uu == "VENUE":
                            s = v2[m]["show"]

                            if s[0] == "(":
                                s2 = str.split(s, ")")
                                s2 = str.split(s2[0], "(")
                                # logging.info(s[1])
                                if s2[1] == "TM":
                                    s2[1] = "TMA"
                                pos.append(s2[1])
                                added = True
                            if "vgk" in s.lower() and added == False:
                                pos.append("TMA")
                                added = True
                            if s[0] != "(" and added == False:
                                # logging.info(s, "BLARRRRR")

                                pos.append("?")
                        # logging.info(uu, "UUUUUUUUU")
                        if (
                            uu == "pos"
                            or uu == "class"
                            or uu == "client"
                            or uu == "otH"
                        ):
                            pos.append(v2[m][uu])
                        if uu == "hours":
                            s = v2[m]["tot_hours"]
                            poss.append(s)
                            s = str(s)
                            s = str.split(s, ".")
                            if len(s) < 2:
                                s = 0 + s
                            pos.append(int(s[0]))
                        if uu == "otH":
                            s = v2[m][uu]
                            if float(s) > 1:
                                s = str.split(s, ".")
                                logging.info(s[0], "s000000")
                                s = s[0]
                                s = int(0)

                                pos.append(s)
    # logging.info (pos,'POSSS')
    # pos=str(pos)

    # logging.info(len(pos))
    logging.info(pos, "sssssssssssss")
    z = collections.Counter(pos)
    # logging.info(dir(z))
    logging.info(z, type(z), "zzzzzzz")
    k2 = []
    v2 = []
    v3 = []
    if uu == "otH":
        # logging.info (z)
        z2 = dict(
            sorted(z.items(), reverse=False, key=lambda item: item[1]),
        )

    if uu != "hours":
        z2 = dict(
            sorted(z.items(), reverse=True, key=lambda item: item[1]),
        )
    if uu == "hours":
        # logging.info (z)
        z2 = dict(
            sorted(z.items(), reverse=False, key=lambda item: item[0]),
        )
        # logging.info (z2)
        # logging.info (z2)
    for k, v in z2.items():
        # logging.info(k, v)

        if shrink == True:
            # logging.info(k)
            if len(k) > 6:
                k = k[0:6]
            try:
                k = str.split(k, " ")
                k = k[0]
            except:
                """"""
        if uu == "hours":
            k = str(k)
        v2.append(v)

        k2.append(k)

    zz = (k2, v2)
    # logging.info(zz)
    # logging.info (pos,'posss')
    # logging.info(zz[0][0])
    if uu == "hours":
        return k2, v2, poss, qwer
    return (
        k2,
        v2,
        poss,
    )


def moneyconvert(z):
    # logging.info(z)
    z = str.replace(z, ",", "")
    z = str.replace(z, "$", "")
    try:
        z = float(z)
        # logging.info(z)
    except:
        z = int(z)
    return z


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
    dthours = soup.find("span", id="lblDTHoursTotal")

    reghourst = soup.find("span", id="lblRegPayTotal")
    othourst = soup.find("span", id="lblOTPayTotal")
    dthourst = soup.find("span", id="lblDTPayTotal")

    reghourst = moneyconvert(reghourst.get_text())
    othourst = moneyconvert(othourst.get_text())
    dthourst = moneyconvert(dthourst.get_text())
    grandtotal = moneyconvert(grandtotal.get_text())
    # logging.info g

    payperiod = soup.find("span", id="lblPayPeriod")
    junk, junk, ppstart, junk, ppend = str.split(payperiod.get_text(), " ")
    junk, junk, junk, paydate = str.split(paydate.get_text(), " ")
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
    pp_all = []

    for i in range(len(ab)):
        ax = ab[i].find_all("td")

        # logging.info(len(ax))
        real_show = False
        if len(ax) == 12:
            try:
                # logging.info(ax[5].get_text())
                nIn = datetime.strptime(ax[5].get_text(), "%m/%d/%Y %H:%M:%S %p")
                nOut = datetime.strptime(ax[6].get_text(), "%m/%d/%Y %H:%M:%S %p")
                # logging.info(nIn)
                real_show = True
                total = moneyconvert(ax[11].get_text())
                rate = moneyconvert(ax[10].get_text())
            except:
                nIn = ""
                nOut = ""
                total = ""
                rate = ""

            show = {
                "job": ax[0].get_text(),
                "class": ax[1].get_text(),
                "pos": ax[2].get_text(),
                "client": ax[3].get_text(),
                "show": ax[4].get_text(),
                "timeIn": str(nIn),
                "timeOut": str(nOut),
                "RegH": ax[7].get_text(),
                "otH": ax[8].get_text(),
                "dH": ax[9].get_text(),
                "Rate": rate,
                "Total": total,
            }
            if real_show == True:
                days = days + 1

                show["tot_hours"] = (
                    float(ax[7].get_text())
                    + float(ax[8].get_text())
                    + float(ax[9].get_text())
                )
                pp_all.append(show)
    # logging.info(pp_all)
    pp = {
        "paydate": paydate,
        "ppstart": ppstart,
        "ppend": ppend,
        "reghours": reghours.get_text(),
        "othours": othours.get_text(),
        "dthours": dthours.get_text(),
        "reghourst": reghourst,
        "othourst": othourst,
        "dthourst": dthourst,
        "grandtotal": grandtotal,
        "days": days,
        "gigs": pp_all,
    }
    # logging.info(grandtotal)
    return pp


def parsepayperiod2(file):
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
        try:
            alldays = [ax[5].get_text(), ax[11].get_text(), ax[4].get_text()]
            #

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

    for i in range(1, len(allday) - 1):
        # allday[i][0], junk, junk = str.split(allday[i][0], " ")
        newallday0, junk, junk = str.split(allday[i][0], " ")
        junk, allday[i][1] = str.split(allday[i][1], "$")
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
        "daysago": realday[0],
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

        # libs.lib_bonus.cancel_notification()
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
    ad = "C:/Users/twat/AppData/Roaming/demo3/"
    # parsepayperiod("C:/Users/kw/AppData/Roaming/demo3/pp/04-05-2022.html")
    # a, b, c = load_full_pp(ad, "json_pps.json", "TOTAL")
    a, b, c = load_full_pp(ad, "json_pps.json", "PCDA")
    # a, b, c = load_full_pp(ad, "json_pps.json", "VENUE")

    f = "jason_show_cache_real.json"
    a, b, c = load_full_pp(ad, f, "Hours")
    logging.info(a, b, c)
