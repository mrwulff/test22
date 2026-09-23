from libs.paystub_parser import parse_paystub
from libs.lib_rhino_db import RhinoDatabase

PAYSTUB_FILE = (
    "/Users/kevinwulff/Library/Application Support/demo3/pp/09-15-2026.html"
)

DB_FILE = (
    "/Users/kevinwulff/Library/Application Support/demo3/rhino.db"
)

print("\n========== PAYSTUB IMPORT TEST ==========")
print(f"Paystub: {PAYSTUB_FILE}")

with open(PAYSTUB_FILE, "r", encoding="utf-8") as f:
    html = f.read()

paystub = parse_paystub(html)

print(
    f"Pay period: {paystub['pay_period_start']} -> "
    f"{paystub['pay_period_end']}"
)
print(f"Pay date: {paystub['pay_date']}")
print(f"Payroll lines: {len(paystub['items'])}")

db = RhinoDatabase(DB_FILE)
shows = db.get_all_shows()

print(f"Database shows: {len(shows)}")

result = db.import_paystub(
    paystub=paystub,
    shows=shows,
)

print("\n========== IMPORT RESULT ==========")
print(f"Paystub ID:       {result['paystub_id']}")
print(
    f"Paystub:          "
    f"{'NEW' if result['is_new_paystub'] else 'EXISTING'}"
)
print(f"Payroll lines:    {result['imported']}")
print(f"Exact matches:    {result['exact']}")
print(f"Possible matches: {result['possible']}")
print(f"Unmatched:        {result['unmatched']}")
print("===================================\n")

print("========== STORED PAYROLL ==========")

rows = db.db.execute("""
    SELECT
        job_number,
        position,
        show,
        time_in,
        time_out,
        reg_hours,
        ot_hours,
        weekly_ot_hours,
        dt_hours,
        meal_penalty_hours,
        rest_break_penalty_hours,
        pay,
        show_id
    FROM payroll_items
    WHERE paystub_id = ?
    ORDER BY time_in
""", (result["paystub_id"],)).fetchall()

for row in rows:
    match_text = (
        f"MATCHED show_id={row['show_id']}"
        if row["show_id"]
        else "NO RHINO MATCH"
    )

    print(
        f"{row['job_number']} | "
        f"{row['position']} | "
        f"{row['show']} | "
        f"{row['time_in']} -> {row['time_out']} | "
        f"REG {row['reg_hours']} | "
        f"OT {row['ot_hours']} | "
        f"WEEKLY OT {row['weekly_ot_hours']} | "
        f"DT {row['dt_hours']} | "
        f"MEAL {row['meal_penalty_hours']} | "
        f"REST {row['rest_break_penalty_hours']} | "
        f"${row['pay']} | "
        f"{match_text}"
    )

print(f"\nStored payroll lines: {len(rows)}")
print("===================================\n")
