import re
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
