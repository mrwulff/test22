# from turtle import xcor


def makeuserdata_extra(App, config_file, ios):
    import json
    from kivy.app import App

    app = App.get_running_app()
    ad = app.user_data_dir
    if ios == True:
        ad = config_file
        app = App.get_running_app()
        ad = app.user_data_dir

    x = ' { "update":0,"confirm":0,"streak":0,"lstreak":0}'
    y = json.loads(x)
    with open(ad + "/userdata_extra.json.txt", "w") as outfile:
        json.dump(y, outfile)
    # logging.info("writedata")


def makeuserdata(App, config_file, ios):
    import json
    from kivy.app import App

    app = App.get_running_app()
    ad = app.user_data_dir
    if ios == True:
        ad = config_file
        app = App.get_running_app()
        ad = app.user_data_dir

    x = ' { "username":"test@gmail.com", "password":"", "city":"lasvegas","usecache":"True","pcolor":"Red"  , "scolor":"White","debug":"True" ,     "theme" : "Dark", "not1" : "True", "not2": "True", "not1time": "60.0", "not2time": "120.0", "sound_effects": "Bang", "refreshreload": "False","not": "False","name": "anon","login": "False","hide_canceled": false,"today_start": true,"twenty":false,"bio": false,"nick": true,"phone":false,"button4":false,"hidden":false}'
    y = json.loads(x)
    with open(ad + "/userdata.json.txt", "w") as outfile:
        json.dump(y, outfile)
    # logging.info("writedata")


def format_textt(name):
    name = str.replace(name, "/", "")
    name = str.replace(name, ":", "")
    return name


def makeshowfile(App, x, config_file, ios):
    import json
    import os

    # app = App.get_running_app()
    app = App.get_running_app()
    ad = app.user_data_dir
    if ios == True:
        ad = config_file
        app = App.get_running_app()
        ad = app.user_data_dir
    # logging.info(x, "whathwat")
    try:
        fdate = format_textt(x[0])
        ftime = format_textt(x[1])
        fshow = format_textt(x[3])
    except:
        fdate = format_textt(x["date"])
        ftime = format_textt(x["time"])
        fshow = format_textt(x["show"])
    try:
        newhours = App.get_running_app().root.current_screen.ids["newhours"].text
    except:
        # logging.info("newhours not found")
        newhours = "0"
    try:
        lunch = App.get_running_app().root.current_screen.ids["lunches"].text
    except:
        logging.info("failed to find lunches")
        lunch = "0"
    try:
        fname = fdate + " " + ftime + " " + x["2"] + " " + fshow
    except:
        fname = fdate + " " + ftime + " " + x["job"] + " " + fshow
    try:
        x = (
            ' { "date":"'
            + x[0]
            + '", "time":"'
            + x[1]
            + '", "job":"'
            + x[2]
            + '","show":"'
            + x[3]
            + '","venue":"'
            + x[4]
            + '","location":"'
            + x[5]
            + '","client":"'
            + x[6]
            + '","type":"'
            + x[7]
            + '","pos":"'
            + x[8]
            + '","endtime":"'
            + newhours
            + '","lunches":"'
            + lunch
            + '"}'
        )
    except:
        x = (
            ' { "date":"'
            + x["date"]
            + '", "time":"'
            + x["time"]
            + '", "job":"'
            + x["job"]
            + '","show":"'
            + x["show"]
            + '","venue":"'
            + x["venue"]
            + '","location":"'
            + x["location"]
            + '","client":"'
            + x["client"]
            + '","type":"'
            + x["type"]
            + '","pos":"'
            + x["pos"]
            + '","endtime":"'
            + newhours
            + '","lunches":"'
            + lunch
            + '"}'
        )
    # logging.info (x,'jsonfile')
    y = json.loads(x, strict=False)
    try:
        with open(ad + "/shows/" + fname + ".json", "w") as outfile:
            json.dump(y, outfile)
    except:
        os.mkdir(ad + "/shows")
        with open(ad + "/shows/" + fname + ".json", "w") as outfile:
            json.dump(y, outfile)


def makeratefile(ad, rate, pos):
    try:
        rate = float(rate)
    except:
        rate = 0
    import json

    try:
        # with open(ad + "/rates.json", "r") as json_file:
        with open(ad + "/position_list.json", "r") as json_file:
            data2 = json.load(json_file)
        # json_file.close()
    except:
        data2 = {}
    # logging.info(data2, "POSITIONS!!!")
    dictionary = data2["positions"]
    #    dictionary = json.loads(dictionary)
    for z in range(len(dictionary)):
        logging.info((dictionary[z]["abv"]), pos, "wow")
        if (dictionary[z]["abv"]) == pos:
            logging.info("omg")
            dictionary[z]["rate"] = rate

    # logging.info(dictionary, "rateposad", type(dictionary))
    import json
    import os

    new_rate = {pos: rate}
    # dictionary.update(new_rate)

    logging.info(ad, "AFUCKINGD")

    with open(ad + "/position_list.json", "w") as outfile:
        json.dump(data2, outfile)
    outfile.close()


def makeposfile(App, x, config_file, ios, rate):
    import json
    import os

    # app = App.get_running_app()
    app = App.get_running_app()
    ad = app.user_data_dir
    if ios == True:
        ad = config_file
        app = App.get_running_app()
        ad = app.user_data_dir

    data = ' { "rate":"' + rate + '"}'
    y = json.loads(data)
    try:
        with open(ad + "/pos/" + x + ".json", "w") as outfile:
            json.dump(y, outfile)
        logging.info("wrote pos file")
    except:
        os.mkdir(ad + "/pos")
        with open(ad + "/pos/" + x + ".json", "w") as outfile:
            json.dump(y, outfile)
        logging.info("updated pos file")


if __name__ == "__main__":
    # get_positions("C://Users//twat//schedulara", "")
    makeratefile("C://Users//twat//AppData//Roaming//demo3", 30, "ME")
