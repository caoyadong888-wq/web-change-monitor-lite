#!/usr/bin/env python3
"""SHA-256 two local files and print MATCH or DIFFER. No snapshot and no network."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare SHA-256 of two local files.")
    parser.add_argument("left")
    parser.add_argument("right")
    try:
        args = parser.parse_args(argv)
        left = digest(Path(args.left))
        right = digest(Path(args.right))
    except OSError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2
    status = "MATCH" if left == right else "DIFFER"
    print("status: %s" % status)
    print("left_sha256: %s" % left)
    print("right_sha256: %s" % right)
    return 0 if status == "MATCH" else 1


if __name__ == "__main__":
    sys.exit(main())
