def download_ach(ad):
    import urllib.request, urllib.error, urllib.parse, json

    flag = True
    hash = False
    try:
        # openedFile = open(ad + "/ids22.json")
        f = open(ad + "/ids22.json")
        data = json.load(f)
        logging.info(data)

        z = data["children"]

    except:
        logging.info("fail")
        z = ""

    try:
        url = "https://kevinwulff.com/wedding/ids22.json"

        response = urllib.request.urlopen(url)
        webContent = response.read().decode("UTF-8")
        f = open(ad + "/ids22.json", "w")
        f.write(webContent)
        f.close
        flag = True
        logging.info("downloaded score tables")
    except:
        logging.info("failed to dl")
        return "failed to dl"

    f = open(ad + "/ids22.json")
    data = json.load(f)
    logging.info(data)

    nz = data["children"]

    if z == nz:
        logging.info("sameold")
        return "No Update Avalable"

    if flag == True:
        return "Success. Downloaded new Tables"
    if flag == False:
        return "Falue[0]"


def list_ach(ad, select):
    import json

    try:
        f = open(ad + "/testtest22.json")
    except:
        make_ach(ad)
        f = open(ad + "/testtest22.json")
    data = json.load(f)
    newdata = []
    xnewdata = []
    # logging.info(data["children"][0])
    # logging.info(len(data["children"]))
    # logging.info(data["children"])
    z = data["children"]
    for i in range(len(z)):
        if (z[i]["achieved"]) == "True":
            newdata.append(z[i])
        if (z[i]["achieved"]) == "False":
            xnewdata.append(z[i])

    if select == "all":
        return data["children"]
    if select == "done":
        return newdata
    if select == "notdone":
        return xnewdata


def make_ach(ad):
    import json

    response_json = {}
    response_json["name"] = "ach"

    # where your children list will go
    children = []

    size = 500  # or whatever else you want

    # For each item in your original list

    # children.append({"name": "name", "size": size})
    # children.append({"name": "name", "size": size})

    ach_name = "Test"
    ach_disc = "This is just a test"
    achieved = "False"
    date_achieved = "0"
    ach_level = 0
    ach_color = "Black"
    ach_shows = dict()
    ach_extra = "none"
    ach_hidden = "False"
    ach_progress = 0
    ach_icon = "lock-alert"
    ach_graph_disc = []

    # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    hats = {
        "name": "Wear The Hat",
        "disc": "Work 10 different Positions",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 0,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": "Positions:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "account-cowboy-hat",
        "ach_graph_disc": ["Percent:", "Position:", "###:"],
    }

    grind = {
        "name": "Hustle and Grind",
        "disc": "Work 14 days in a Row",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 0,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": "Dates:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "calendar-sync",
        "ach_graph_disc": ["###:", "Date:"],
    }

    hourly = {
        "name": "Celery man!",
        "disc": "Work 18 Hours on a single call",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 0,
        "ach_color": "Who's green, gets no overtime pay and snaps easily?",
        "ach_shows": ach_shows,
        "ach_extra": "Most Hours:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "clock-time-four",
        "ach_graph_disc": ["Hours:", "Show", "Date:"],
    }
    scroll = {
        "name": "Scrollbar!",
        "disc": "Have over 30 gigs listed in schedule",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 0,
        "ach_color": "Who's green, gets no overtime pay and snaps easily?",
        "ach_shows": ach_shows,
        "ach_extra": "Most Gigs:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "clock-time-four",
        "ach_graph_disc": ["", "", ""],
    }
    ach = [hats, grind, hourly, scroll]

    for iii in range(len(ach)):
        children.append(ach[iii])

    for i in range(10):
        tot_ach = {
            "name": ach_name + " " + str(i),
            "disc": ach_disc,
            "achieved": achieved,
            "date_achieved": date_achieved,
            "ach_level": ach_level,
            "ach_color": ach_color,
            "ach_shows": ach_shows,
            "ach_extra": ach_extra,
            "ach_hidden": ach_hidden,
            "ach_progress": ach_progress,
            "ach_icon": ach_icon,
            "ach_graph_disc": ach_graph_disc,
        }

        children.append(tot_ach)

    response_json["children"] = children

    json_object = json.dumps(response_json, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


def longestrun(myList):
    size = 1
    max_size = 0
    listshows = []
    mshows = []
    date = ""
    for i in range(len(myList) - 1):
        # logging.info(myList[i][0], myList[i + 1][0], myList[i][1])

        if myList[i + 1][0] - 1 == myList[i][0] or myList[i + 1][0] == myList[i][0]:
            if myList[i + 1][0] - 1 == myList[i][0]:
                size += 1
            # logging.info("omg")
            listshows.append(myList[i])
        else:
            size = 1
            # logging.info("fail")
            listshows = []
        # logging.info(size)
        if max_size < size:
            # logging.info(size)
            date = myList[i]
            max_size = size
            mshows = listshows

    return max_size, date, mshows


def check_scroll(self, ad, x):
    import libs.lib_new
    import json
    import datetime

    dataxx = libs.lib_new.get_json_schedule(x, ad)
    logging.info(len(dataxx["shows"]), "asdfasdfasdf")

    f = open(ad + "/testtest22.json")
    data = json.load(f)

    if (len(dataxx["shows"])) > 30:
        logging.info("scroll ach unlocked!!!")
        if data["children"][3]["achieved"] == "False":
            data["children"][3]["date_achieved"] = str(datetime.date.today())
        data["children"][3]["achieved"] = "True"
        data["children"][3]["ach_level"] = 10
        data["children"][3]["ach_shows"] = str(len(dataxx["shows"]))
        data["children"][2]["ach_progress"] = str(len(dataxx["shows"]))
    json_object = json.dumps(data, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


def check_hats(self, ad):
    try:
        f = open(ad + "/testtest22.json")
    except:
        make_ach(ad)
        f = open(ad + "/testtest22.json")

    logging.info("checking hats")
    points = 0
    from datetime import datetime, timedelta
    import libs.lib_makegraphs as lib_makegraphs

    new_start = datetime.now()
    new_finish = datetime.now() - timedelta(days=10365)
    h, h2, days, hours = lib_makegraphs.parsepp(
        self,
        ad,
        "hats",
        new_start,
        new_finish,
    )
    # logging.info(h, h2, days, hours)
    return h, h2
    """
    hours.sort(key=lambda x: x[0], reverse=True)
    top_hours = []
    # logging.info(hours, "hourssss")
    if len(hours) > 5:
        for aaa in range(5):
            top_hours.append(hours[aaa])

    import json
    from collections import Counter

    # logging.info(Counter(h2))
    days.sort()
    import itertools

    if len(days) == 0:
        logging.info("no pay data.  Please download")
        return
    # logging.info(days)
    xx, date, shows = longestrun(days)
    # logging.info(xx, shows, "whtdcfuck")
    # for i in range(len(days)):
    #    logging.info(days[i][0])

    f = open(ad + "/testtest22.json")
    data = json.load(f)

    ###hats
    data["children"][0]["ach_shows"] = Counter(h2)
    data["children"][0]["ach_progress"] = len(h)

    if len(h) > 10:
        if data["children"][0]["achieved"] == "False":
            data["children"][0]["date_achieved"] = str(datetime.date.today())

        data["children"][0]["achieved"] = "True"
        data["children"][0]["ach_level"] = 10

    ###hustle
    if len(shows) >= 14:
        if data["children"][1]["achieved"] == "False":
            data["children"][1]["date_achieved"] = str(datetime.date.today())

        data["children"][1]["achieved"] = "True"
        data["children"][1]["ach_level"] = 10
    data["children"][1]["ach_shows"] = shows
    data["children"][1]["ach_progress"] = len(shows)

    ###hours_ach
    if hours[0][0] > 18:
        logging.info("ach unlocked!!!")
        if data["children"][2]["achieved"] == "False":
            data["children"][2]["date_achieved"] = str(datetime.date.today())
        data["children"][2]["achieved"] = "True"
        data["children"][2]["ach_level"] = 10
        data["children"][2]["ach_shows"] = top_hours
        data["children"][2]["ach_progress"] = hours[0][0]

    json_object = json.dumps(data, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)

    """


def make_scores(ad):
    import json

    response_json = {}
    response_json["name"] = "Scores"

    # where your children list will go
    children = []

    size = 500  # or whatever else you want

    # For each item in your original list

    # children.append({"name": "name", "size": size})
    # children.append({"name": "name", "size": size})

    score_name = "Test"
    score_disc = "This is just a test"

    # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    zero = {
        "name": "ach",
        "appid": "d6073280-f7af-4082-8b33-0356d7068f51",
        "secret": "073276b2-4940-40f0-87cc-7e4805382cd0",
    }

    one = {
        "name": "hats",
        "appid": "13efdf33-50c3-4a88-bd6f-a9342c18502d",
        "secret": "fd31ac45-089b-4d79-bb0e-a378d58fe9a4",
    }

    two = {
        "name": "grind",
        "appid": "7102b222-2f8f-4b5d-b654-6e86ce450bcc",
        "secret": "ddb635c1-b74c-4cf7-aadf-57cb7b986bb8",
    }

    three = {
        "name": "celery",
        "appid": "ddc1ae8c-d9ee-4854-ac61-597fffd9445f",
        "secret": "7fd16428-49e8-46af-a44f-6e2ef9e5d8bf",
    }

    ach = [zero, one, two, three]

    for iii in range(len(ach)):
        children.append(ach[iii])

    response_json["children"] = children

    json_object = json.dumps(response_json, indent=4)
    x = open(ad + "/ids22.json", "w")
    x.write(json_object)


if __name__ == "__main__":
    ad = "C:/Users/kw/AppData/Roaming/demo3/"
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # list_ach("C:/Users/kw/AppData/Roaming/demo3/", "done")
    # make_scores("C:/Users/kw/AppData/Roaming/demo3/")
    # check_hats("", "C:/Users/kw/AppData/Roaming/demo3/")
    # make_scores("C:/Users/kw/AppData/Roaming/demo3/")
    download_ach(ad)
# y(uv7K9PJ2B1
