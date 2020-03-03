import pathlib

from typing import Tuple, List

import click
import requests

from magic import Magic
from termcolor import colored


mime_map = {
    "text/plain": "text",
    "text/x-python": "python",
}


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
    default=True,
    help="Enable or disable confirmation.",
)
@click.option(
    "--magic/--no-magic",
    default=True,
    help="Enable or disable guessing file types.",
)
@click.argument("paths", nargs=-1)
def paste(confirm: bool, magic: bool, paths: Tuple[str]) -> None:
    """Paste some files matching a pattern."""

    if not paths:
        print(colored("No paths found, did you forget to pass some?", "red"))
        return

    files = aggregate(*paths)

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
        print()

    if confirm:
        if input(colored("Continue? [y/N] ", "yellow")).lower() != "y":
            return None
        print()

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
        "https://bpaste.net/api/v1/paste", json=data
    ).json()

    print(colored("Completed paste.", "green"))
    print("View link:   ", response["link"])
    print("Removal link:", response["removal"])


if __name__ == "__main__":
    raise SystemExit(main())
