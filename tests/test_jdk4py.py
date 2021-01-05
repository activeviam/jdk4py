from pathlib import Path
from subprocess import PIPE

_TESTS_DIRECTORY = Path(__file__).parent


def test_java_version():
    from jdk4py import JAVA_VERSION

    assert JAVA_VERSION == "11"


def test_java_home():
    from jdk4py import JAVA, JAVA_HOME

    assert JAVA == JAVA_HOME / "bin" / "java"


def test_hello_world_jar():
    from jdk4py import execute_jar

    # The JAR can be regenerated like that:
    #    rm resources/*.class
    #    rm resources/*.jar
    #    javac resources/HelloWorld.java
    #    jar cfe resources/hello.jar resources.HelloWorld resources/HelloWorld.class
    #    jar tf resources/hello.jar
    path = _TESTS_DIRECTORY / "resources" / "hello.jar"
    process = execute_jar(path.absolute(), stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert out == b"Hello, World\n" or out == b"Hello, World\r\n"
    assert err == b""
    assert process.returncode == 0
