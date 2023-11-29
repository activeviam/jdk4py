"""JDK packaged for Python."""

from pathlib import Path

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME: Path = _PACKAGE_DIRECTORY.absolute() / "java-runtime"
JAVA: Path = JAVA_HOME / "bin" / "java"

_major, _minor, _patch = [
    int(part)
    for part in (_PACKAGE_DIRECTORY / "java_version.txt").read_text().strip().split(".")
]
JAVA_VERSION: tuple[int, int, int] = _major, _minor, _patch
