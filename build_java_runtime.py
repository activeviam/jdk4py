from pathlib import Path
from shutil import rmtree, which
from subprocess import check_call

from jdk4py import JAVA_HOME, _get_release_property
from jdk4py._added_modules import ADDED_MODULES
from jdk4py._included_locales import INCLUDED_LOCALES


def build_java_runtime() -> None:
    jlink = which("jlink")
    if jlink is None:
        message = "jlink not found."
        raise RuntimeError(message)
    # The `release` file of the JDK that jlink comes from has the version with its
    # build number, such as 21.0.13.1+2-LTS. jlink only keeps the version without it,
    # so it is added back for `JAVA_FULL_VERSION`.
    source_java_home = Path(jlink).resolve().parent.parent
    runtime_version = _get_release_property(source_java_home, "JAVA_RUNTIME_VERSION")

    rmtree(JAVA_HOME, ignore_errors=True)

    check_call(  # noqa: S603
        [
            jlink,
            "--no-man-pages",
            "--strip-debug",
            "--add-modules",
            ",".join(ADDED_MODULES),
            f"--include-locales={','.join(INCLUDED_LOCALES)}",
            "--release-info",
            f'add:JAVA_RUNTIME_VERSION="{runtime_version}"',
            "--output",
            JAVA_HOME,
        ],
    )


if __name__ == "__main__":
    build_java_runtime()
