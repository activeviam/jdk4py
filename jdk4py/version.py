"""Version of the package."""

from pathlib import Path

_PARENT = Path(__file__).parent

LIB_VERSION = "1"

with open(_PARENT / "java_version") as f:
    JAVA_VERSION = f.read()

JAVA_VERSION = "0.0.1" # BETA: replace the Java version by 0.0.1
VERSION = f"{JAVA_VERSION}.{LIB_VERSION}"