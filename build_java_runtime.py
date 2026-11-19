from collections.abc import Collection
from pathlib import Path
from shutil import rmtree, which
from subprocess import run
from typing import Final, Literal, TypeAlias, get_args

from jdk4py import JAVA_HOME, _get_release_property

_ADDED_MODULES: Final = frozenset(
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
_REGION_SPECIFIC_LOCALES: Final[Collection[str]] = get_args(_RegionSpecificLocale)

_INCLUDED_LOCALES: Final = frozenset(
    {
        locale
        for tag in _REGION_SPECIFIC_LOCALES
        # Expand each region-specific locale to also include its language-only locale so that `jlink --include-locales` retains the language-only locale bundles (e.g. `FormatData_fr.class`).
        # See https://github.com/openjdk/jdk/blob/jdk-25%2B35/src/jdk.jlink/share/classes/jdk/tools/jlink/internal/plugins/IncludeLocalesPlugin.java.
        for locale in (tag, tag.split("-", maxsplit=1)[0])
    },
)


def build_java_runtime() -> None:
    jlink = which("jlink")
    if jlink is None:
        message = "jlink not found."
        raise RuntimeError(message)
    # The JDK that jlink comes from, whose `release` file has the version with its build number, such as 25.0.5.1+2-LTS.
    # jlink only keeps the version without it, so it is added back for `JAVA_FULL_VERSION`.
    source_java_home = Path(jlink).resolve().parent.parent
    runtime_version = _get_release_property(source_java_home, "JAVA_RUNTIME_VERSION")

    rmtree(JAVA_HOME, ignore_errors=True)

    run(  # noqa: S603
        [
            jlink,
            "--no-man-pages",
            "--strip-debug",
            "--add-modules",
            ",".join(_ADDED_MODULES),
            f"--include-locales={','.join(_INCLUDED_LOCALES)}",
            "--release-info",
            f'add:JAVA_RUNTIME_VERSION="{runtime_version}"',
            "--output",
            JAVA_HOME,
        ],
        check=True,
    )


if __name__ == "__main__":
    build_java_runtime()
