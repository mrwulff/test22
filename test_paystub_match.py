import sys

from libs.paystub_parser import parse_paystub
from libs.paystub_matcher import match_paystub_to_shows
#from kivy.app import App
from libs.lib_rhino_db import RhinoDatabase


# --------------------------------------------------
# Paystub file
# --------------------------------------------------

PAYSTUB_FILE = (
    "/Users/kevinwulff/Library/Application Support/demo3/pp/09-15-2026.html"

)


# --------------------------------------------------
# Parse paystub
# --------------------------------------------------

with open(
    PAYSTUB_FILE,
    "r",
    encoding="utf-8",
) as f:

    html = f.read()


paystub = parse_paystub(html)


db = RhinoDatabase(
    "/Users/kevinwulff/Library/Application Support/demo3/rhino.db"
)
paystub_record = db.get_or_create_paystub(paystub)

paystub_id = paystub_record["paystub_key"]

print(
    f"\n[PAYSTUB] "
    f"{paystub_record['paystub_key']} | "
    f"{'NEW' if paystub_record['is_new'] else 'EXISTING'}"
)

# --------------------------------------------------
# Load existing shows
# --------------------------------------------------
#app = App.get_running_app()






shows = db.get_all_shows()
print("\n========== DATABASE SAMPLE ==========")

for show in shows:
    if str(show.get("job")) in ("34389", "34503", "34415", "34395", "34444", "34593"):
        print(
            f"DB | job={show.get('job')!r} "
            f"date={show.get('date')!r} "
            f"position={show.get('position')!r} "
            f"show={show.get('show')!r}"
        )

print("=====================================\n")

print()
print("========== PAYSTUB MATCH TEST ==========")

print(
    "Pay period:",
    paystub["pay_period_start"],
    "->",
    paystub["pay_period_end"],
)

print(
    "Pay date:",
    paystub["pay_date"],
)

print(
    "Paystub jobs:",
    len(paystub["items"]),
)

print(
    "Database shows:",
    len(shows),
)

print()


# --------------------------------------------------
# Match
# --------------------------------------------------

results = match_paystub_to_shows(
    paystub,
    shows,
)


# --------------------------------------------------
# Display
# --------------------------------------------------

exact_count = 0
possible_count = 0
no_match_count = 0


for result in results:

    item = result["paystub"]
    status = result["status"]
    matches = result["matches"]

    if status == "EXACT":
        exact_count += 1

    elif status == "POSSIBLE":
        possible_count += 1

    else:
        no_match_count += 1

    print(
        f"{status:10} | "
        f"{item['job_number']} | "
        f"{item['position']} | "
        f"{item['show']}"
    )

    print(
        f"           "
        f"{item['time_in']}"
    )

    for match in matches:

        print(
            f"           -> DB: "
            f"{match['date']} | "
            f"{match['job']} | "
            f"{match['position']} | "
            f"{match['show']}"
        )

    print()


print("---------------------------------------")

print(
    "EXACT:",
    exact_count,
)

print(
    "POSSIBLE:",
    possible_count,
)

print(
    "NO MATCH:",
    no_match_count,
)

print(
    "======================================="
)


print("\n========== PAYROLL IMPORT TEST ==========")

exact_count = 0
possible_count = 0
no_match_count = 0

for result in results:

    status = result["status"]

    if status == "EXACT":
        payroll_item = result["paystub"]
        show = result["matches"][0]

        db.update_show_payroll(
            show_id=show["id"],
            payroll_item=payroll_item,
            paystub_id=paystub_id,
        )
        db.delete_unmatched_payroll(
            paystub_id=paystub_id,
            payroll_item=payroll_item,
        )




        exact_count += 1

        print(
            f"IMPORTED | "
            f"{payroll_item['job_number']} | "
            f"{payroll_item['position']} | "
            f"{payroll_item['show']}"
        )

    elif status == "POSSIBLE":
        possible_count += 1

        print(
            f"SKIPPED POSSIBLE | "
            f"{result['paystub']['job_number']} | "
            f"{result['paystub']['position']} | "
            f"{result['paystub']['show']}"
        )

    elif status == "NO MATCH":
        no_match_count += 1

        payroll_item = result["paystub"]

        db.save_unmatched_payroll(
            payroll_item=payroll_item,
            paystub_id=paystub_id,
        )

        print(
            f"SAVED UNMATCHED | "
            f"{payroll_item['job_number']} | "
            f"{payroll_item['position']} | "
            f"{payroll_item['show']}"
        )

print("----------------------------------------")
print(f"Imported exact: {exact_count}")
print(f"Skipped possible: {possible_count}")
print(f"Skipped no match: {no_match_count}")
print("========================================")



print("\n========== UNMATCHED PAYROLL ==========")

rows = db.db.execute("""
    SELECT
        job_number,
        position,
        show,
        time_in,
        time_out,
        reg_hours,
        ot_hours,
        pay
    FROM unmatched_payroll
    ORDER BY time_in
""").fetchall()

for row in rows:
    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"{row[2]} | "
        f"{row[3]} -> {row[4]} | "
        f"REG {row[5]} | OT {row[6]} | "
        f"${row[7]}"
    )

print(f"Unmatched records: {len(rows)}")
print("======================================")
