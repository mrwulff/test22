import os
import sqlite3
from datetime import datetime
from kivy.app import App


class RhinoDatabase:

    def __init__(self):
        app = App.get_running_app()


        self.db_path = os.path.join(
            app.user_data_dir,
            "rhino.db",
        )

        self.db = sqlite3.connect(self.db_path)

        self.db.row_factory = sqlite3.Row

        self._create_tables()

    def _create_tables(self):

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

        self.db.commit()

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