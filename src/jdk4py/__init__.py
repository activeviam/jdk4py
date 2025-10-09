"""JDK packaged for Python."""

from importlib.metadata import version as _version
from pathlib import Path

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"

_VERSION = _version("jdk4py")
_MAJOR, _MINOR, _PATCH = tuple(int(number) for number in _VERSION.split(".")[:3])
JAVA_VERSION = _MAJOR, _MINOR, _PATCH
