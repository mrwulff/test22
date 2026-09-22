from datetime import datetime
from bs4 import BeautifulSoup
import re


def money(value):
    if not value:
        return 0.0

    value = str(value)
    value = value.replace("$", "")
    value = value.replace(",", "")
    value = value.strip()

    try:
        return float(value)
    except ValueError:
        return 0.0


def number(value):
    if not value:
        return 0.0

    value = str(value)
    value = value.replace(",", "")
    value = value.strip()

    try:
        return float(value)
    except ValueError:
        return 0.0


def parse_date(value):
    if not value:
        return None

    value = value.strip()

    for fmt in (
        "%m/%d/%Y",
        "%m/%d/%y",
    ):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass

    return None


def normalize_header(value):
    """
    Turn things like:

        "Time In"
        "TIME IN"
        "Time&nbsp;In"

    into a predictable key.
    """

    value = value.replace("\xa0", " ")
    value = value.strip().lower()

    value = re.sub(r"\s+", " ", value)

    return value

def find_paystub_table(soup):
    """
    Find the payroll table.

    Rhino currently uses:
        id="dgResults"

    The header cells are <td>, not <th>.
    """

    table = soup.find(
        "table",
        id="dgResults",
    )

    if table is not None:
        return table

    # Fallback for future format changes
    for table in soup.find_all("table"):

        first_row = table.find("tr")

        if first_row is None:
            continue

        cells = first_row.find_all(
            ["th", "td"]
        )

        headers = [
            normalize_header(
                cell.get_text(" ", strip=True)
            )
            for cell in cells
        ]

        required = {
            "job #",
            "class",
            "pos",
            "show",
            "time in",
            "time out",
        }

        if required.issubset(set(headers)):
            return table

    return None


def build_header_map(table):
    """
    Build a map from column name to column index.

    Supports both <th> and <td> header cells.
    """

    first_row = table.find("tr")

    if first_row is None:
        return {}

    headers = first_row.find_all(
        ["th", "td"]
    )

    result = {}

    for index, header in enumerate(headers):

        name = normalize_header(
            header.get_text(" ", strip=True)
        )

        result[name] = index

    return result


def cell_value(cells, header_map, name):

    index = header_map.get(name)

    if index is None:
        return ""

    if index >= len(cells):
        return ""

    return cells[index].get_text(
        " ",
        strip=True,
    )


def parse_paystub(html):

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    result = {
        "pay_period_start": None,
        "pay_period_end": None,
        "pay_date": None,

        "employee_name": None,
        "employee_number": None,

        "reg_hours": 0.0,
        "reg_pay": 0.0,

        "ot_hours": 0.0,
        "ot_pay": 0.0,

        "dt_hours": 0.0,
        "dt_pay": 0.0,

        "weekly_ot_hours": 0.0,
        "weekly_ot_pay": 0.0,

        "meal_penalty_hours": 0.0,
        "meal_penalty_pay": 0.0,

        "rest_break_penalty_hours": 0.0,
        "rest_break_penalty_pay": 0.0,

        "flat_fee_pay": 0.0,
        "grand_total": 0.0,

        "items": [],
    }

    # --------------------------------------------------
    # Pay period
    # --------------------------------------------------

    element = soup.find(id="lblPayPeriod")

    if element:

        text = element.get_text(
            " ",
            strip=True,
        )

        match = re.search(
            r"For Period\s+"
            r"(\d+/\d+/\d+)\s+"
            r"through\s+"
            r"(\d+/\d+/\d+)",
            text,
            re.I,
        )

        if match:

            result["pay_period_start"] = parse_date(
                match.group(1)
            )

            result["pay_period_end"] = parse_date(
                match.group(2)
            )

    # --------------------------------------------------
    # Pay date
    # --------------------------------------------------

    element = soup.find(id="lblPayDate")

    if element:

        text = element.get_text(
            " ",
            strip=True,
        )

        match = re.search(
            r"Date of Pay\s+(\d+/\d+/\d+)",
            text,
            re.I,
        )

        if match:

            result["pay_date"] = parse_date(
                match.group(1)
            )

    # --------------------------------------------------
    # Employee
    # --------------------------------------------------

    element = soup.find(id="lblEmpName")

    if element:
        result["employee_name"] = element.get_text(
            " ",
            strip=True,
        )

    element = soup.find(id="lblEmpNum")

    if element:
        result["employee_number"] = element.get_text(
            " ",
            strip=True,
        )

    # --------------------------------------------------
    # Job table
    # --------------------------------------------------

    table = find_paystub_table(soup)

    if table is None:

        print(
            "[PAYSTUB] ERROR: "
            "Could not find payroll table"
        )

        return result

    header_map = build_header_map(table)

    print(
        "[PAYSTUB] Found payroll table"
    )

    print(
        "[PAYSTUB] Columns:"
    )

    for name, index in header_map.items():

        print(
            f"    {index}: {name}"
        )

    # --------------------------------------------------
    # Rows
    # --------------------------------------------------

    rows = table.find_all("tr")

    for row in rows:

        cells = row.find_all("td")

        if not cells:
            continue

        job_number = cell_value(
            cells,
            header_map,
            "job #",
        )

        if not job_number:
            continue
        if normalize_header(job_number) == "job #":
            continue

        item = {
            "job_number": job_number,

            "class": cell_value(
                cells,
                header_map,
                "class",
            ),

            "position": cell_value(
                cells,
                header_map,
                "pos",
            ),

            "client": cell_value(
                cells,
                header_map,
                "client",
            ),

            "show": cell_value(
                cells,
                header_map,
                "show",
            ),

            "time_in": cell_value(
                cells,
                header_map,
                "time in",
            ),

            "time_out": cell_value(
                cells,
                header_map,
                "time out",
            ),

            "reg_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "reg hrs",
                )
            ),

            "ot_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "ot hrs",
                )
            ),

            "dt_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "dt hrs",
                )
            ),

            "weekly_ot_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "weekly ot hours",
                )
            ),

            "meal_penalty_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "meal penalty",
                )
            ),

            "rest_break_penalty_hours": number(
                cell_value(
                    cells,
                    header_map,
                    "rest break penalty",
                )
            ),

            "base_rate": number(
                cell_value(
                    cells,
                    header_map,
                    "base rate",
                )
            ),

            "blended_rate": number(
                cell_value(
                    cells,
                    header_map,
                    "blended rate",
                )
            ),

            "total": money(
                cell_value(
                    cells,
                    header_map,
                    "total",
                )
            ),
        }

        result["items"].append(item)

    # --------------------------------------------------
    # Period totals
    # --------------------------------------------------

    total_fields = {

        "lblRegHoursTotal":
            "reg_hours",

        "lblRegPayTotal":
            "reg_pay",

        "lblOTHoursTotal":
            "ot_hours",

        "lblOTPayTotal":
            "ot_pay",

        "lblDTHoursTotal":
            "dt_hours",

        "lblDTPayTotal":
            "dt_pay",

        "lblWeeklyOTHoursTotal":
            "weekly_ot_hours",

        "lblWeeklyOTPayTotal":
            "weekly_ot_pay",

        "lblMealPenaltyHoursTotal":
            "meal_penalty_hours",

        "lblMealPenaltyPayTotal":
            "meal_penalty_pay",

        "lblOTCHoursTotal":
            "rest_break_penalty_hours",

        "lblOTCPayTotal":
            "rest_break_penalty_pay",

        "lblFlatFeeTotal":
            "flat_fee_pay",

        "lblGrandTotal":
            "grand_total",
    }

    for element_id, result_key in total_fields.items():

        element = soup.find(id=element_id)

        if element is None:
            continue

        value = element.get_text(
            " ",
            strip=True,
        )

        if (
            "pay" in result_key
            or result_key in (
                "flat_fee_pay",
                "grand_total",
            )
        ):
            result[result_key] = money(value)

        else:
            result[result_key] = number(value)

    return result