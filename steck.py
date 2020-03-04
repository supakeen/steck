import pathlib
import subprocess

from typing import Tuple, List

import toml
import appdirs
import click
import requests

from magic import Magic
from termcolor import colored


mime_map = {
    "text/plain": "text",
    "text/x-python": "python",
}

configuration_path = (
    pathlib.Path(appdirs.user_config_dir("steck")) / "steck.toml"
)

if configuration_path.exists():
    with open(configuration_path) as f:
        configuration = toml.load(f)
else:
    configuration = {
        "base": "https://bpaste.net/",
        "confirm": True,
        "magic": True,
        "ignore": True,
    }


def ignored(*passed_paths: str,) -> List[str]:
    try:
        process = subprocess.run(  # type: ignore
            ["git", "check-ignore"] + list(passed_paths),
            capture_output=True,
            encoding="utf8",
        )
    except subprocess.CalledProcessError:
        return list(passed_paths)
    else:
        return list(set(passed_paths) - set(process.stdout.splitlines()))


def aggregate(
    *passed_paths: str, recursive: bool = False
) -> List[pathlib.Path]:
    """Get all the paths passed as arguments and turn them into
       pathlib.Paths."""

    stack = []

    for passed_path in passed_paths:
        path = pathlib.Path(passed_path)

        if path.is_file():
            stack.append(path)

    return stack


def guess(path: pathlib.Path) -> str:
    """Guess a lexer type based on a path."""
    return mime_map.get(Magic(mime=True).from_file(str(path)), "text")


@click.group()
def main() -> None:
    """Steck, a pastebin client for pinnwand."""
    return


@main.command()
@click.option(
    "--confirm/--no-confirm",
    default=configuration["confirm"],
    help="Enable or disable confirmation.",
)
@click.option(
    "--magic/--no-magic",
    default=configuration["magic"],
    help="Enable or disable guessing file types.",
)
@click.option(
    "--ignore/--no-ignore",
    default=configuration["ignore"],
    help="Enable or disable .gitignore checking.",
)
@click.argument("paths", nargs=-1)
def paste(confirm: bool, magic: bool, ignore: bool, paths: Tuple[str]) -> None:
    """Paste some files matching a pattern."""
    if not paths:
        print(colored("No paths found, did you forget to pass some?", "red"))
        return

    if ignore:
        filtered = ignored(*paths)

    if not filtered:
        print(colored("No paths found, did you forget to pass some?", "red"))
        return

    files = aggregate(*paths)

    if not len(files):
        print(colored("No files found in given paths?", "red"))
        return

    if confirm:
        print(
            colored(
                f"You are about to paste the following {len(files)} files. Do you want to continue?",
                "yellow",
            )
        )
    else:
        print(colored(f"Pasting the following {len(files)} files.", "yellow"))

    for file in files:
        print(f" - {file}")

    if confirm:
        print()
        if input(colored("Continue? [y/N] ", "yellow")).lower() != "y":
            return None

    data = {
        "expiry": "1day",
        "files": [
            {
                "name": file.name,
                "content": file.read_text(),
                "lexer": guess(file) if magic else "text",
            }
            for file in files
        ],
    }

    response = requests.post(
        f"{configuration['base']}api/v1/paste", json=data
    ).json()

    print()
    print(colored("Completed paste.", "green"))
    print("View link:   ", response["link"])
    print("Removal link:", response["removal"])


if __name__ == "__main__":
    raise SystemExit(main())
