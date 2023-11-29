import json
from pathlib import Path
from shutil import rmtree
from subprocess import check_call


_SCRIPTS_DIRECTORY = Path(__file__).parent
_PROJECT_DIRECTORY = _SCRIPTS_DIRECTORY.parent
_JAVA_PATH = _PROJECT_DIRECTORY / "jdk4py" / "java-runtime"


_MODULES = [
    "java.se",
    "jdk.crypto.ec",
    "jdk.httpserver",
    "jdk.jcmd",
    "jdk.jfr",
    "jdk.localedata",
    "jdk.management.agent",
    "jdk.management.jfr",
    "jdk.security.auth",
    "jdk.unsupported",
    "jdk.zipfs",
]


def build_java_executable_files() -> None:
    rmtree(_JAVA_PATH, ignore_errors=True)

    locales = json.loads((_SCRIPTS_DIRECTORY / "locales.json").read_bytes())

    check_call(
        [
            "jlink",
            "--no-header-files",
            "--no-man-pages",
            "--compress=2",
            "--strip-debug",
            "--add-modules",
            ",".join(_MODULES),
            f"--include-locales={','.join(locales)}",
            "--output",
            str(_JAVA_PATH),
        ],
    )


if __name__ == "__main__":
    build_java_executable_files()
