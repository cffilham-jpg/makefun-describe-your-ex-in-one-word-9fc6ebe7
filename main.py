"""Write the one-word competition entry without a trailing newline.

The entry is stored as UTF-8 bytes in ``entry.txt`` under the configured output
directory. If that directory cannot be used, write to a fresh system temporary
directory instead. The program uses only the Python standard library and does
not make network requests or create other output files.
"""

import os
from pathlib import Path
import tempfile


WORD = "Recalled"


def validate_word(word: str) -> None:
    if not isinstance(word, str):
        raise ValueError("Entry must be text.")
    if len(word) < 1 or len(word) > 111:
        raise ValueError(
            f"Entry must contain between 1 and 111 characters; got {len(word)}."
        )
    if any(character.isspace() for character in word):
        raise ValueError("Entry must be a single word without whitespace.")


def main() -> Path:
    validate_word(WORD)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    payload = WORD.encode("utf-8")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / "entry.txt"
        destination.write_bytes(payload)
    except OSError:
        output_dir = Path(tempfile.mkdtemp(prefix="makefun-entry-"))
        destination = output_dir / "entry.txt"
        destination.write_bytes(payload)
    return destination


if __name__ == "__main__":
    print(main())
