import logging


def get_single_rate(ad, pos):
    import json

    f = "position_list.json"
    # logging.info
    # logging.info(ad, "get positions")
    o = open(ad + "/" + f)
    data = json.load(o)
    d = data["positions"]
    for x in range(len(d)):
        # logging.info(d[x], "dsubx")
        if d[x]["abv"] == pos:
            try:
                zz = d[x]["rate"]
            except:
                zz = 0
    return zz


def get_position_name(ad, name):
    import os
    import shutil
    import json

    f = "position_list.json"
    # logging.info
    # logging.info(ad, "get positions")
    try:
        o = open(ad + "/" + f)
        # logging.info("opened json file")
    except:
        pass
        logging.info("cant find position list", os.getcwd())
        shutil.copyfile(f, ad + "/" + f)
        o = open(ad + "/" + f)
        # logging.info("opened json file")
    data = json.load(o)
    data = data["positions"]
    # logging.info(data, "data")
    # x3 = search(data, name)
    # logging.info(x3)
    for x in range(len(data)):
        if name == (data[x]["abv"]):
            return data[x]["description"]


def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k


def get_positions(ad, search):
    import os
    import shutil
    import json

    f = "position_list.json"
    # logging.info
    # logging.info(ad, "get positions")
    try:
        o = open(ad + "/" + f)
        # logging.info("opened json file")
    except:
        pass
        logging.info("cant find position list", os.getcwd())
        shutil.copyfile(f, ad + "/" + f)
        o = open(ad + "/" + f)
        # logging.info("opened json file")
    data = json.load(o)
    # logging.info(
    #    data["positions"], len(data["positions"]), type(data["positions"]), "DATATATA"
    # )
    # xx = filter(lambda person: person["abv"] == "V", data)

    xx = [element for element in data["positions"] if search.lower() in element["all"]]
    # logging.info(len(xx), search, "xx", len(data["positions"]))
    return xx


def edit(ad):
    import json

    f = "position_list.json"
    f2 = "poslist.json"
    # logging.info
    # logging.info(ad, "get positions")

    o = open(ad + "/" + f)
    data = json.load(o)["positions"]
    for i in range(len(data)):
        logging.info(data[i])
        data[i]["all"] = data[i]["abv"] + " " + data[i]["description"]
        data[i]["all"] = data[i]["all"].lower()
    logging.info(data)
    with open(f2, "w") as ofile:
        json.dump(data, ofile, indent=4)


if __name__ == "__main__":
    # get_positions("C://Users//twat//schedulara", "")
    # edit("C://Users//twat//schedulara")
    r = "C:/Users/twat/AppData/Roaming/demo3/"
    # get_single_rate(r, "ME")
    get_position_name(r, "ME")
