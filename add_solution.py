"""Generate a solution scaffold for a question."""

import sys
from pathlib import Path
import time
from rename_directories import to_lower_snake_case


def generate_file(question_name: str):
    """
    Generate a file based on the question name.

    Args:
        question_name: The question name, in the form of ``123. This is the question``.
    """
    filename = to_lower_snake_case(question_name)
    month = time.strftime("%b").lower()
    year = time.strftime("%Y")

    dir_path = Path(f"solutions/{month}_{year}/{filename}")
    if not dir_path.exists():
        dir_path.mkdir()

    file_path = dir_path / "solution.py"
    if file_path.exists():
        raise RuntimeError(f"{file_path} already exists.")

    with file_path.open(mode="w"):
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Must provide a question name in quotes.")

    generate_file(sys.argv[1])
