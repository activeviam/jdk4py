"""Script to set the version of Java and the library."""

import argparse
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
JAVA_VERSION_FILE = PROJECT_DIR / "jdk4py" / "java_version"

def main():
    """Main script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="Version to set")
    args = parser.parse_args()
    version = args.version
    with open(JAVA_VERSION_FILE,"w") as f:
        f.write(version)

if __name__ == "__main__":
    main()