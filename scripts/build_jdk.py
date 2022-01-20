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
    "jdk.localedata",
]

_LOCALES = [
    "bn-IN",
    "da-DK",
    "de-DE",
    "en-US",
    "en-GB",
    "es-ES",
    "es-MX",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "pt-BR",
    "ru-RU",
    "zh-CN",
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
            "--include-locales=",
            ",".join(_LOCALES),
            "--output",
            str(_JAVA_PATH),
        ],
    )


if __name__ == "__main__":
    build_java_executable_files()
