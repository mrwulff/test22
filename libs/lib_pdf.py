from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.graphics.shapes import Drawing
import logging
import calendar

from reportlab.lib import pagesizes
from reportlab.pdfgen.canvas import Canvas
import calendar, time, datetime
from math import floor

NOW = datetime.datetime.now()
SIZE = pagesizes.landscape(pagesizes.letter)


class NoCanvasError(Exception):
    pass


def nonzero(row):
    return len([x for x in row if x != 0])


def createCalendar(
    name, a, month, year=NOW.year, canvas=None, filename=None, size=SIZE
):
    # logging.info(month, "month", year, "year")
    """
    Create a one-month pdf calendar, and return the canvas

    month: can be an integer (1=Jan, 12=Dec) or a month abbreviation (Jan, Feb,
            etc.
    year: year in which month falls. Defaults to current year.
    canvas: you may pass in a canvas to add a calendar page to the end.
    filename: String containing the file to write the calendar to
    size: size, in points of the canvas to write on
    """
    s = 5
    if type(month) == type(""):
        month = time.strptime(month, "%b")[1]
    if canvas is None and filename is not None:
        canvas = Canvas(filename, size)
    elif canvas is None and filename is None:
        raise NoCanvasError
    datee = datetime.datetime.strptime(str(month), "%m")
    logging.info(datee)
    monthname = time.strftime(
        "%B",
    )
    calendar.setfirstweekday(6)
    cal = calendar.monthcalendar(
        year,
        month,
    )
    # cal.firstweekday(-1)
    title = monthname + " " + str(year) + " Rhino Schedule for " + name
    width, height = size
    width2, height2 = size

    # draw the month title
    # title = monthname + " " + str(year)
    canvas.drawCentredString(width / 2, height - 27, title)

    height = height - 40

    # margins
    wmar, hmar = width / 50, height / 50

    # set up constants
    width, height = width - (2 * wmar), height - (2 * hmar)
    rows, cols = len(cal), 7
    lastweek = nonzero(cal[-1])
    firstweek = nonzero(cal[0])
    weeks = len(cal)
    rowheight = floor(height / rows)
    boxwidth = floor(width / 7)

    # draw the bottom line
    canvas.line(wmar, hmar, wmar + (boxwidth * lastweek), hmar)
    # now, for all complete rows, draw the bottom line
    for row in range(1, len(cal[1:-1]) + 1):
        y = hmar + (row * rowheight)
        canvas.line(wmar, y, wmar + (boxwidth * 7), y)
    # now draw the top line of the first full row
    y = hmar + ((rows - 1) * rowheight)
    canvas.line(wmar, y, wmar + (boxwidth * 7), y)
    # and, then the top line of the first row
    startx = wmar + (boxwidth * (7 - firstweek))
    endx = startx + (boxwidth * firstweek)
    y = y + rowheight
    canvas.line(startx, y, endx, y)

    # now draw the vert lines
    for col in range(8):
        # 1 = don't draw line to first or last; 0 = do draw
        last, first = 1, 1
        if col <= lastweek:
            last = 0
        if col >= 7 - firstweek:
            first = 0
        x = wmar + (col * boxwidth)
        starty = hmar + (last * rowheight)
        endy = hmar + (rows * rowheight) - (first * rowheight)
        canvas.line(x, starty, x, endy)

    # now fill in the day numbers and any data
    x = wmar + 6
    y = hmar + (rows * rowheight) - 15
    tot = 0
    for week in cal:
        for day in week:
            event = False
            if day:
                try:
                    zzz = (a[day], day, "asdf")
                    zzz
                    event = True
                except:
                    # logging.info("no event")

                    pass

                canvas.setFont("Helvetica", s * 2)
                canvas.drawString(x, y, str(day))
                if event:
                    b = (len(a[day]) / 3) - 2
                    tot = tot + (len(a[day]) / 3)

                    for i in range(2):
                        if a[day].get("out" + str(i)):
                            if a[day].get("out" + str(i)) == "0":
                                si = ""
                            else:
                                si = "- " + a[day].get("out" + str(i))
                            canvas.setFont("Helvetica", s)
                            canvas.drawString(x + 15, y - 10 - i * 40, str(si))

                        # logging.info(str(a[day]) + "aday")

                        try:
                            canvas.setFont("Helvetica", s)
                            canvas.drawString(
                                x, y - 10 - i * 40, str(a[day]["time" + str(i)])
                            )
                            canvas.drawString(
                                x, y - 20 - i * 40, str(a[day]["venue" + str(i)])
                            )
                            canvas.drawString(
                                x, y - 30 - i * 40, str(a[day]["show" + str(i)])
                            )
                        except:
                            # logging.info("fail")
                            pass
                    try:
                        logging.info(str(a[day]["time2"]))

                        if b > 1:
                            canvas.drawString(x, y - 90, str(b) + " MORE EVENTS")
                        if b == 1:
                            canvas.drawString(
                                x, y - 90, str.split(str(b), ".")[0] + " MORE EVENT"
                            )

                    except:
                        pass

            x = x + boxwidth
        y = y - rowheight
        x = wmar + 6
    canvas.setFont("Helvetica", s * 1.4)
    canvas.drawCentredString(
        width / 2,
        height2 - 40,
        str.split(str(tot), ".")[0]
        + " Events, Updated "
        + str(datetime.datetime.now().date())
        + " Created By Schedulara.app",
    )
    # canvas.drawCentredString(width / 2, height2 + 0, str.split(str(tot), ".")[0]+ ' Shifts2')
    # canvas.drawCentredString(width / 2, height2 -100, str.split(str(tot), ".")[0]+ ' Shifts3')
    # canvas.drawCentredString(width / 2, height2 - 199, str.split(str(tot), ".")[0]+ ' Shifts4')
    # finish this page
    canvas.showPage()

    return canvas


def alt(name, ad, a, m, y):
    # create a December, 2005 PDF
    s = 5
    # logging.info(m, "month", y, "year")
    c = createCalendar(
        name, a, m, y, filename=ad + "/" + str(m) + "-" + str(y) + ".pdf"
    )
    logging.debug(a, m, y, "amy")
    # now add January, 2006 to the end
    # createCalendar(1, 2006, canvas=c)
    c.save()
    return ad + "/" + str(m) + "-" + str(y) + ".pdf"


if __name__ == "__main__":
    ad = "C:/Users/twat/AppData/Roaming/demo3"
    a = {
        1: {"time": "8am", "venue": "TMA", "show": "WWE EVENT"},
        2: {"time": "8am", "venue": "TMA", "show": "WWE EVENT"},
    }
    # submit("kevin wulff bad", 0, 0)
    # dl_score("kevin wulff", 0, ad)
    # parse_score(
    #    "kevin wulff bad", 0, "C:/Users/kw/AppData/Roaming/demo3", [50, 127, 250, 1]
    # )
    # submit("kevin wulff", 300, 0, ad)
    # create(ad)\
    m = 2
    y = 2024
    alt(ad, a, m, y)
