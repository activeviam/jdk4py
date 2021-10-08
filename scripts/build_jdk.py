from pathlib import Path
from shutil import rmtree
from subprocess import check_call


_PROJECT_DIRECTORY = Path(__file__).parent.parent
_JAVA_PATH = _PROJECT_DIRECTORY / "jdk4py" / "java-runtime"

_MODULES = [
    "jdk.management.agent",
    "java.se",
    "jdk.unsupported",
    "jdk.security.auth",
    "jdk.crypto.ec",
    "jdk.jcmd",
    "jdk.jfr",
    "jdk.management.jfr",
]


def build_java_executable_files():
    rmtree(_JAVA_PATH, ignore_errors=True)

    check_call(
        [
            "jlink",
            "--no-header-files",
            "--no-man-pages",
            "--compress=2",
            "--strip-debug",
            "--add-modules",
            ",".join(_MODULES),
            "--output",
            str(_JAVA_PATH),
        ],
    )


if __name__ == "__main__":
    build_java_executable_files()
