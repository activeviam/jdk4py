from collections.abc import Collection
from typing import Literal, TypeAlias, get_args

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

INCLUDED_LOCALES = frozenset(
    {
        locale
        for tag in _REGION_SPECIFIC_LOCALES
        # Expand each region-specific locale to also include its language-only locale so that `jlink --include-locales` retains the language-only locale bundles (e.g. `FormatData_fr.class`).
        # See https://github.com/openjdk/jdk/blob/jdk-25%2B35/src/jdk.jlink/share/classes/jdk/tools/jlink/internal/plugins/IncludeLocalesPlugin.java.
        for locale in (tag, tag.split("-", maxsplit=1)[0])
    },
)
