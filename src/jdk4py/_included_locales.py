# Each region-specific tag is paired with its bare-language parent so that
# `jlink --include-locales` retains the corresponding parent resource bundle
# (e.g. `FormatData_fr.class`).
# See https://github.com/openjdk/jdk/blob/jdk-25%2B35/src/jdk.jlink/share/classes/jdk/tools/jlink/internal/plugins/IncludeLocalesPlugin.java
INCLUDED_LOCALES = frozenset(
    [
        "bn",
        "bn-IN",
        "da",
        "da-DK",
        "de",
        "de-DE",
        "en",
        "en-GB",
        "en-US",
        "es",
        "es-ES",
        "es-MX",
        "fr",
        "fr-FR",
        "it",
        "it-IT",
        "ja",
        "ja-JP",
        "pt",
        "pt-BR",
        "ru",
        "ru-RU",
        "zh",
        "zh-CN",
    ],
)
