"""JDK packaged for Python."""

import re as _re
from functools import cache as _cache
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


def _get_release_property(java_home: _Path, key: str, /) -> str:
    release_file = java_home / "release"
    for line in release_file.read_text(encoding="utf-8").splitlines():
        line_key, _, value = line.partition("=")
        if line_key == key:
            return value.strip('"')
    raise RuntimeError(f"No {key} in {release_file}.")


@_cache
def _get_java_full_version() -> str:
    runtime_version = _get_release_property(JAVA_HOME, "JAVA_RUNTIME_VERSION")
    # Drop the optional suffix after the build number, such as `-LTS` in 25.0.5.1+2-LTS.
    return _re.sub(r"(\+\d+)-.*$", r"\1", runtime_version)


def __getattr__(name: str) -> str:
    # `JAVA_FULL_VERSION` is read from the Java runtime on first access:
    # the runtime does not exist yet when `build_java_runtime.py` imports this module.
    if name == "JAVA_FULL_VERSION":
        return _get_java_full_version()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
