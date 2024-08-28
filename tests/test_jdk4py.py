import json
import re
from pathlib import Path
from subprocess import STDOUT, check_output
from unittest import TestCase

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION

_TESTS_DIRECTORY = Path(__file__).parent
_TEST_RESOURCES_DIRECTORY = _TESTS_DIRECTORY / "resources"
_LOCALES_PATH = _TESTS_DIRECTORY.parent / "scripts" / "locales.json"


class TestJdk4py(TestCase):
    def test_java_home(self) -> None:
        self.assertEqual(JAVA, JAVA_HOME / "bin" / "java")

    def test_java_version(self) -> None:
        output = check_output([str(JAVA), "-version"], stderr=STDOUT, text=True)
        match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
        self.assertIsNotNone(match, f"Unexpected output:\n{output}")
        version = match.group("version")
        self.assertIsInstance(version, str)
        self.assertEqual(
            tuple([int(number) for number in str(version).split(".")][:3]), JAVA_VERSION
        )

    def test_jar_execution(self) -> None:
        jar_path = _TEST_RESOURCES_DIRECTORY / "HelloWorld.jar"
        output = check_output(
            [str(JAVA), "-jar", str(jar_path.absolute())], stderr=STDOUT, text=True
        )
        self.assertEqual(output.strip(), "Hello, World")

    def test_available_locales(self) -> None:
        path = _TEST_RESOURCES_DIRECTORY / "PrintAvailableLocales.jar"
        output = check_output(
            [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
        )
        actual_locales = set(
            locale.replace("_", "-") for locale in output.strip().splitlines()
        )
        expected_locales = set(json.loads(_LOCALES_PATH.read_bytes()))
        missing_locales = actual_locales - expected_locales
        self.assertSetEqual(missing_locales, {})
