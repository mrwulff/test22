from dataclasses import dataclass

from bs4 import BeautifulSoup


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
            # Rhino schedule rows have 15 columns
            #

            if len(cols) != 15:
                continue

            show = RhinoShow()

            show.date = cols[1].get_text(strip=True)
            show.time = cols[2].get_text(strip=True)
            show.job = cols[3].get_text(strip=True)
            show.show = cols[4].get_text(strip=True)

            show.venue = cols[5].get_text(" ", strip=True)

            link = cols[5].find("a")

            if link and link.get("href"):
                show.venue_pdf = link["href"]

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
            show.old = show_date < date.today()

            self.shows.append(show)