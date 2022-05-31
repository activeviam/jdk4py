import json
import os
import platform
from pathlib import Path
from shutil import copytree, rmtree
from subprocess import check_call


_SCRIPTS_DIRECTORY = Path(__file__).parent
_PROJECT_DIRECTORY = _SCRIPTS_DIRECTORY.parent
_JAVA_PATH = _PROJECT_DIRECTORY / "jdk4py" / "java-runtime"

_MACHINE_TO_ARCHITECTURE = {
    "AMD64": "x64",
    "arm64": "aarch64",
    "x86_64": "x64",
    **{architecture: architecture for architecture in ["aarch64", "x64"]},
}


_MODULES = [
    "jdk.management.agent",
    "java.se",
    "jdk.unsupported",
    "jdk.security.auth",
    "jdk.crypto.ec",
    "jdk.jcmd",
    "jdk.jfr",
    "jdk.management.jfr",
    "jdk.localedata",
]


def build_java_executable_files() -> None:
    rmtree(_JAVA_PATH, ignore_errors=True)

    # current_architecture = _MACHINE_TO_ARCHITECTURE[platform.machine()]
    # if current_architecture != os.environ["JDK4PY_ARCHITECTURE"]:
    #     # The target architecture is not the same as the one of the current machine.
    #     # `jlink` would produce a JDK unusable on the target architecture.
    #     # The whole downloaded JDK will be used instead.
    #     copytree(os.environ["JAVA_HOME"], _JAVA_PATH)
    #     return

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
            "--module-path",
            f"""{os.environ["JAVA_HOME"]}/jmods""",
            "--output",
            str(_JAVA_PATH),
        ],
    )


if __name__ == "__main__":
    build_java_executable_files()
