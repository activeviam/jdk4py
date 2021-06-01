from pathlib import Path
from shutil import rmtree
from subprocess import PIPE, Popen


_PROJECT_DIRECTORY = Path(__file__).parent.parent
_JAVA_PATH = _PROJECT_DIRECTORY / "jdk4py" / "java-runtime"

_MODULES = [
    "jdk.management.agent",
    "java.se",
    "jdk.unsupported",
    "jdk.security.auth",
    "jdk.crypto.ec",
    "jdk.jfr",
    "jdk.management.jfr",
]


def build_java_executable_files():
    rmtree(_JAVA_PATH, ignore_errors=True)

    process = Popen(
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
        stdout=PIPE,
        stderr=PIPE,
    )
    out, err = process.communicate()

    if process.returncode == 0:
        print("Successfully built the Java executables.")
        return
    else:
        print(
            f"Failed to build the Java executables with error code {process.returncode}."
        )
        print(out)
        raise SystemError(err)


if __name__ == "__main__":
    build_java_executable_files()
