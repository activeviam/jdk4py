import json
import re
from pathlib import Path
from subprocess import STDOUT, check_output

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION
from jdk4py._included_locales import INCLUDED_LOCALES


_TEST_RESOURCES_DIRECTORY = Path(__file__).parent / "resources"


def test_java_home() -> None:
    assert JAVA == JAVA_HOME / "bin" / "java"


def test_java_version() -> None:
    output = check_output([str(JAVA), "-version"], stderr=STDOUT, text=True)
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match, f"Unexpected output:\n{output}"
    version = match.group("version")
    assert isinstance(version, str)
    assert tuple([int(number) for number in version.split(".")][:3]) == JAVA_VERSION


def test_jar_execution() -> None:
    jar_path = _TEST_RESOURCES_DIRECTORY / "HelloWorld.jar"
    output = check_output(
        [str(JAVA), "-jar", str(jar_path.absolute())], stderr=STDOUT, text=True
    )
    assert output.strip() == "Hello, World"


def test_available_locales() -> None:
    path = _TEST_RESOURCES_DIRECTORY / "PrintAvailableLocales.jar"
    output = check_output(
        [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
    )
    actual_locales = set(
        locale.replace("_", "-") for locale in output.strip().splitlines()
    )
    assert INCLUDED_LOCALES.issubset(actual_locales)
