"""Test the paths entries of the API."""


def test_java_home():
    """Test the java home path."""
    from jdk4py import JAVA, JAVA_HOME

    assert JAVA == JAVA_HOME / "bin" / "java"

