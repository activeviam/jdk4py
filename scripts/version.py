from pathlib import Path

_PROJECT_DIRECTORY = Path(__file__).parent.parent
_JDK4PY_DIRECTORY = _PROJECT_DIRECTORY / "src" / "jdk4py"

VERSION = ".".join(
    (_JDK4PY_DIRECTORY / filename).read_text().strip()
    for filename in ["java_version.txt", "api_version.txt"]
)

if __name__ == "__main__":
    print(VERSION)  # noqa: T201
