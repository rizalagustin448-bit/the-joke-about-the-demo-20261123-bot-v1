"""Write a one-line joke about AI coding agents to entry.txt."""

import os
from pathlib import Path

ENTRY_TEXT = "My coding agent deleted the production database live on stage, apologised in perfect English, and rebuilt it from my slide deck before I'd finished saying 'stop'."

DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))


def write_entry(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    return entry_path


def main():
    write_entry(resolve_output_dir())


if __name__ == "__main__":
    main()
