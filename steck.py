import pathlib

from typing import Tuple

import click
import requests

from magic import Magic


mime_map = {
    "text/plain": "text",
    "text/x-python": "python",
}


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
@click.argument("files", nargs=-1)
def paste(confirm: bool, magic: bool, files: Tuple[str]) -> None:
    """Paste some files matching a pattern."""

    if not files:
        print("No files, did you forget to pass any?")
        return

    if confirm:
        print(
            f"You are about to paste the following {len(files)} files. Do you want to continue?"
        )

        for file in files:
            if pathlib.Path(file).is_file():
                print(f" - {file}")

        if input("Continue? [y/N] ").lower() != "y":
            return None

    guesser = Magic(mime=True)

    collected = []

    for file in files:
        path = pathlib.Path(file)

        if not path.is_file():
            continue

        collected.append(
            (
                path.name,
                open(path).read(),
                mime_map.get(guesser.from_file(file), "text")
                if magic
                else "text",
            )
        )

    data = {
        "expiry": "1day",
        "files": [
            {"name": name, "content": content, "lexer": lexer}
            for name, content, lexer in collected
        ],
    }

    response = requests.post(
        "https://bpaste.net/api/v1/paste", json=data
    ).json()

    print("View Paste", response["link"])
    print("Remove Paste", response["removal"])


if __name__ == "__main__":
    raise SystemExit(main())
