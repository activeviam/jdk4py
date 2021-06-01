from pathlib import Path
from subprocess import PIPE

from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION, execute_jar, java

_TESTS_DIRECTORY = Path(__file__).parent


def test_java_version():
    process = java(["--version"], stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert not err
    version = str(out).split("\n")[0].split(" ")[1]
    assert version == JAVA_VERSION


def test_java_home():
    assert JAVA == JAVA_HOME / "bin" / "java"


def test_hello_world_jar():
    # The JAR can be regenerated like that:
    #    rm resources/*.class
    #    rm resources/*.jar
    #    javac resources/HelloWorld.java
    #    jar cfe resources/hello.jar resources.HelloWorld resources/HelloWorld.class
    #    jar tf resources/hello.jar
    path = _TESTS_DIRECTORY / "resources" / "hello.jar"
    process = execute_jar(path.absolute(), stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert not err
    assert process.returncode == 0
    assert out == b"Hello, World\n" or out == b"Hello, World\r\n"
