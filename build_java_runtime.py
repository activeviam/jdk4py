from collections.abc import Collection
from shutil import rmtree
from subprocess import check_call
from typing import Literal, TypeAlias, get_args

from jdk4py import JAVA_HOME

_ADDED_MODULES = frozenset(
    {
        "java.se",
        "jdk.crypto.ec",
        "jdk.httpserver",
        "jdk.jcmd",
        "jdk.jdwp.agent",
        "jdk.jfr",
        "jdk.localedata",
        "jdk.management.agent",
        "jdk.management.jfr",
        "jdk.net",
        "jdk.security.auth",
        "jdk.unsupported",
        "jdk.zipfs",
    },
)

_RegionSpecificLocale: TypeAlias = Literal[
    "bn-IN",
    "da-DK",
    "de-DE",
    "en-GB",
    "en-US",
    "es-ES",
    "es-MX",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "pt-BR",
    "ru-RU",
    "zh-CN",
]
_REGION_SPECIFIC_LOCALES: Collection[str] = get_args(_RegionSpecificLocale)

_INCLUDED_LOCALES = frozenset(
    {
        locale
        for tag in _REGION_SPECIFIC_LOCALES
        # Expand each region-specific locale to also include its language-only locale so that `jlink --include-locales` retains the language-only locale bundles (e.g. `FormatData_fr.class`).
        # See https://github.com/openjdk/jdk/blob/jdk-25%2B35/src/jdk.jlink/share/classes/jdk/tools/jlink/internal/plugins/IncludeLocalesPlugin.java.
        for locale in (tag, tag.split("-", maxsplit=1)[0])
    },
)


def build_java_runtime() -> None:
    rmtree(JAVA_HOME, ignore_errors=True)

    check_call(  # noqa: S603
        [  # noqa: S607
            "jlink",
            "--no-man-pages",
            "--strip-debug",
            "--add-modules",
            ",".join(_ADDED_MODULES),
            f"--include-locales={','.join(_INCLUDED_LOCALES)}",
            "--output",
            JAVA_HOME,
        ],
    )


if __name__ == "__main__":
    build_java_runtime()
