"""JDK packaged for Python."""

import json
from pathlib import Path

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"


JAVA_VERSION: tuple[int, int, int] = tuple(
    json.loads((_PACKAGE_DIRECTORY / "versions.json").read_bytes())["java"],
)
