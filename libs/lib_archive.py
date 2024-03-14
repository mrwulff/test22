import json
import logging


def delete_demo_files(cd, ad):
    # logging.info("loading archive",first,last)
    import glob
    import os
    from datetime import datetime

    all_shows = []
    z = glob.glob(ad + cd + "/*.json")
    # logging.info (z)
    dell = 0
    for i in range(len(z)):
        if "DEMOSHOW!" in z[i]:
            try:
                os.remove(z[i])
                dell = dell + 1
                # self.snackbarx("success")
            except:
                logging.info("failed to remove")
                logging.info(z[i], "files)")

    logging.info(dell)
    return dell


def load(cd, ad, last, first):
    # logging.info("loading archive",first,last)
    import glob
    import json
    from datetime import datetime

    all_shows = []
    z = glob.glob(ad + cd + "/*.json")
    # logging.info (z)
    for i in range(len(z)):
        flag = True
        with open(z[i]) as d:
            # logging.info (z[i],'try jzon')
            # logging.info(z[i], "TRY JSON")
            try:
                dictData = json.load(d)
            except:
                logging.warning("failed to load " + z[i])
                flag = False
            if flag == True:
                c = dictData["date"]
                # logging.info (c,'dateeee',type(last))
                try:
                    show_date = datetime.strptime(c, "%m/%d/%Y")
                except:
                    try:
                        show_date = datetime.strptime(c, "%Y-%m-%d")
                    except:
                        show_date = datetime.strptime("1999-01-01", "%Y-%m-%d")
                show_date = show_date.date()
                # logging.info (first,show_date,last)
                # logging.info (type(first),type(show_date),type(last))
                if type(last) == int or type(last) == str:
                    all_shows.append(dictData)
                else:
                    # logging.info (first,show_date,last,'FIRST AND LAST')
                    if first <= show_date:
                        # logging.info (first,show_date,last,'found one!')
                        if show_date <= last:
                            # logging.info (first,show_date,last,'found one!')
                            all_shows.append(dictData)

    # logging.info (all_shows)
    return all_shows


def load_archive(ad, first, last, term, strict):
    success = []
    tot_hours = 0
    tot_money = 0
    tot_gigs = 0
    with open(ad + "/full_pp.json") as json_file:
        data = json.load(json_file)
    z = data["shows"]
    # logging.info (len(z))
    term = term.upper()
    for z2 in range(len(z)):
        # logging.info ((z[z2]
        gigs = z[z2]["gigs"]
        # logging.info (len(gigs))

        for z3 in range(len(gigs)):
            if "'" + term + "'" in str(gigs[z3]) and strict == True:
                success.append(gigs[z3])
                tot_money = tot_money + gigs[z3]["Total"]
                tot_hours = tot_hours + gigs[z3]["tot_hours"]
                tot_gigs = tot_gigs + 1

                # logging.info (gigs[z3])
            if term in str(gigs[z3]) and strict == False:
                success.append(gigs[z3])
                tot_money = tot_money + gigs[z3]["Total"]
                tot_hours = tot_hours + gigs[z3]["tot_hours"]
                tot_gigs = tot_gigs + 1

                # logging.info (gigs[z3])
    q = success, tot_hours, tot_money, tot_gigs
    return q


if __name__ == "__main__":
    # x=load("future_shows","C:/Users/twat/AppData/Roaming/demo3/",0,0)
    x = load_archive("C:/Users/twat/AppData/Roaming/demo3/", "all", "all", "VGK", False)
    logging.info(x)
