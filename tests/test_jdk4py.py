import re
from dataclasses import dataclass
from pathlib import Path
from subprocess import run

from jdk4py import JAVA, JAVA_VERSION
from jdk4py._included_locales import INCLUDED_LOCALES

_TEST_RESOURCES_DIRECTORY = Path(__file__).parent / "resources"


def test_java_version() -> None:
    completed_process = run(  # noqa: S603
        [JAVA, "-version"],
        capture_output=True,
        check=True,
        text=True,
    )
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', completed_process.stderr)
    assert match, f"Unexpected output:\n{completed_process.stdout}"
    version = match.group("version")
    assert isinstance(version, str)
    assert tuple([int(number) for number in version.split(".")][:3]) == JAVA_VERSION


def test_jar_execution() -> None:
    completed_process = run(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / "HelloWorld.jar"],
        capture_output=True,
        check=True,
        text=True,
    )
    assert completed_process.stdout.strip() == "Hello, World"


def test_included_locales() -> None:
    completed_process = run(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / "PrintAvailableLocales.jar"],
        capture_output=True,
        check=True,
        text=True,
    )
    locales = {
        locale.replace("_", "-")
        for locale in completed_process.stdout.strip().splitlines()
    }
    assert locales.issuperset(INCLUDED_LOCALES)


@dataclass(frozen=True)
class NumberFormattingSeparators:
    decimal_separator: str
    grouping_separator: str


COMMA = ","
DOT = "."
NARROW_NO_BREAK_SPACE = chr(0x202F)
NO_BREAK_SPACE = chr(0x00A0)


_NUMBER_FORMATTING_EXPECTED_SEPARATORS = {
    "bn-IN": NumberFormattingSeparators(decimal_separator=DOT, grouping_separator=COMMA),
    "da-DK": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "de-DE": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "en-GB": NumberFormattingSeparators(decimal_separator=DOT, grouping_separator=COMMA),
    "en-US": NumberFormattingSeparators(decimal_separator=DOT, grouping_separator=COMMA),
    "es-ES": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "es-MX": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "fr-FR": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=NARROW_NO_BREAK_SPACE),
    "it-IT": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "ja-JP": NumberFormattingSeparators(decimal_separator=DOT, grouping_separator=COMMA),
    "pt-BR": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=DOT),
    "ru-RU": NumberFormattingSeparators(decimal_separator=COMMA, grouping_separator=NO_BREAK_SPACE),
}


def test_locale_data_is_loaded() -> None:
    """
    `jlink --include-locales=fr-FR` does not retain `FormatData_fr.class`,
    so `DecimalFormatSymbols.getInstance(Locale.forLanguageTag("fr-FR"))`
    silently returns ROOT symbols.

    `INCLUDED_LOCALES` must therefore list each region tag alongside its bare-language parent.
    """
    completed_process = run(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / "PrintLocaleNumberFormats.jar"],
        capture_output=True,
        check=True,
        text=True,
    )
    actual = {}
    for line in completed_process.stdout.strip().splitlines():
        tag, decimal_cp, grouping_cp = line.split("\t")
        actual[tag] = (chr(int(decimal_cp)), chr(int(grouping_cp)))

    mismatches = {
        tag: {"expected": expected, "actual": actual.get(tag)}
        for tag, expected in _NUMBER_FORMATTING_EXPECTED_SEPARATORS.items()
        if actual.get(tag) != expected
    }
    assert not mismatches, (
        f"CLDR data not loaded for these locales (likely a missing "
        f"parent-language bundle): {mismatches}"
    )
