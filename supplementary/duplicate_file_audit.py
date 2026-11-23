#!/usr/bin/env python3
"""Find byte-for-byte duplicate files without changing or deleting anything.

Usage:
    python supplementary/duplicate_file_audit.py
    python supplementary/duplicate_file_audit.py ./some/folder
    python supplementary/duplicate_file_audit.py . --exclude-dir datasets
"""

from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path

DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Return a SHA-256 digest while reading the file in small chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_exact_duplicates(
    root: Path, excluded_dirs: set[str]
) -> dict[str, list[Path]]:
    """Group files with identical bytes by their SHA-256 digest."""
    candidates: dict[int, list[Path]] = defaultdict(list)

    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in excluded_dirs for part in path.relative_to(root).parts[:-1]):
            continue
        try:
            candidates[path.stat().st_size].append(path)
        except OSError as error:
            print(f"Skipping unreadable file: {path} ({error})")

    duplicates: dict[str, list[Path]] = defaultdict(list)
    for same_size_files in candidates.values():
        if len(same_size_files) < 2:
            continue
        for path in same_size_files:
            try:
                duplicates[sha256_file(path)].append(path)
            except OSError as error:
                print(f"Skipping unreadable file: {path} ({error})")

    return {
        digest: sorted(paths)
        for digest, paths in duplicates.items()
        if len(paths) > 1
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Report byte-identical files without modifying the filesystem."
    )
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("."),
        help="Directory to scan (default: current directory).",
    )
    parser.add_argument(
        "--exclude-dir",
        action="append",
        default=[],
        metavar="NAME",
        help="Directory name to skip; may be supplied more than once.",
    )
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")

    excluded_dirs = DEFAULT_EXCLUDED_DIRS | set(args.exclude_dir)
    groups = find_exact_duplicates(root, excluded_dirs)

    if not groups:
        print(f"No exact duplicate files found in: {root}")
        return

    duplicate_file_count = sum(len(paths) for paths in groups.values())
    extra_copy_count = sum(len(paths) - 1 for paths in groups.values())

    print(f"Scanned directory: {root}")
    print(f"Exact duplicate groups: {len(groups)}")
    print(f"Files in duplicate groups: {duplicate_file_count}")
    print(f"Extra copies: {extra_copy_count}")
    print("\nDuplicate files:")

    for number, (digest, paths) in enumerate(sorted(groups.items()), start=1):
        print(f"\n[{number}] SHA-256: {digest}")
        for path in paths:
            print(f"  - {path.relative_to(root)}")

    print("\nNo files were changed or deleted.")


if __name__ == "__main__":
    main()
