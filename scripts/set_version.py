"""Script to set the version of Java and the library."""

import argparse
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
JAVA_VERSION_FILE = PROJECT_DIR / "jdk4py" / "java_version.txt"


def set_version(version: int):
    JAVA_VERSION_FILE.write_text(f"{version}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="Version to set")
    args = parser.parse_args()
    set_version(args.version)
