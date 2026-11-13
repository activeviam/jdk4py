import re
from dataclasses import dataclass
from pathlib import Path
from subprocess import run
from typing import Final, get_args

from build_java_runtime import _INCLUDED_LOCALES, _RegionSpecificLocale
from jdk4py import JAVA, JAVA_VERSION

_TEST_RESOURCES_DIRECTORY: Final = Path(__file__).parent / "resources"


def test_java_version() -> None:
    completed_process = run(  # noqa: S603
        [JAVA, "-version"],
        capture_output=True,
        check=True,
        text=True,
    )
    output = completed_process.stderr
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match, f"Unexpected output:\n{output}"
    version = match.group("version")
    assert tuple(int(number) for number in version.split(".")[:3]) == JAVA_VERSION


def _run_jar(name: str, /) -> str:
    return run(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / name],
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def test_jar_execution() -> None:
    output = _run_jar("HelloWorld.jar")
    assert output.strip() == "Hello, World"


def test_included_locales() -> None:
    output = _run_jar("PrintAvailableLocales.jar")
    available_locales = {
        locale.replace("_", "-") for locale in output.strip().splitlines()
    }
    missing_locales = _INCLUDED_LOCALES - available_locales
    assert not missing_locales


@dataclass(frozen=True)
class _NumberFormattingSeparators:
    decimal_separator: str
    grouping_separator: str


_COMMA: Final = ","
_DOT: Final = "."
_NARROW_NO_BREAK_SPACE: Final = chr(0x202F)
_NO_BREAK_SPACE: Final = chr(0x00A0)


def _get_number_formatting_separators(
    locale: _RegionSpecificLocale, /
) -> _NumberFormattingSeparators:
    match locale:
        case "bn-IN" | "en-GB" | "en-US" | "es-MX" | "ja-JP" | "zh-CN":
            return _NumberFormattingSeparators(
                decimal_separator=_DOT, grouping_separator=_COMMA
            )
        case "da-DK" | "de-DE" | "es-ES" | "it-IT" | "pt-BR":
            return _NumberFormattingSeparators(
                decimal_separator=_COMMA, grouping_separator=_DOT
            )
        case "fr-FR":
            return _NumberFormattingSeparators(
                decimal_separator=_COMMA,
                grouping_separator=_NARROW_NO_BREAK_SPACE,
            )
        case "ru-RU":
            return _NumberFormattingSeparators(
                decimal_separator=_COMMA, grouping_separator=_NO_BREAK_SPACE
            )


def test_locale_data_inclusion() -> None:
    """
    Check that each included locale uses its expected number formatting separators.

    ``jlink --include-locales=fr-FR`` does not retain ``FormatData_fr.class``,
    so ``DecimalFormatSymbols.getInstance(Locale.forLanguageTag("fr-FR"))``
    silently returns ROOT symbols.

    ``_INCLUDED_LOCALES`` must therefore list each region-specific locale alongside its language-only parent.
    """
    output = _run_jar("PrintLocaleNumberFormats.jar")
    expected = {
        locale: _get_number_formatting_separators(locale)
        for locale in get_args(_RegionSpecificLocale)
    }
    actual = {
        locale: _NumberFormattingSeparators(
            decimal_separator=chr(int(decimal_cp)),
            grouping_separator=chr(int(grouping_cp)),
        )
        for line in output.strip().splitlines()
        for locale, decimal_cp, grouping_cp in [line.split("\t")]
        if locale in expected
    }
    assert actual == expected, (
        "CLDR data not loaded for some locales (likely a missing language-only bundle)"
    )
