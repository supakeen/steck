import pathlib

from typing import Tuple

import click
import requests
import magic


mime_map = {
    "text/plain": "text",
    "text/x-python": "python",
}


@click.group()
def main() -> None:
    """Steck, a pastebin client for pinnwand."""
    return


@main.command()
@click.argument("files", nargs=-1)
def paste(files: Tuple[str]) -> None:
    """Paste some files matching a pattern."""
    guesser = magic.Magic(mime=True)

    collect = [
        (
            pathlib.Path(file).name,
            open(file).read(),
            mime_map.get(guesser.from_file(file), "text"),
        )
        for file in files
        if pathlib.Path(file).is_file()
    ]

    data = {
        "expiry": "1day",
        "files": [
            {"name": name, "content": content, "lexer": lexer}
            for name, content, lexer in collect
        ],
    }

    response = requests.post(
        "https://bpaste.net/api/v1/paste", json=data
    ).json()

    print("View Paste", response["link"])
    print("Remove Paste", response["removal"])


if __name__ == "__main__":
    raise SystemExit(main())
