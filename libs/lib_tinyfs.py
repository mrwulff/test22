def stats(xxx, now, search):
    import datetime

    cf = 0
    week = 0
    tot = 0
    for i in range(len(xxx) - 1):
        v = xxx[i][10]
        if search.lower() in str(xxx[i]).lower() or len(search) == 0:
            tot = tot + 1
            if v == "Confirmed":
                cf = cf + 1
            dobj = datetime.datetime.strptime(
                xxx[i][0] + "/" + xxx[i][1], "%m/%d/%Y/%H:%M"
            )
            daysaway = dobj.date() - now.date()
            a = int(daysaway.days)
            if a < 7 and a >= 0:
                week = week + 1
    return cf, week, tot


def format_text(i, xxx, now, page):
    import datetime
    import humanize

    past = False
    # logging.info (xxx,'xxxxx')
    # logging.info (xxx[i]["date"]+'/'+xxx[i]['time'])
    # logging.info(xxx[i], "FAILMAN")
    dobj = datetime.datetime.strptime(
        xxx[i]["date"] + "/" + xxx[i]["time"], "%m/%d/%Y/%H:%M"
    )
    try:
        dobj = datetime.datetime.strptime(
            xxx[i]["date"] + "/" + xxx[i]["time"], "%m/%d/%Y/%H:%M"
        )
    except:
        ("errrrror:", xxx[i])
    diff = now - dobj
    if now.date() > dobj.date():
        past = True
    diff2 = humanize.naturaltime(now - dobj)
    diff2 = str(diff2)
    diff = str(diff)
    if "irmed" not in xxx[i]["status"]:
        xxx[i]["status"] = "[color=ff0000ff]" + xxx[i]["status"] + "[/color]"
    if "irmed" in xxx[i]["status"]:
        xxx[i][10] = "[color=00ff00ff]" + xxx[i]["status"] + "[/color]"
    fdate = (
        (dobj.strftime("%A"))
        + ", "
        + (dobj.strftime("%m"))
        + "/"
        + (dobj.strftime("%d"))
        + " "
        + (dobj.strftime("%I"))
        + ":"
        + (dobj.strftime("%M"))
        + "[sup]"
        + (dobj.strftime("%p"))
        + "[/sup]"
    )
    if now.date() == dobj.date():
        # today='[color=#00007fff][b]TODAY[/b][/color]\n'
        today = "[size=0 sp][b][/b][/size]"
    else:
        today = ""
    rindex = (len(xxx) - 1) - i
    rindex = i
    texta = (
        today
        + ""
        + fdate
        + " \n"
        + xxx[i]["show"]
        + " "
        + "\n[b]"
        + xxx[i]["venue"]
        + "\n[/b][size=13 sp]"
        + xxx[i]["location"]
        + "\n"
        + xxx[i]["pos"]
        + " "
        + xxx[i]["type"]
        + " "
        + xxx[i]["status"]
        + "\n"
        + diff2
    )
    if past == True:
        texta = "[size=12 sp]" + fdate + "\n" + xxx[i]["show"] + "\n" + xxx[i]["venue"]
    if xxx[i]["canceled"] == True:
        texta = "[s][color=ff0000]" + texta
    if xxx[i]["is_new"] == True:
        texta = texta + " new!"
    texta = texta + "[size=1 sp]***"
    # str(rindex)

    if page == "index":
        return texta
    if page == "info":
        return today, fdate
