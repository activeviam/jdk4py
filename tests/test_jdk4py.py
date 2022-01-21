import json
import re
from pathlib import Path
from subprocess import STDOUT, check_output

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION

TESTS_DIRECTORY = Path(__file__).parent
TEST_RESOURCES_DIRECTORY = TESTS_DIRECTORY / "resources"
LOCALES_PATH = TESTS_DIRECTORY.parent / "scripts" / "locales.json"


def test_java_home():
    assert JAVA == JAVA_HOME / "bin" / "java"


def test_java_version():
    output = check_output([str(JAVA), "-version"], stderr=STDOUT, text=True)
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match
    version = match.group("version")
    assert version == ".".join(str(number) for number in JAVA_VERSION)


def test_jar_execution():
    jar_path = TEST_RESOURCES_DIRECTORY / "HelloWorld.jar"
    output = check_output(
        [str(JAVA), "-jar", str(jar_path.absolute())], stderr=STDOUT, text=True
    )
    assert output.strip() == "Hello, World"


def test_available_locales():
    path = TEST_RESOURCES_DIRECTORY / "PrintAvailableLocales.jar"
    output = check_output(
        [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
    )
    actual_locales = set(
        locale.replace("_", "-") for locale in output.strip().splitlines()
    )
    expected_locales = set(json.loads(LOCALES_PATH.read_bytes()))
    assert expected_locales.issubset(actual_locales)
