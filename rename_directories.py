"""Walk the solution directory, convert the name to lower snake case."""

import os
from pathlib import Path


def rename_directories():
    """Rename directories within the solution directory."""

    for root, dirnames, _ in os.walk("solutions"):
        for dirname in dirnames:
            p = Path(root, dirname)
            p.rename(to_lower_snake_case(str(p)))


def to_lower_snake_case(s: str):
    """Convert the string to a lower snake case, removing
    the first occurrance of ``.``."""

    replace_with_underscore = [" - ", "-", " "]

    s = s.lower().replace(".", "", 1)
    for repl in replace_with_underscore:
        s = s.replace(repl, "_")

    return s


if __name__ == "__main__":
    rename_directories()
