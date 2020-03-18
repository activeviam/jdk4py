"""Test the Java version."""

from jdk4py import JAVA


def test_java_version():
    """Test the Java version."""
    from jdk4py import JAVA_VERSION
    assert JAVA_VERSION == "11.0.2"