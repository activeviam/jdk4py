"""JDK packaged for Python."""

from importlib.metadata import version as _version
from pathlib import Path as _Path

_PACKAGE_DIRECTORY = _Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"

_VERSION = _version("jdk4py")
_JAVA_MAJOR, _JAVA_MINOR, _JAVA_PATCH, _LIB_VERSION = [
    int(number) for number in _VERSION.split(".")
]
JAVA_VERSION = _JAVA_MAJOR, _JAVA_MINOR, _JAVA_PATCH
