from libs.paystub_parser import parse_paystub


with open(
    "/Users/kevinwulff/Library/Application Support/demo3/pp/08-18-2026.html",
    "r",
    encoding="utf-8",
) as f:

    html = f.read()


result = parse_paystub(html)


print()
print("========== PAYSTUB TEST ==========")

print(
    "Period:",
    result["pay_period_start"],
    "->",
    result["pay_period_end"],
)

print(
    "Pay date:",
    result["pay_date"],
)

print(
    "Employee:",
    result["employee_name"],
)

print(
    "Employee number:",
    result["employee_number"],
)

print(
    "Jobs found:",
    len(result["items"]),
)

print()

for item in result["items"]:

    print(
        item["job_number"],
        "|",
        item["position"],
        "|",
        item["show"],
    )

    print(
        "   ",
        item["time_in"],
        "->",
        item["time_out"],
    )

    print(
        "   ",
        "REG:",
        item["reg_hours"],
        "| OT:",
        item["ot_hours"],
        "| DT:",
        item["dt_hours"],
    )

    print(
        "   ",
        "BASE:",
        item["base_rate"],
        "| BLENDED:",
        item["blended_rate"],
        "| PAY:",
        item["total"],
    )

    print()

print(
    "Grand total:",
    result["grand_total"],
)

print(
    "=================================="
)