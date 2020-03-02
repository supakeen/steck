import pathlib

from typing import Tuple, List

import click
import requests

from magic import Magic


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
        print("No paths found, did you forget to pass some?")
        return

    files = aggregate(*paths)

    if confirm:
        print(
            f"You are about to paste the following {len(files)} files. Do you want to continue?"
        )

        for file in files:
            print(f" - {file}")

        if input("Continue? [y/N] ").lower() != "y":
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
        "https://bpaste.net/api/v1/paste", json=data
    ).json()

    print("View Paste", response["link"])
    print("Remove Paste", response["removal"])


if __name__ == "__main__":
    raise SystemExit(main())
