"""JDK packaged for Python."""

from importlib.metadata import version as _version
from pathlib import Path as _Path
from typing import Final as _Final

_PACKAGE_DIRECTORY: _Final = _Path(__file__).parent

JAVA_HOME: _Final = _PACKAGE_DIRECTORY / "java-runtime"
JAVA: _Final = JAVA_HOME / "bin" / "java"

_VERSION: _Final = _version("jdk4py")
_JAVA_MAJOR, _JAVA_MINOR, _JAVA_PATCH, _LIB_VERSION = [
    int(number) for number in _VERSION.split(".")
]
JAVA_VERSION: _Final = _JAVA_MAJOR, _JAVA_MINOR, _JAVA_PATCH
