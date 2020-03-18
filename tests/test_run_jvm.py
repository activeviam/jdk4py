"""Test the JDK."""

from pathlib import Path
from subprocess import PIPE
from jdk4py import java_jar

def test_run_hello_world_jar():
    """Test running the JDK with a hello world JAR.

    The JAR can be regenerated like that: 
        rm resources/*.class
        rm resources/*.jar
        javac resources/HelloWorld.java
        jar cfe resources/hello.jar resources.HelloWorld resources/HelloWorld.class
        jar tf resources/hello.jar
    """

    path = Path(__file__).parent / "resources" / "hello.jar"
    process = java_jar(path.absolute(), stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    assert out == b"Hello, World\n" or out == b"Hello, World\r\n"
    assert err == b""
    assert process.returncode == 0
