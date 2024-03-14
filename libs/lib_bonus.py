def create_notification(x, y, debug, ad):
    import logging
    import datetime
    import os

    now = datetime.datetime.now()
    from kivy.utils import platform

    new_text = datetime.datetime.now().strftime("%H:%M:%S")
    logging.info(new_text)

    # logging.info(platform, "KIVY PLATFORM")
    if platform == "linux":
        logging.info("omgitslinux")
    d1 = float(y["not1time"])
    d2 = float(y["not2time"])

    d1 = d1 * 60
    d2 = d2 * 60

    logging.info(d1, d2, "omgwtfitsday1", x, y)

    showdatetime = x["date"] + " " + x["time"]

    showdatetime = datetime.datetime.strptime(showdatetime, "%m/%d/%Y %H:%M")
    dif = showdatetime - now

    delay2 = dif.total_seconds()
    # logging.info (delay2,'delay2',d2)
    # logging.info (type(delay2),type(d2))
    delay2 = delay2 - d2
    # logging.info (delay2,'delay2-d2',d2)

    delay1 = dif.total_seconds()
    # logging.info (delay1,'delay1')

    delay1 = delay1 - d1
    logging.info(delay1, "delay1")
    if debug == True:
        delay1 = 30
    if 1 == 1:
        from plyer import notification

        title = "test"
        message = "test2"
        ticker = "test3"
        kwargs = {"title": title, "message": message, "ticker": ticker}
        notification.notify(**kwargs)
    if platform in ("android", "win"):
        import json
        from datetime import datetime
        import time

        task_time = delay1 * 1000
        logging.info(task_time, "tasktime")
        from jnius import autoclass

        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        TaskScheduler = autoclass("org.test.myapp.TaskScheduler")

        task_details = {"title": title, "message": message}
        python_activity = PythonActivity.mActivity

        task_scheduler = TaskScheduler(python_activity)
        task_scheduler.scheduleTask(task_time, json.dumps(task_details))

    if platform == "ios":
        # if platform != "win":
        if 1 == 2:
            logging.info("IOS BITCHES", x["show"], delay2, d2, now, showdatetime)

            import libs.notification as notification

            try:
                if y["not"] == True and y["not2"] == True:
                    # logging.info (x,'xxxxxx')
                    # logging.info (x['show'])
                    notification.schedule(
                        x["show"],
                        delay=delay2,
                        title=y["not2time"] + " Minutes From Now: " + x["time"],
                        subtitle=x["venue"],
                        attachments=["images/black-rhino.png"],
                        sound_name="images/beep.wav",
                    )
                    logging.info("added not 2 ", delay2)

                if y["not"] == True and y["not1"] == True:
                    notification.schedule(
                        x["show"],
                        delay=delay1,
                        title=y["not1time"] + " Minutes From Now:  " + x["time"],
                        subtitle=x["venue"],
                        attachments=["images/black-rhino.png"],
                        sound_name="images/beep.wav",
                    )
                    logging.info("added not 1 ", delay1)
            except:
                logging.info("failed to make nots")

            # import notification_old
            # x6=notification.get_scheduled()
            # logging.info (len(x6),'omggggg')
            # logging.info(type(datetime_object))
            # logging.info(datetime_object)

    logging.debug(x)


def cancel_notification():
    import platform
    import logging

    from kivy.utils import platform

    logging.info(platform, "KIVY PLATFORM")
    if platform == "ios":
        # import notification_old as notification

        logging.debug("IOS BITCHES")
        # notification.cancel_all()


x = {
    "date": "08/24/2022",
    "time": "07:00",
    "job": "26678",
    "show": "(TMA) MY CHEMICAL ROMANCE - PLACEHOLDER",
    "venue": "T- MOBILE ARENA",
    "location": "LOADING DOCK",
    "client": "MGM RESORTS",
    "type": "IN",
    "pos": "ME",
    "details": "\xa0",
    "status": "Confirmed",
    "notes": "HARD HAT, SAFETY VEST, GLOVES & PROTECTIVE TOE BOOTS; BRING PARKING STUB TO VALIDATE// FACE MASK REQ'D",
    "timekeep": "\xa0",
    "plus": "\xa0",
    "canceled": False,
    "confirmid": "",
    "lunches": "",
    "endtime": "",
    "is_new": False,
    "confirable": "False",
    "old": False,
}
y = {
    "username": "kevincwulff@gmail.com",
    "password": "b'YmxpbmsxODI='",
    "city": "lasvegas",
    "usecache": False,
    "pcolor": "DeepPurple",
    "scolor": "Amber",
    "debug": "True",
    "theme": "Light",
    "not1": False,
    "not2": False,
    "not1time": 0,
    "not2time": 0,
    "sound_effects": "Bang",
    "refreshreload": False,
    "not": False,
    "login": "False",
    "hide_canceled": True,
    "today_start": True,
    "twenty": False,
    "bio": False,
    "nick": True,
    "phone": False,
    "button4": False,
    "onboarding": True,
    "backup_checks": "False",
    "backup_config": "False",
    "backup_shows": "False",
    "usegoogle": "False",
    "last_backup": "2022-08-17 09:52:56.665309",
    "name": "Kevin Wulff",
    "drive_id": "1IOFfiU0V4qySMyU3cEK32ypGczXRWz-q",
    "cal_id": "n60m9dk1tv6eg17v6o71vbn4o4@group.calendar.google.com",
    "theme2": False,
}
ad = "C:/Users/kw/AppData/Roaming/demo3/"
if __name__ == "__main__":
    create_notification(x, y, True, ad)
