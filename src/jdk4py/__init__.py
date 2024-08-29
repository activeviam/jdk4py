"""JDK packaged for Python."""

import json
from pathlib import Path

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"


_VERSION: str = json.loads((_PACKAGE_DIRECTORY / "version.json").read_bytes())
JAVA_VERSION: tuple[int, int, int] = tuple(
    int(number) for number in _VERSION.split(".")[:3]
)
