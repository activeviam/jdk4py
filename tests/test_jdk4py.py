import re
from pathlib import Path
from subprocess import STDOUT, check_output

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION

_TESTS_DIRECTORY = Path(__file__).parent

_LOCALES = [
    "bn-IN",
    "da-DK",
    "de-DE",
    "en-US",
    "en-GB",
    "es-ES",
    "es-MX",
    "fr-FR",
    "it-IT",
    "ja-JP",
    "pt-BR",
    "ru-RU",
    "zh-CN",
]

def test_java_home():
    assert JAVA == JAVA_HOME / "bin" / "java"


def test_java_version():
    output = check_output([str(JAVA), "-version"], stderr=STDOUT, text=True)
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match
    version = match.group("version")
    assert version == ".".join(str(number) for number in JAVA_VERSION)


def test_locales():
    # The JAR can be regenerated like that:
    #    rm resources/GetLocales.jar
    #    javac resources/GetLocales.java
    #    jar cfe resources/GetLocales.jar resources.GetLocales resources/GetLocales.class
    #    jar tf resources/GetLocales.jar
    path = _TESTS_DIRECTORY / "resources" / "GetLocales.jar"
    output = check_output(
        [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
    )
    embedded_locales = output.strip().strip("][").replace(", ", "", 1).split(", ")
    for locale in _LOCALES:
        assert locale in embedded_locales


def test_jar_execution():
    # The JAR can be regenerated like that:
    #    rm resources/HelloWorld.jar
    #    javac resources/HelloWorld.java
    #    jar cfe resources/HelloWorld.jar resources.HelloWorld resources/HelloWorld.class
    #    jar tf resources/HelloWorld.jar
    path = _TESTS_DIRECTORY / "resources" / "HelloWorld.jar"
    output = check_output(
        [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
    )
    assert output.strip() == "Hello, World"
