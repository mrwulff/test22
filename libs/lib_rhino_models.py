from dataclasses import dataclass
from datetime import datetime, date
from bs4 import BeautifulSoup
import hashlib



@dataclass
class RhinoShow:

    date: str = ""
    time: str = ""
    job: str = ""
    show: str = ""

    venue: str = ""
    venue_pdf: str = ""

    location: str = ""
    client: str = ""
    type: str = ""
    position: str = ""

    details: str = ""
    status: str = ""
    notes: str = ""

    tk: str = ""
    plus: str = ""

    confirmable: bool = False
    confirm_id: str = ""

    cancelled: bool = False
    old: bool = False

    id: str = ""

    def generate_id(self):

        identity = "|".join([
            self.date,
            self.job,
            self.show

        ])

        self.id = hashlib.sha256(
            identity.encode("utf-8")
        ).hexdigest()

        return self.id
    


class RhinoParser:

    def __init__(self, html):

        if isinstance(html, bytes):
            html = html.decode("utf-8", errors="ignore")

        self.soup = BeautifulSoup(html, "html.parser")

        self.name = ""
        self.shows = []
        self.last_updated=None
        self.old_shows=[]
        self.confirmables=[]


    def parse(self):

        self._parse_name()
        self._parse_schedule()

        return self

    def _parse_name(self):

        emp = self.soup.find("span", id="lblEmpName")

        if not emp:
            return

        text = emp.get_text(strip=True)

        if ", " not in text:
            self.name = text
            return

        last, first = text.split(", ", 1)

        self.name = f"{first} {last}"

    def _parse_schedule(self):

        rows = self.soup.find_all("tr")

        for row in rows:

            cols = row.find_all("td")

            #
            # Ignore anything that isn't a schedule row
            #

            if len(cols) != 15:
                continue

            #
            # A real schedule row must have a valid date
            #

            date_text = cols[1].get_text(strip=True)

            if not date_text:
                continue

            try:
                show_date = datetime.strptime(
                    date_text,
                    "%m/%d/%Y"
                ).date()
            except ValueError:
                continue

            #
            # Create show
            #

            show = RhinoShow()

            show.date = date_text
            show.time = cols[2].get_text(strip=True)
            show.job = cols[3].get_text(strip=True)
            show.show = cols[4].get_text(strip=True)

            #
            # Venue
            #

            show.venue = cols[5].get_text(" ", strip=True)

            link = cols[5].find("a")

            if link and link.get("href"):
                show.venue_pdf = link["href"]

            #
            # Remaining fields
            #

            show.location = cols[6].get_text(strip=True)
            show.client = cols[7].get_text(strip=True)
            show.type = cols[8].get_text(strip=True)
            show.position = cols[9].get_text(strip=True)

            show.details = cols[10].get_text(" ", strip=True)
            show.status = cols[11].get_text(strip=True)
            show.notes = cols[12].get_text(" ", strip=True)

            show.tk = cols[13].get_text(strip=True)
            show.plus = cols[14].get_text(strip=True)

            #
            # Confirmation
            #

            cell_html = str(cols[0])

            if "dgR" in cell_html:

                show.confirmable = True

                try:
                    show.confirm_id = cell_html.split('"')[3]
                except (IndexError, AttributeError):
                    show.confirm_id = ""

            #
            # Cancellation
            #

            if "Red" in cell_html:
                show.cancelled = True

            if "Turned Down" in show.status:
                show.cancelled = True

            #
            # Is this show in the past?
            #

            show.old = show_date < date.today()

            #
            # Generate stable ID
            #

            show.generate_id()

            #
            # Separate current/future shows
            # from historical shows
            #

            if show.old:
                self.old_shows.append(show)
            else:
                self.shows.append(show)