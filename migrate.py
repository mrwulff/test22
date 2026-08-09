cd /opt/lab && source .venv/bin/activate


from pathlib import Path

import typer
from rich import print

from lab.services.docker import DockerService
from lab.generators.compose import write_compose
from lab.generators.env import write_env
from lab.generators.readme import write_readme

app = typer.Typer()


CATEGORIES = {
    "media": {
        "sonarr",
        "radarr",
        "bazarr",
        "prowlarr",
        "sabnzbd",
        "qbittorrent",
        "plex",
        "tautulli",
        "huntarr",
        "cleanuparr",
        "overseerr",
        "seerr",
    },
    "network": {
        "npm",
        "adguardhome",
        "nginx",
    },
    "printing": {
        "bambuddy",
        "spoolman",
        "obico",
    },
    "utilities": {
        "homepage",
        "heimdall",
        "filebrowser",
        "playnite",
        "portainer",
    },
    "automation": {
        "homeassistant",
    },
}


def guess_category(name: str):

    for category, services in CATEGORIES.items():

        if name.lower() in services:
            return category

    return "misc"


@app.command()
def generate(name: str):

    docker = DockerService()

    container = docker.container(name)

    category = guess_category(container.name)

    stack = Path("/opt/stacks") / category / container.name

    stack.mkdir(parents=True, exist_ok=True)

    #
    # Standard Lab directories
    #

    for folder in (
        "config",
        "data",
        "logs",
        "backups",
    ):

        d = stack / folder

        d.mkdir(exist_ok=True)

        (d / ".gitkeep").touch(exist_ok=True)

    #
    # .gitignore
    #



import subprocess

FOLDER_MAP = {
    "/config": "config",
    "/database": "data",
    "/app/data": "data",
    "/app/logs": "logs",
    "/opt/adguardhome/work": "data",
    "/opt/adguardhome/conf": "config",
}


@app.command()
def copy(name: str):

    docker = DockerService()

    container = docker.container(name)

    category = guess_category(container.name)

    stack = Path("/opt/stacks") / category / container.name

    mounts = docker.mounts(container.name)

    copied = False

    for mount in mounts:

        if mount["Type"] != "volume":
            continue

        volume = mount["Name"]
        dest = mount["Destination"]

        folder = FOLDER_MAP.get(
            dest,
            dest.strip("/").split("/")[-1],
        )

        target = stack / folder
        target.mkdir(parents=True, exist_ok=True)

        print()
        print(f"[cyan]{volume}[/]")
        print(f"  -> {target}")

        cmd = [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{volume}:/from",
            "-v",
            f"{target.resolve()}:/to",
            "alpine",
            "sh",
            "-c",
            "cp -av /from/. /to/",
        ]

        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
        )

        if result.returncode:

            print(result.stderr)
            raise typer.Exit(1)

        #
        # Count copied files
        #

        count = subprocess.run(
            [
                "find",
                str(target),
                "-type",
                "f",
            ],
            text=True,
            capture_output=True,
        )

        files = len(
            [
                x
                for x in count.stdout.splitlines()
                if x.strip()
            ]
        )

        print(f"[green]✓[/] {files} files")

        copied = True

    if not copied:

        print()
        print("[green]✓[/] No named Docker volumes detected.")
        
        
        
        
    gitignore = """config/*
!config/.gitkeep

data/*
!data/.gitkeep

logs/*
!logs/.gitkeep

backups/*
!backups/.gitkeep
"""

    (stack / ".gitignore").write_text(gitignore)

    #
    # Generate files
    #

    write_compose(container, stack)
    write_env(container, stack)
    write_readme(container, stack)

    print()

    print(f"[green]✓[/] Generated [cyan]{stack}[/]")

    print()

    print("[bold]Created[/]")

    print("  compose.yml")
    print("  .env")
    print("  README.md")
    print("  .gitignore")

    print()

    print("[bold]Directories[/]")

    print("  config/")
    print("  data/")
    print("  logs/")
    print("  backups/")

    #
    # Named volumes
    #

    mounts = docker.mounts(container.name)

    named = []

    for mount in mounts:

        if mount["Type"] == "volume":

            named.append(mount["Name"])

    if named:

        print()

        print("[yellow]Named Docker volumes detected:[/]")

        for volume in named:

            print(f"  • {volume}")

        print()

        print("Next step:")

        print(f"  lab migrate copy {container.name}")

    else:

        print()

        print("[green]No Docker named volumes detected.[/]")