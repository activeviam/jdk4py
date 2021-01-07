from pathlib import Path
from subprocess import Popen, PIPE

_TESTS_DIRECTORY = Path(__file__).parent

def test_output():
    process = Popen(["echo", "\"test\""], stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert err == b""
    assert out == "test"

def test_java_version():
    from jdk4py import java, JAVA_VERSION

    process = java(["--version"], stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert err == b""
    version = str(out).split("\n")[0].split(" ")[1]
    assert version[:version.rindex(".")] == JAVA_VERSION

def test_major_java_version():
    from jdk4py import MAJOR_JAVA_VERSION

    assert MAJOR_JAVA_VERSION == "11"

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
    assert err == b""
    assert out == b"Hello, World\n" or out == b"Hello, World\r\n"
    assert process.returncode == 0
