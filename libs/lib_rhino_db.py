##lib_rhino_db.py

import os
import sqlite3
from datetime import datetime
from kivy.app import App


class RhinoDatabase:

    def __init__(self, db_path=None):
        if db_path is None:
            app = App.get_running_app()
            self.db_path = os.path.join(app.user_data_dir, "rhino.db")
        else:
            self.db_path = db_path

        print(f"[DB] Opening database: {self.db_path}")

        self.db = sqlite3.connect(self.db_path)
        self.db.row_factory = sqlite3.Row

        self._create_tables()





    def _create_tables(self):
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS paystubs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                paystub_key TEXT UNIQUE NOT NULL,

                pay_period_start TEXT,
                pay_period_end TEXT,
                pay_date TEXT,

                employee_name TEXT,
                employee_number TEXT,

                imported_at TEXT,
                updated_at TEXT
            )
        """)
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS unmatched_payroll (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                paystub_id TEXT,
                paystub_imported_at TEXT,

                job_number TEXT,
                class TEXT,
                position TEXT,
                client TEXT,
                show TEXT,

                time_in TEXT,
                time_out TEXT,

                reg_hours REAL,
                ot_hours REAL,
                dt_hours REAL,
                weekly_ot_hours REAL,

                meal_penalty_hours REAL,
                rest_break_penalty_hours REAL,

                base_rate REAL,
                blended_rate REAL,
                pay REAL,

                created_at TEXT
            )
        """)

        self.db.execute("""
            CREATE TABLE IF NOT EXISTS metadata (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        self.db.execute("""
            CREATE TABLE IF NOT EXISTS changes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT,

                show_id TEXT,
                change_type TEXT,

                field TEXT,
                old_value TEXT,
                new_value TEXT
            )
        """)

        self.db.execute("""
            CREATE TABLE IF NOT EXISTS shows (
                id TEXT PRIMARY KEY,
                date TEXT,
                time TEXT,
                job TEXT,
                show TEXT,
                venue TEXT,
                venue_pdf TEXT,
                location TEXT,
                client TEXT,
                type TEXT,
                position TEXT,
                details TEXT,
                status TEXT,
                notes TEXT,
                tk TEXT,
                plus TEXT,
                confirmable INTEGER,
                confirm_id TEXT,
                cancelled INTEGER,
                created_at TEXT,
                updated_at TEXT
            )
        """)

        self._migrate_shows_table()

        self.db.commit()


    def _migrate_shows_table(self):

        columns = {
            "paystub_id": "TEXT",
            "paystub_imported_at": "TEXT",

            "time_in": "TEXT",
            "time_out": "TEXT",

            "reg_hours": "REAL",
            "ot_hours": "REAL",
            "dt_hours": "REAL",
            "weekly_ot_hours": "REAL",

            "meal_penalty_hours": "REAL",
            "rest_break_penalty_hours": "REAL",

            "base_rate": "REAL",
            "blended_rate": "REAL",
            "pay": "REAL",

            "user_reported_hours": "REAL",
            "user_reported_meal_breaks": "INTEGER",
            "user_notes": "TEXT",
        }

        existing = {
            row["name"]
            for row in self.db.execute(
                "PRAGMA table_info(shows)"
            ).fetchall()
        }

        for column, column_type in columns.items():

            if column not in existing:

                print(
                    f"[DB] Adding column: "
                    f"shows.{column} ({column_type})"
                )

                self.db.execute(
                    f"ALTER TABLE shows ADD COLUMN "
                    f"{column} {column_type}"
                )

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def set(self, key, value):

        self.db.execute(
            """
            INSERT INTO metadata (key, value)
            VALUES (?, ?)
            ON CONFLICT(key)
            DO UPDATE SET value = excluded.value
            """,
            (key, str(value)),
        )

        self.db.commit()

    def get(self, key, default=None):

        row = self.db.execute(
            """
            SELECT value
            FROM metadata
            WHERE key = ?
            """,
            (key,),
        ).fetchone()

        if row is None:
            return default

        return row["value"]

    # --------------------------------------------------
    # User / App Settings
    # --------------------------------------------------

    def save_user_setting(self, key, value):

        self.db.execute("""
            INSERT INTO metadata (key, value)
            VALUES (?, ?)
            ON CONFLICT(key)
            DO UPDATE SET value = excluded.value
        """, (
            key,
            str(value) if value is not None else "",
        ))

        self.db.commit()


    def get_user_setting(self, key, default=None):

        row = self.db.execute("""
            SELECT value
            FROM metadata
            WHERE key = ?
        """, (key,)).fetchone()

        if row is None:
            return default

        return row["value"]


    def save_user_settings(self, settings):

        for key, value in settings.items():

            self.db.execute("""
                INSERT INTO metadata (key, value)
                VALUES (?, ?)
                ON CONFLICT(key)
                DO UPDATE SET value = excluded.value
            """, (
                key,
                str(value) if value is not None else "",
            ))

        self.db.commit()




    def delete_unmatched_payroll(
        self,
        paystub_id,
        payroll_item,
    ):
        """
        Remove an unmatched payroll item after it has
        subsequently been matched to a Rhino show.
        """

        self.db.execute("""
            DELETE FROM unmatched_payroll
            WHERE
                paystub_id = ?
                AND job_number = ?
                AND position = ?
                AND time_in = ?
                AND time_out = ?
        """, (
            paystub_id,
            payroll_item.get("job_number"),
            payroll_item.get("position"),
            payroll_item.get("time_in"),
            payroll_item.get("time_out"),
        ))

        self.db.commit()

    def get_user_settings(self):

        rows = self.db.execute("""
            SELECT key, value
            FROM metadata
        """).fetchall()

        return {
            row["key"]: row["value"]
            for row in rows
        }

    

    # --------------------------------------------------
    # Last updated
    # --------------------------------------------------

    def set_last_updated(self, timestamp=None):

        if timestamp is None:
            timestamp = datetime.now()

        self.set(
            "last_updated",
            timestamp.isoformat(),
        )

    def get_last_updated(self):

        value = self.get("last_updated")

        if value is None:
            return None

        try:
            return datetime.fromisoformat(value)
        except ValueError:
            return None

    # --------------------------------------------------
    # Close
    # --------------------------------------------------

    def close(self):

        self.db.close()

    def _show_values(self, show):

        return {
            "id": show.id,

            "date": show.date,
            "time": show.time,
            "job": show.job,
            "show": show.show,

            "venue": show.venue,
            "venue_pdf": show.venue_pdf,

            "location": show.location,
            "client": show.client,
            "type": show.type,
            "position": show.position,

            "details": show.details,
            "status": show.status,
            "notes": show.notes,

            "tk": show.tk,
            "plus": show.plus,

            "confirmable": int(show.confirmable),
            "confirm_id": show.confirm_id,

            "cancelled": int(show.cancelled),
        }

    def compare(self, shows):

        current = {
            show.id: show
            for show in shows
        }

        rows = self.db.execute(
            "SELECT * FROM shows"
        ).fetchall()

        previous = {
            row["id"]: row
            for row in rows
        }

        result = {
            "new": [],
            "modified": [],
            "unchanged": [],
            "removed": [],
        }

        #
        # NEW / MODIFIED / UNCHANGED
        #

        for show_id, show in current.items():

            if show_id not in previous:

                result["new"].append(show)

                continue

            old = previous[show_id]

            changes = self._compare_show(
                old,
                show,
            )

            if changes:

                result["modified"].append({
                    "show": show,
                    "changes": changes,
                })

            else:

                result["unchanged"].append(show)

        #
        # REMOVED
        #

        for show_id, old in previous.items():

            if show_id not in current:

                result["removed"].append(old)

        return result


    def _compare_show(self, old, new):

        fields = [
            "date",
            "time",
            "job",
            "show",
            "venue",
            "venue_pdf",
            "location",
            "client",
            "type",
            "position",
            "details",
            "status",
            "notes",
            "tk",
            "plus",
            "confirmable",
            "confirm_id",
            "cancelled",
        ]

        changes = {}

        for field in fields:

            old_value = old[field]

            new_value = getattr(new, field)

            if isinstance(new_value, bool):
                new_value = int(new_value)

            if str(old_value) != str(new_value):

                changes[field] = {
                    "old": old_value,
                    "new": new_value,
                }

        return changes

    def save_shows(self, shows):

        now = datetime.now().isoformat()

        for show in shows:

            values = self._show_values(show)

            self.db.execute("""
                INSERT INTO shows (
                    id,
                    date,
                    time,
                    job,
                    show,
                    venue,
                    venue_pdf,
                    location,
                    client,
                    type,
                    position,
                    details,
                    status,
                    notes,
                    tk,
                    plus,
                    confirmable,
                    confirm_id,
                    cancelled,
                    created_at,
                    updated_at
                )
                VALUES (
                    :id,
                    :date,
                    :time,
                    :job,
                    :show,
                    :venue,
                    :venue_pdf,
                    :location,
                    :client,
                    :type,
                    :position,
                    :details,
                    :status,
                    :notes,
                    :tk,
                    :plus,
                    :confirmable,
                    :confirm_id,
                    :cancelled,
                    :created_at,
                    :updated_at
                )

                ON CONFLICT(id) DO UPDATE SET

                    date = excluded.date,
                    time = excluded.time,
                    job = excluded.job,
                    show = excluded.show,
                    venue = excluded.venue,
                    venue_pdf = excluded.venue_pdf,
                    location = excluded.location,
                    client = excluded.client,
                    type = excluded.type,
                    position = excluded.position,
                    details = excluded.details,
                    status = excluded.status,
                    notes = excluded.notes,
                    tk = excluded.tk,
                    plus = excluded.plus,
                    confirmable = excluded.confirmable,
                    confirm_id = excluded.confirm_id,
                    cancelled = excluded.cancelled,
                    updated_at = excluded.updated_at
            """, {
                **values,
                "created_at": now,
                "updated_at": now,
            })

        self.db.commit()

    def save_changes(self, changes):

        now = datetime.now().isoformat()

        for show in changes["new"]:

            self.db.execute("""
                INSERT INTO changes (
                    timestamp,
                    show_id,
                    change_type,
                    field,
                    old_value,
                    new_value
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                now,
                show.id,
                "new",
                None,
                None,
                None,
            ))

        for item in changes["modified"]:

            show = item["show"]

            for field, change in item["changes"].items():

                self.db.execute("""
                    INSERT INTO changes (
                        timestamp,
                        show_id,
                        change_type,
                        field,
                        old_value,
                        new_value
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    now,
                    show.id,
                    "modified",
                    field,
                    str(change["old"]),
                    str(change["new"]),
                ))

        for old in changes["removed"]:

            self.db.execute("""
                INSERT INTO changes (
                    timestamp,
                    show_id,
                    change_type,
                    field,
                    old_value,
                    new_value
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                now,
                old["id"],
                "removed",
                None,
                None,
                None,
            ))

        self.db.commit()
    def reset_dev(self):

        self.db.execute("DELETE FROM changes")
        self.db.execute("DELETE FROM shows")

        self.db.commit()

        print("DEV DATABASE RESET")
    def get_changes(self, limit=100):
        """
        Return the most recent schedule changes.
        """

        rows = self.db.execute("""
            SELECT
                c.id,
                c.timestamp,
                c.show_id,
                c.change_type,
                c.field,
                c.old_value,
                c.new_value,

                s.show,
                s.venue,
                s.date,
                s.time

            FROM changes c

            LEFT JOIN shows s
                ON c.show_id = s.id

            ORDER BY c.id DESC

            LIMIT ?
        """, (limit,)).fetchall()

        return [dict(row) for row in rows]

    def migrate_userdata_json(self, json_path):

        import json
        import os

        if not os.path.exists(json_path):
            print("[INFO] No legacy userdata.json found")
            return False

        # Don't overwrite an existing DB.
        existing = self.get_user_setting("username")

        if existing:
            print("[INFO] User settings already exist in DB")
            return False

        try:

            with open(json_path, "r", encoding="utf-8") as f:
                settings = json.load(f)

        except Exception as e:

            print(
                "[ERROR] Could not read userdata.json:",
                e
            )

            return False

        self.save_user_settings(settings)

        print(
            f"[INFO] Migrated {len(settings)} settings "
            "from userdata.json into rhino.db"
        )

        return True

    def get_all_shows(self):
        cursor = self.db.execute("""
            SELECT *
            FROM shows
        """)

        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        return [
            dict(zip(columns, row))
            for row in rows
        ]


    def save_unmatched_payroll(self, payroll_item, paystub_id=None):
        """
        Store an unmatched payroll item.

        If the same payroll line has already been imported,
        do nothing instead of creating a duplicate.
        """

        existing = self.db.execute("""
            SELECT id
            FROM unmatched_payroll
            WHERE
                paystub_id = ?
                AND job_number = ?
                AND position = ?
                AND time_in = ?
                AND time_out = ?
        """, (
            paystub_id,
            payroll_item.get("job_number"),
            payroll_item.get("position"),
            payroll_item.get("time_in"),
            payroll_item.get("time_out"),
        )).fetchone()

        if existing:
            print(
                f"[DB] Unmatched payroll already exists: "
                f"{paystub_id} | "
                f"{payroll_item.get('job_number')} | "
                f"{payroll_item.get('time_in')}"
            )
            return False

        now = datetime.now().isoformat()

        self.db.execute("""
            INSERT INTO unmatched_payroll (
                paystub_id,
                paystub_imported_at,

                job_number,
                class,
                position,
                client,
                show,

                time_in,
                time_out,

                reg_hours,
                ot_hours,
                dt_hours,
                weekly_ot_hours,

                meal_penalty_hours,
                rest_break_penalty_hours,

                base_rate,
                blended_rate,
                pay,

                created_at
            )
            VALUES (
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?,
                ?, ?, ?, ?,
                ?, ?,
                ?, ?, ?,
                ?
            )
        """, (
            paystub_id,
            now,

            payroll_item.get("job_number"),
            payroll_item.get("class"),
            payroll_item.get("position"),
            payroll_item.get("client"),
            payroll_item.get("show"),

            payroll_item.get("time_in"),
            payroll_item.get("time_out"),

            payroll_item.get("reg_hours"),
            payroll_item.get("ot_hours"),
            payroll_item.get("dt_hours"),
            payroll_item.get("weekly_ot_hours"),

            payroll_item.get("meal_penalty_hours"),
            payroll_item.get("rest_break_penalty_hours"),

            payroll_item.get("base_rate"),
            payroll_item.get("blended_rate"),
            payroll_item.get("total"),

            now,
        ))

        self.db.commit()

        return True


    def update_show_payroll(self, show_id, payroll_item, paystub_id=None):
        """
        Store payroll information on an existing show.

        Only payroll-specific columns are updated.
        Normal Rhino schedule fields are left untouched.
        """

        self.db.execute("""
            UPDATE shows
            SET
                paystub_id = ?,
                paystub_imported_at = ?,

                time_in = ?,
                time_out = ?,

                reg_hours = ?,
                ot_hours = ?,
                dt_hours = ?,
                weekly_ot_hours = ?,

                meal_penalty_hours = ?,
                rest_break_penalty_hours = ?,

                base_rate = ?,
                blended_rate = ?,
                pay = ?

            WHERE id = ?
        """, (
            paystub_id,
            datetime.now().isoformat(),

            payroll_item.get("time_in"),
            payroll_item.get("time_out"),

            payroll_item.get("reg_hours"),
            payroll_item.get("ot_hours"),
            payroll_item.get("dt_hours"),
            payroll_item.get("weekly_ot_hours"),

            payroll_item.get("meal_penalty_hours"),
            payroll_item.get("rest_break_penalty_hours"),

            payroll_item.get("base_rate"),
            payroll_item.get("blended_rate"),
            payroll_item.get("total"),

            show_id,
        ))

        self.db.commit()









    def debug_payroll_columns(self):

        print("\n========== PAYROLL DB DEBUG ==========")

        columns = self.db.execute(
            "PRAGMA table_info(shows)"
        ).fetchall()

        print("\n[DB] SHOW COLUMNS:")

        for column in columns:
            print(
                f"    {column['name']:<30} "
                f"{column['type']}"
            )

        print("\n[DB] EXISTING SHOW DATA:")

        rows = self.db.execute("""
            SELECT
                date,
                show,
                position,
                time_in,
                time_out,
                reg_hours,
                ot_hours,
                dt_hours,
                base_rate,
                blended_rate,
                paystub_id,
                paystub_imported_at,
                pay,
                user_reported_hours,
                user_reported_meal_breaks,
                user_notes
            FROM shows
            ORDER BY date
            LIMIT 10
        """).fetchall()

        for row in rows:

            print(
                f"\n    {row['date']} | "
                f"{row['show']} | "
                f"{row['position']}"
            )

            print(
                f"        Paystub: "
                f"{row['paystub_id']} | "
                f"imported {row['paystub_imported_at']}"
            )

            print(
                f"        Payroll: "
                f"{row['time_in']} -> {row['time_out']} | "
                f"REG {row['reg_hours']} | "
                f"OT {row['ot_hours']} | "
                f"DT {row['dt_hours']}"
            )

            print(
                f"        Rates: "
                f"base=${row['base_rate']} | "
                f"blended=${row['blended_rate']} | "
                f"pay=${row['pay']}"
            )

            print(
                f"        User: "
                f"hours={row['user_reported_hours']} | "
                f"meal breaks={row['user_reported_meal_breaks']} | "
                f"notes={row['user_notes']!r}"
            )

        print("\n========== END DB DEBUG ==========\n")

    def debug_insert_payroll_test(self):

        row = self.db.execute("""
            SELECT id, date, show, position
            FROM shows
            ORDER BY date
            LIMIT 1
        """).fetchone()

        if row is None:
            print("[PAYROLL TEST] No shows found in database")
            return

        print(
            f"[PAYROLL TEST] Testing against: "
            f"{row['id']} | "
            f"{row['date']} | "
            f"{row['show']} | "
            f"{row['position']}"
        )

        self.db.execute("""
            UPDATE shows
            SET
                paystub_id = ?,
                paystub_imported_at = ?,

                time_in = ?,
                time_out = ?,

                reg_hours = ?,
                ot_hours = ?,
                dt_hours = ?,

                base_rate = ?,
                blended_rate = ?,
                pay = ?

            WHERE id = ?
        """, (
            "DEBUG-TEST",
            datetime.now().isoformat(),

            "8:00 AM",
            "9:00 PM",

            8.0,
            5.0,
            0.0,

            32.0,
            30.1935,
            496.0,

            row["id"],
        ))

        self.db.commit()

        print("[PAYROLL TEST] Updated successfully")


    def get_or_create_paystub(self, paystub):
        """
        Get an existing paystub record or create it.

        Returns:
            {
                "id": int,
                "paystub_key": str,
                "is_new": bool
            }
        """

        employee_number = str(
            paystub.get("employee_number") or ""
        ).strip()

        period_start = str(
            paystub.get("pay_period_start") or ""
        ).strip()

        period_end = str(
            paystub.get("pay_period_end") or ""
        ).strip()

        pay_date = str(
            paystub.get("pay_date") or ""
        ).strip()

        paystub_key = (
            f"{employee_number}|"
            f"{period_start}|"
            f"{period_end}|"
            f"{pay_date}"
        )

        now = datetime.now().isoformat()

        existing = self.db.execute("""
            SELECT id
            FROM paystubs
            WHERE paystub_key = ?
        """, (paystub_key,)).fetchone()

        if existing:
            self.db.execute("""
                UPDATE paystubs
                SET
                    pay_period_start = ?,
                    pay_period_end = ?,
                    pay_date = ?,
                    employee_name = ?,
                    employee_number = ?,
                    updated_at = ?
                WHERE id = ?
            """, (
                period_start,
                period_end,
                pay_date,
                paystub.get("employee_name"),
                employee_number,
                now,
                existing["id"],
            ))

            self.db.commit()

            return {
                "id": existing["id"],
                "paystub_key": paystub_key,
                "is_new": False,
            }

        cursor = self.db.execute("""
            INSERT INTO paystubs (
                paystub_key,
                pay_period_start,
                pay_period_end,
                pay_date,
                employee_name,
                employee_number,
                imported_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            paystub_key,
            period_start,
            period_end,
            pay_date,
            paystub.get("employee_name"),
            employee_number,
            now,
            now,
        ))

        self.db.commit()

        return {
            "id": cursor.lastrowid,
            "paystub_key": paystub_key,
            "is_new": True,
        }