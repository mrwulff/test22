def updateuser(data, ad):
    import json

    # with open(ad+'/userdata.json.txt') as json_file:
    #    data = json.load(json_file)

    # logging.info (data)
    # logging.info (type(data))
    (data["username"]) = data["username"]
    (data["password"]) = data["password"]
    (data["city"]) = data["city"]
    (data["usecache"]) = data["usecache"]
    (data["pcolor"]) = data["pcolor"]
    (data["scolor"]) = data["scolor"]
    # (data["name"]) = data["name"]
    try:
        (data["theme"]) = data["theme"]
    except:
        """"""
    # logging.info (data['username'])
    # data=str(data)
    data = json.dumps(data, indent=4)

    # logging.info(data, ad, "gaga")
    x = open(ad + "/userdata.json.txt", "w")
    x.write(data)
    x.close()


def updateuser_extra(data, ad):
    import json

    # logging.info(data, "json exta data")

    data = json.dumps(data, indent=4)
    x = open(ad + "/userdata_extra.json.txt", "w")
    x.write(data)
    x.close()

    # logging.info(data, "update extra")
