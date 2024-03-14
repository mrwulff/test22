def extract_show(App, f, config_file):
    import json, os
    from datetime import datetime, timedelta

    nf = os.path.join(config_file, "shows", f)
    with open(nf) as json_file:
        data = json.load(json_file)

        ndate = str.split(data["date"], "/")
        ndate = ndate[0] + "/" + ndate[1]
        start = datetime.strptime(data["time"], "%H:%M")
        good = True
        try:
            end = datetime.strptime(data["endtime"], "%H:%M:%S")
            worked_hours = end - start
            if end < start:
                end = end + timedelta(hours=24)
                worked_hours = end - start
        except:
            worked_hours = 0
            end = "?"
            good = False

        try:
            lunch = int(data["lunches"])
        except:
            lunch = "?"
            good = False

        try:
            worked_hours = worked_hours - timedelta(hours=lunch)
            logging.info("its not good")
        except:
            good = False
        worked_hours = str(worked_hours)
        ot = 0
        hours = 0
        earnings = 0
        overtime = 0
        regular_hours = 0
        if good == True:
            start = start.strftime(" %H:%M")
            end = end.strftime(" %H:%M:%S")
            worked_hours = datetime.strptime(worked_hours, "%H:%M:%S")
            # worked_hours = worked_hours.strftime(" %H:%M")
            # hour = worked_hours.strftime("%H")
            # min = float(worked_hours.strftime("%M"))
            # min=min/float(60)
            # worked_hours=float(hour)+min
            hour = float(datetime.strftime(worked_hours, "%H"))
            minute = float(datetime.strftime(worked_hours, "%M"))
            minute = minute / 60.0
            worked_hours = hour + minute
            try:
                rate = float(extract_pos(App, config_file, data["pos"]))
            except:
                rate = float(0)
            earnings = rate * worked_hours
            if worked_hours > 8:
                overtime = worked_hours - 8
                overtimer = rate * 1.5 * overtime
                regular_hoursr = 8 * rate
                regular_hours = 8
                earnings = regular_hoursr + overtimer
            if worked_hours < 4:
                earnings = 4 * rate

        if good == False:
            rate = 0.0
            earnings = 0

        # except:
        #    'pass'
        logging.info(good, "wasitgood?")
        start = str(start)
        end = str(end)
        if earnings > 0:
            show_data = (
                ndate
                + " "
                + data["show"]
                + "\n"
                + start
                + " to "
                + end
                + " with "
                + str(lunch)
                + " lunche(s)\n"
                + str(worked_hours)
                + "*"
                + str(rate)
                + " earned: "
                + str(earnings)
            )
        else:
            show_data = (
                ndate
                + " "
                + data["show"]
                + "\n"
                + start
                + " to "
                + end
                + " with "
                + str(lunch)
                + " lunche(s)\n"
            )

        return (
            show_data,
            (earnings),
            (overtime),
            (regular_hours),
            int(worked_hours),
            data["date"],
        )


def extract_pos(App, config_file, pos):
    import json, os

    nf = os.path.join(
        config_file,
        "pos",
        pos,
    )
    try:
        with open(nf + ".json") as json_file:
            data = json.load(json_file)

            show_data = data["rate"]

            return show_data
    except:
        return "0"
