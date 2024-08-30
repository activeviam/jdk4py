import re
from pathlib import Path
from subprocess import STDOUT, check_output

from jdk4py import JAVA, JAVA_VERSION
from jdk4py._included_locales import INCLUDED_LOCALES

_TEST_RESOURCES_DIRECTORY = Path(__file__).parent / "resources"


def test_java_version() -> None:
    output = check_output(  # noqa: S603
        [JAVA, "-version"],
        stderr=STDOUT,
        text=True,
    )
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match, f"Unexpected output:\n{output}"
    version = match.group("version")
    assert isinstance(version, str)
    assert tuple([int(number) for number in version.split(".")][:3]) == JAVA_VERSION


def test_jar_execution() -> None:
    output = check_output(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / "HelloWorld.jar"],
        stderr=STDOUT,
        text=True,
    ).strip()
    assert output == "Hello, World"


def test_included_locales() -> None:
    output = check_output(  # noqa: S603
        [JAVA, "-jar", _TEST_RESOURCES_DIRECTORY / "PrintAvailableLocales.jar"],
        stderr=STDOUT,
        text=True,
    ).strip()
    locales = {locale.replace("_", "-") for locale in output.splitlines()}
    assert locales.issuperset(INCLUDED_LOCALES)
