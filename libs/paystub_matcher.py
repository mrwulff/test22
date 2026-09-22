from datetime import datetime


def parse_paystub_date(value):
    """
    Extract the date from a paystub Time In value.

    Example:
        9/1/2026 12:00:00 PM

    Returns:
        09/01/2026
    """

    if not value:
        return None

    value = value.strip()

    try:
        dt = datetime.strptime(
            value,
            "%m/%d/%Y %I:%M:%S %p",
        )

        return dt.strftime("%m/%d/%Y")

    except ValueError:
        return None


def normalize(value):
    if value is None:
        return ""

    return str(value).strip().upper()


def match_paystub_to_shows(paystub, shows):

    results = []

    for item in paystub.get("items", []):

        paystub_date = parse_paystub_date(
            item.get("time_in")
        )

        paystub_job = normalize(
            item.get("job_number")
        )

        paystub_position = normalize(
            item.get("position")
        )

        paystub_show = normalize(
            item.get("show")
        )

        exact = []
        possible = []

        for show in shows:

            db_date = normalize(
                show.get("date")
            )

            db_job = normalize(
                show.get("job")
            )

            db_position = normalize(
                show.get("position")
            )

            db_show = normalize(
                show.get("show")
            )

            # ------------------------------------------
            # Exact match
            #
            # Job + date + position
            # ------------------------------------------

            if (
                paystub_job == db_job
                and paystub_date == db_date
                and paystub_position == db_position
            ):
                exact.append(show)
                continue

            # ------------------------------------------
            # Possible match
            #
            # Date + job
            # ------------------------------------------

            if (
                paystub_job == db_job
                and paystub_date == db_date
            ):
                possible.append(show)
                continue

            # ------------------------------------------
            # Possible match
            #
            # Date + show + position
            # ------------------------------------------

            if (
                paystub_date == db_date
                and paystub_show == db_show
                and paystub_position == db_position
            ):
                possible.append(show)

        if exact:

            status = "EXACT"
            matches = exact

        elif possible:

            status = "POSSIBLE"
            matches = possible

        else:

            status = "NO MATCH"
            matches = []

        results.append({
            "status": status,
            "paystub": item,
            "matches": matches,
        })

    return results