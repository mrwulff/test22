# libs/rhino_parser.py

from bs4 import BeautifulSoup
from datetime import datetime

from .lib_rhino_models import RhinoShow


class RhinoParser:

    def __init__(self, html):

        if isinstance(html, bytes):
            html = html.decode("utf-8", errors="ignore")

        self.soup = BeautifulSoup(html, "html.parser")

        self.name = ""
        self.shows = []

    def parse(self):

        self._parse_name()
        self._parse_schedule()

        return self
    def _parse_name(self):

        span = self.soup.find("span", id="lblEmpName")

        if not span:
            return

        last, first = span.text.split(", ")

        self.name = f"{first} {last}"
    def _parse_schedule(self):

        rows = self.soup.find_all("tr")

        for row in rows:

            cells = row.find_all("td")

            if len(cells) != 15:
                continue

            show = RhinoShow()

            show.date = cells[1].get_text(strip=True)
            show.time = cells[2].get_text(strip=True)
            show.job = cells[3].get_text(strip=True)
            show.show = cells[4].get_text(strip=True)
            show.venue = cells[5].get_text(" ", strip=True)
            show.location = cells[6].get_text(strip=True)
            show.client = cells[7].get_text(strip=True)
            show.type = cells[8].get_text(strip=True)
            show.position = cells[9].get_text(strip=True)
            show.details = cells[10].get_text(strip=True)
            show.status = cells[11].get_text(strip=True)
            show.notes = cells[12].get_text(strip=True)
            show.timekeeper = cells[13].get_text(strip=True)
            show.plus = cells[14].get_text(strip=True)
            

            #
            # venue pdf
            #

            link = cells[5].find("a")

            if link:
                show.venue_pdf = link.get("href")

            #
            # cancelled
            #

            show.cancelled = (
                "turned down" in show.status.lower()
                or "red" in str(cells[0]).lower()
            )

            #
            # confirm id
            #

            html = str(cells[0])

            if "dgR" in html:

                try:
                    show.confirm_id = html.split('"')[3]
                except:
                    pass

            self.shows.append(show)