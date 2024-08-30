from shutil import rmtree
from subprocess import check_call

from jdk4py import JAVA_HOME
from jdk4py._added_modules import ADDED_MODULES
from jdk4py._included_locales import INCLUDED_LOCALES


def build_java_runtime() -> None:
    rmtree(JAVA_HOME, ignore_errors=True)

    check_call(  # noqa: S603
        [  # noqa: S607
            "jlink",
            "--no-man-pages",
            "--strip-debug",
            "--add-modules",
            ",".join(ADDED_MODULES),
            f"--include-locales={','.join(INCLUDED_LOCALES)}",
            "--output",
            JAVA_HOME,
        ],
    )


if __name__ == "__main__":
    build_java_runtime()
