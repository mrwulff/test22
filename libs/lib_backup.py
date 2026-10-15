import os
import json
import sqlite3
import zipfile

from datetime import datetime


def create_backup_archive(
    source_db,
    output_dir,
    include_credentials=False,
):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")

    archive_path = os.path.join(
        output_dir,
        "Schedulara-Backup-" + timestamp + ".zip",
    )

    snapshot_path = os.path.join(
        output_dir,
        "backup-snapshot-" + timestamp + ".db",
    )

    snapshot_db = None

    try:
        # Make a consistent snapshot of the live SQLite database.
        snapshot_db = sqlite3.connect(snapshot_path)

        source_db.backup(snapshot_db)

        # Exclude credentials by default.
        if not include_credentials:
            rows = snapshot_db.execute(
                "SELECT key FROM metadata"
            ).fetchall()

            sensitive_terms = (
                "password",
                "token",
                "secret",
                "credential",
                "auth",
            )

            for row in rows:
                key = str(row[0]).lower()

                if key in ("username", "password") or any(
                    term in key for term in sensitive_terms
                ):
                    snapshot_db.execute(
                        "DELETE FROM metadata WHERE key = ?",
                        (row[0],),
                    )

            snapshot_db.commit()

        # Refuse to export a corrupt snapshot.
        result = snapshot_db.execute(
            "PRAGMA integrity_check"
        ).fetchone()[0]

        if result != "ok":
            raise RuntimeError(
                "Backup database integrity check failed: " + str(result)
            )

        snapshot_db.close()
        snapshot_db = None

        manifest = {
            "format": "schedulara-backup",
            "version": 1,
            "created_at": datetime.now().isoformat(),
            "database": "rhino.db",
            "includes_login_credentials": bool(include_credentials),
        }

        with zipfile.ZipFile(
            archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as archive:
            archive.write(
                snapshot_path,
                arcname="rhino.db",
            )

            archive.writestr(
                "manifest.json",
                json.dumps(manifest, indent=2),
            )

        print("[BACKUP] Created:", archive_path)

        return archive_path

    finally:
        if snapshot_db is not None:
            snapshot_db.close()

        if os.path.exists(snapshot_path):
            os.remove(snapshot_path)

def validate_backup_archive(archive_path):
    import json
    import os
    import sqlite3
    import tempfile
    import zipfile

    if not os.path.isfile(archive_path):
        raise RuntimeError("Backup file does not exist.")

    if not zipfile.is_zipfile(archive_path):
        raise RuntimeError("The selected file is not a valid Schedulara backup.")

    temp_dir = tempfile.mkdtemp(prefix="schedulara_import_")

    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            names = archive.namelist()

            if "manifest.json" not in names:
                raise RuntimeError("Backup is missing manifest.json.")

            if "rhino.db" not in names:
                raise RuntimeError("Backup is missing rhino.db.")

            with archive.open("manifest.json") as f:
                manifest = json.load(f)

            if manifest.get("format") != "schedulara-backup":
                raise RuntimeError("This is not a Schedulara backup.")

            if manifest.get("version") != 1:
                raise RuntimeError(
                    "Unsupported backup version: "
                    + str(manifest.get("version"))
                )

            database_path = os.path.join(temp_dir, "rhino.db")
            archive.extract("rhino.db", temp_dir)

        db = sqlite3.connect(database_path)

        try:
            result = db.execute("PRAGMA integrity_check").fetchone()[0]

            if result != "ok":
                raise RuntimeError(
                    "The backup database failed its integrity check: "
                    + str(result)
                )
        finally:
            db.close()

        return {
            "manifest": manifest,
            "database_path": database_path,
            "temp_dir": temp_dir,
        }

    except Exception:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise