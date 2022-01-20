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
    "bn_IN",
    "da_DK",
    "de_DE",
    "en_US",
    "en_GB",
    "es_ES",
    "es_MX",
    "fr_FR",
    "it_IT",
    "ja_JP",
    "pt_BR",
    "ru_RU",
    "zh_CN",
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
            f"--include-locales={','.join(_LOCALES)}",
            "--output",
            str(_JAVA_PATH),
        ],
    )


if __name__ == "__main__":
    build_java_executable_files()
