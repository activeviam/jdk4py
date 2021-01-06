"""JDK packaged for Python."""

from typing import Union, List, Optional, Any
from pathlib import Path
from subprocess import Popen

_PACKAGE_DIRECTORY = Path(__file__).parent

JAVA_HOME = _PACKAGE_DIRECTORY.absolute() / "java-runtime"
JAVA = JAVA_HOME / "bin" / "java"

JAVA_VERSION, LIB_VERSION, MAJOR_JAVA_VERSION = (
    (_PACKAGE_DIRECTORY / filename).read_text().strip()
    for filename in ("java_version.txt", "lib_version.txt", "major_java_version.txt")
)

__version__ = ".".join((JAVA_VERSION, LIB_VERSION))


def java(
    java_args: List[str],
    **popen_args: Any,
) -> Popen:
    """Run a Java process with the given arguments.

    Args:
        jvm_args: The Java arguments, for instance ["HelloWorls.class", "-Xmx16G"]
        popen_args: Additional arguments to pass to the Popen

    Returns:
        The Popen process
    """
    return Popen([str(JAVA), *java_args], **popen_args)


def execute_jar(
    jar_path: Union[Path, str],
    jvm_args: Optional[List[str]] = None,
    **popen_args: Any,
) -> Popen:
    """Execute a JAR file.

    Args:
        jar_path: The path to the JAR file
        jvm_args: The JVM arguments, for instance ["-Xmx16G", "-Xms2G"]
        popen_args: Additional arguments to pass to the Popen

    Returns:
        The Popen process
    """
    if jvm_args is None:
        jvm_args = []
    return java(["-jar", str(jar_path), *jvm_args], **popen_args)
