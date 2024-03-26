# from kivy_garden.graph import Graph, BarPlot
# from datetime import datetime
import logging

def make_matplot():
    pass


# def show_maker(ins,outs,shows):
#    return [[0,ins],[1,outs],2,shows]


def make_stats_pp(self, clabel, dd, newmax, y):
    if clabel == "1":
        from kivymd.uix.card import MDCard

        self.root.current_screen.ids["graphs"].add_widget(MDCard(text="wow"))
        logging.info("wow")

    # import platform

    platformheight = 400

    from kivy.utils import platform

    # logging.info(platform, "KIVY PLATFORM")
    if platform == "android":
        logging.info("omg its android")

    if platform == "win":
        platformheight = 400

    # self.root.current = "stats"
    # self.root.set_current("stats")
    self.samples = y
    # logging.info(len(dd), "lendd")
    self.graph = Graph(
        y_ticks_major=newmax / 3,
        x_ticks_major=y / 3,
        xmin=0,
        xmax=self.samples,
        ymin=0,
        ymax=newmax,
        draw_border=True,
        height=platformheight,
        xlabel=clabel,
        x_grid_label=True,
        y_grid_label=True,
    )
    self.root.current_screen.ids["graphs"].add_widget(self.graph)

    self.plot = BarPlot(color=self.theme_cls.primary_color, bar_spacing=0.5)
    self.graph.add_plot(self.plot)
    self.plot.bind_to_graph(self.graph)
    update_plot(self, dd)


def update_plot(self, dd):
    self.plot.points = [(dd[x][0], dd[x][1]) for x in range(len(dd))]
    pp_date = datetime.strptime(file2, "%m-%d-%Y.html")


def make_full_json_pp(ad, s, e, full):
    ###
    ### NEW ONE
    ###
    from datetime import datetime

    all_pp = []
    logging.info(s, e, "START AND END")
    try:
        import libs.lib_parse2 as lib_parse
    except:
        import lib_parse2 as lib_parse
    import os, glob, json

    try:
        os.chdir(ad + "/pp")
    except:
        os.mkdir(ad + "/pp")
        os.chdir(ad + "/pp")

    for file in glob.glob("*.html"):
        # logging.info(file)
        # f1, f2 = str.split(file, ".")
        f1 = datetime.strptime(file, "%m-%d-%Y.html")
        if full == False:
            if s < f1 and f1 < e:
                # logging.info(type(s), type(f1), e, "DATES OF PPPPS")

                pp = lib_parse.parsepayperiod(ad + "/pp/" + file)
                all_pp.append(pp)

        if full == True:
            pp = lib_parse.parsepayperiod(ad + "/pp/" + file)
            all_pp.append(pp)
    full_pp = {"shows": all_pp}

    ddj = json.dumps(full_pp, indent=4, default=str)
    if full == False:
        mm = open(ad + "/json_pps.json", "w")
    if full == True:
        mm = open(ad + "/full_pp.json", "w")
    mm.write(ddj)


def parsepp(self, ad, type, finish, start):
    import os, glob
    import libs.lib_parse as lib_parse
    from datetime import datetime

    try:
        os.chdir(ad + "/pp")
    except:
        os.mkdir(ad + "/pp")
        os.chdir(ad + "/pp")
    x = 0
    listofdicks = []
    dd = []
    dd2 = []
    realdays = []
    realdays_max = 0
    month_max = 0
    days_ago_max = 0
    months_ago_max = 30
    ins = 0
    outs = 0
    shows = 0
    all_pos = []
    days_ach_list = []
    all_hours = []
    max_t = 0
    for file in glob.glob("*.html"):
        # logging.info(file)
        # file2, junk = str.split(file, ".")
        file2 = file
        pp_date = datetime.strptime(file2, "%m-%d-%Y.html")

        # logging.info(pp_date)
        try:
            qq = (start.date(), finish.date(), pp_date.date(), "STARTSSS")
        except:
            pass
        try:
            start = start.date()
        except:
            pass
            # logging.info("cannont convert start")

        try:
            finish = finish.date()
        except:
            # logging.info("cannont convert finish")
            pass

        try:
            pp_date = pp_date.date()
        except:
            # logging.info("cannont convert pp_date")
            pass

        # logging.info(type(pp_date))
        # xx = type(start)
        # logging.info(xx)
        """
        try:
            if start.date() < pp_date and pp_date < finish.date():
                flag = True
                start = start.date()
                finish = finish.date()
        except:
            pass
        """

        if start < pp_date and pp_date < finish:
            dd, days, ins2, outs2, shows2, positions = lib_parse.parsepayperiod(
                ad + "/pp/" + file
            )
            # logging.info(dd["day_ach"], "DAYS MOTHERFUCKER")
            # logging.info((dd["day_ach"]), "DAYS MOTHERFUCKER")
            days_ach_list = days_ach_list + dd["day_ach"]
            ins = ins + ins2
            outs = outs + outs2
            shows = shows + shows2
            listofdicks.append(dd)
            x = x + 1
            if (dd["moneytotal"]) > month_max:
                month_max = dd["moneytotal"]
            z = [dd["ddelta"], dd["moneytotal"]]
            dd2.append(z)
            all_hours = all_hours + dd["hours_ach"]

            for z in range(len(days)):
                if days[z][1] > realdays_max:
                    realdays_max = days[z][1]
                if days[z][0] > days_ago_max:
                    days_ago_max = days[z][0]
                realdays.append(days[z])

        max_t = ins
        if outs > ins:
            max_t = outs
        if shows > max_t:
            max_t = shows

        #    return dd2,5000
        try:
            for x in range(len(positions)):
                all_pos.append(positions[x])
        except:
            logging.info("no poss")
    #logging.info(len(days_ach_list), "DAYSACHLIST")
    if type != "hats":
        return (
            dd2,
            realdays,
            realdays_max,
            month_max,
            days_ago_max,
            months_ago_max,
            ins,
            outs,
            shows,
            max_t,
        )
    if type == "hats":
        # logging.info(all_pos)
        hats = list(set(all_pos))
        # logging.info(hats, len(hats))
        return hats, all_pos, days_ach_list, all_hours


if __name__ == "__main__":
    # from kivy.app import App

    ad = "C:/Users/kw/AppData/Roaming/demo3/"
    make_full_json_pp(ad, full)
