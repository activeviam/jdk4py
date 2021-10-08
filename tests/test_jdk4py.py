import re
from pathlib import Path
from subprocess import STDOUT, check_output

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION

_TESTS_DIRECTORY = Path(__file__).parent


def test_java_home():
    assert JAVA == JAVA_HOME / "bin" / "java"


def test_java_version():
    output = check_output([str(JAVA), "-version"], stderr=STDOUT, text=True)
    match = re.match(r'^openjdk version "(?P<version>[^"]+)"', output)
    assert match
    version = match.group("version")
    assert version == ".".join(str(number) for number in JAVA_VERSION)


def test_jar_execution():
    # The JAR can be regenerated like that:
    #    rm resources/*.class
    #    rm resources/*.jar
    #    javac resources/HelloWorld.java
    #    jar cfe resources/HelloWorld.jar resources.HelloWorld resources/HelloWorld.class
    #    jar tf resources/HelloWorld.jar
    path = _TESTS_DIRECTORY / "resources" / "HelloWorld.jar"
    output = check_output(
        [str(JAVA), "-jar", str(path.absolute())], stderr=STDOUT, text=True
    )
    assert output.strip() == "Hello, World"
